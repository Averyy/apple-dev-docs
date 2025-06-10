# Enabling Apple Intelligence summarization and prioritization

**Framework**: Core Spotlight

Summarize and prioritize app content using Spotlight extensions.

#### Overview

In iOS 18.4 and macOS 15.4 and later, Apple Intelligence can optionally summarize mail, messages, and audio transcripts, and prioritize mail and messages content when you provide the content to Core Spotlight.

Enable this functionality by providing a Spotlight delegate app extension for your app.

The following example demonstrates adding summarization and prioritization to a messaging app. The process you use to add a Spotlight app extension is the same for other kinds of apps; the difference is the content type of the items that the system indexes to Spotlight.

#### Create a Spotlight Delegate App Extension

To create a Spotlight delegate app extension, add a new target to your app’s Xcode project and select “CoreSpotlight Delegate”.

In the app extension, override the [`searchableItemsDidUpdate(_:)`](CSSearchableIndexDelegate/searchableItemsDidUpdate(_:).md) method to write to the app’s shared group information store, such as a database:

```swift
override func searchableItemsDidUpdate(_ items: [CSSearchableItem]) {
    for item in items {
        if let isPriority = item.attributeSet.isPriority {
            // Item has a priority classification.
        }
        if let summary = item.attributeSet.textContentSummary {
           // Item has a summary.
        }
    }
}
```

Spotlight calls this method whenever a mail, message, or audio transcript you provide finishes processing and Apple Intelligence updates it with a summary or priority.

#### Create a Searchable Item in Your App

In your messaging app, you create a [`CSSearchableItem`](cssearchableitem.md) that contains the content Spotlight indexes:

```swift
let attributeSet = CSSearchableItemAttributeSet()
attributeSet.contentType = UTType.message.identifier
attributeSet.textContent = "You should replace this attribute with the text content for this particular message item. The length of this content must be at least 200 characters for it to be eligible for single-message summarization."
attributeSet.domainIdentifier = "conversationId"
attributeSet.contentCreationDate = Date.now
attributeSet.authors = [CSPerson(displayName: "Test Person", handles: ["1234567890"], handleIdentifier: "phoneNumbers")]

let csItem = CSSearchableItem(uniqueIdentifier: "uniqueId", domainIdentifier: "uniqueId", attributeSet: attributeSet)
```

The app then sets the listener flag to include summarization or prioritization (or both):

```swift
csItem.updateListenerOptions.insert(.summarization)
csItem.updateListenerOptions.insert(.priority)
```

And, lastly, the app adds the `CSSearchableItem` to Spotlight:

```swift
try await CSSearchableIndex.default().indexSearchableItems([csItem])
```

#### Select the Correct Attributes for Your Default App

In order for Apple Intelligence to summarize or prioritize a `CSSearchableItem`, set the following attributes, basedon the type of default app:

| Mail apps | Messaging apps | Audio Transcripts |
| --- | --- | --- |
| `authors` | `authors` |  |
| `contentCreationDate` | `contentCreationDate` | `contentCreationDate` |
| `domainIdentifier` | `domainIdentifier` | `domainIdentifier` |
| `htmlContentData` or `textContent` | `textContent` | `transcribedTextContent` |
| `uniqueIdentifier` | `uniqueIdentifier` | `uniqueIdentifier` |

#### Enable Summarization for Email and Message Threads

In iOS 18.4 and later and macOS 15.4 and later, Apple Intelligence supports optional summarization of email and message threads; these are separate capabilities that your app can adopt as needed.

To summarize multiple  in a conversation, adopt  [`INSearchForMessagesIntent`](https://developer.apple.com/documentation/Intents/INSearchForMessagesIntent) in your app. This class enables Apple Intelligence to fetch previously unread messages from a conversation. Provide a `domainIdentifier` when indexing these messages into Spotlight; Apple Intelligence uses the `domainIdentifier` to group messages into conversations.

To summarize multiple  in a conversation, provide implementations of [`AssistantEntity(schema:)`](https://developer.apple.com/documentation/AppIntents/AssistantEntity(schema:)) in your app for the [`account`](https://developer.apple.com/documentation/AppIntents/AssistantSchemas/MailEntity/account), [`mailbox`](https://developer.apple.com/documentation/AppIntents/AssistantSchemas/MailEntity/mailbox), and [`message`](https://developer.apple.com/documentation/AppIntents/AssistantSchemas/MailEntity/message) entities; these entities are part of the [`App Intents`](https://developer.apple.com/documentation/AppIntents) API, and enable Apple Intelligence to fetch previously unread emails from the conversation. As with message summarization, provide `domainIdentifier` when indexing emails into Spotlight. Apple Intelligences uses the `domainIdentifier` to group emails into conversations. The `domainIdentifier` needs to be globally unique across accounts and mailboxes.

With this information, the email thread summarization process proceeds as follows:

1. Your app provides email for Spotlight to index. Populate the `domainIdentifier` property with the identifier for the conversation to which the email belongs.
2. The system asks Spotlight for the email identifiers for all emails sharing the same `domainIdentifier`.
3. The system issues a query to your app with the email identifiers from the previous step. Respond with the emails matching the identifiers the system provides in the App Entity query.
4. Apple Intelligence combines the email from the initial indexing request and any additional email messages the system receives from your app as part of the follow-up request, and summarizes their content.
5. Your app receives a callback from Core Spotlight that contains the summarization result.

#### Ensure Your Searchable Item Is Eligible

Apple Intelligence only considers an item for summarization or prioritization when it meets the following criteria:

- The  [`contentType`](CSSearchableItemAttributeSet/contentType.md) contains one of the following UTI types: [`message`](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTType-swift.struct/message)  or [`emailMessage`](https://developer.apple.com/documentation/UniformTypeIdentifiers/UTType-swift.struct/emailMessage), or `public.voice-audio`.
- The item has either the `CSSearchableItemFlagNeedsSummary` or `CSSearchableItemFlagNeedsPriority` options set.
- The `contentCreationDate` is no more than 24 hours old.
- The content isn’t empty; this criteria applies specifically to `textContent` for messages, `textContent` or `htmlContentData` for mail, and `transcribedTextContent`for voice audio transcripts.
- For summarization, the `CSSearchableItemFlagNeedsSummary` option is set to `true` and the content is at least `200` characters in length.
- If you adopt [`INSearchForMessagesIntent`](https://developer.apple.com/documentation/Intents/INSearchForMessagesIntent) to support multiple message summarization, Apple Intelligence uses the combined content length of the unread message history, which must be at least 200 characters to be eligible for summarization.
- For prioritization, the `CSSearchableItemFlagNeedsPriority` option is set.
- Mail or messages need [`authors`](cssearchableitemattributeset/1621608-authors.md), and the system doesn’t summarize the same [`CSSearchableItem`](CSSearchableItem.md) twice, even if you present the item to Core Spotlight again.

> **Note**: Only mail or messages support priority classification, not audio transcripts. The `contentType` must conform to  one of the following types: `message` or `emailMessage`.

## See Also

- [Adding your app’s content to Spotlight indexes](adding-your-app-s-content-to-spotlight-indexes.md)
  Create a description for your app’s content and add it to a Spotlight index to make it searchable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/enable-apple-intelligence-summaries)*