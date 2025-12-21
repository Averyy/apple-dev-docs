# Making onscreen content available to Siri and Apple Intelligence

**Framework**: App Intents

Enable Siri and Apple Intelligence to respond to a person’s questions and action requests for your app’s onscreen content.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+
- Xcode 16.2+

#### Overview

When a person asks a question about onscreen content or wants to perform an action on it, Siri and Apple Intelligence will be able to retrieve the content to respond to the question and perform the action. If the user explicitly requests it, Siri and Apple Intelligence will be able to send content to supported third-party services. For example, someone could view a website and use Siri to provide a summary by saying or typing a phrase like “Hey Siri, what’s this document about?”

> **Note**: Siri’s personal context understanding, onscreen awareness, and in-app actions are in development and will be available with a future software update.

##### Create an App Entity and Associate It with the User Activity Object

To integrate your app’s onscreen content with current and upcoming personal intelligence features of Siri and Apple Intelligence, explicitly provide the onscreen content using the App Intents framework. Describe the content with an [`AppEntity`](appentity.md) — you might be able to reuse existing app entity code. Then, tell the system about the content when it becomes visible:

1. Create an app entity identifier using [`EntityIdentifier`](entityidentifier.md) .
2. Associate the identifier with the current [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) by setting the activity’s [`appEntityIdentifier`](https://developer.apple.com/documentation/Foundation/NSUserActivity/appEntityIdentifier) property.

To remove the association between the user activity and your app entity, set the user activity’s `appEntityIdentifier` property to `nil`.

The following code snippet from the [`Making your app’s functionality available to Siri`](making-your-app-s-functionality-available-to-siri.md) sample code project shows how a photo-viewing app might provide a photo to Siri and Apple Intelligence by creating an app entity identifier for the `asset` app entity that represents a photo, and associating it with the user activity:

```swift
 MediaView(
    image: image,
    duration: asset.duration,
    isFavorite: asset.isFavorite,
    proxy: proxy
)
.userActivity(
    "com.example.apple-samplecode.AssistantSchemasExample.ViewingPhoto",
    element: asset.entity
) { asset, activity in
    activity.title = "Viewing a photo"
    activity.appEntityIdentifier = EntityIdentifier(for: asset)
}
```

##### Make the App Entity Transferable

Associating an [`AppEntity`](appentity.md) with the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) provides Siri and Apple Intelligence with your app’s onscreen content to offer personalized intelligence assistance. To go one step further and enable Siri and Apple Intelligence to further process the provided onscreen content and respond to a person’s explicit request to send the content as an attachment to other services, including third parties:

1. Update your app entity to conform to the [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) protocol.
2. In your `Transferable` implementation, provide image, PDF, rich text, or plain text representations. To increase compatibility with third-party services, provide several representations that best fit your content. For example, an email client might represent an email as rich text, plain text, and a PDF. For more on adopting `Transferable`, refer to [`CoreTransferable`](https://developer.apple.comhttp://developer.apple.com/documentation/coretransferable).

##### Provide Additional Context to the System with an Assistant Schema

To enable Siri and Apple Intelligence to further process the provided onscreen content and provide a better response in iOS 18, make sure that the app entity that you associate with an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) conforms to one of the assistant schemas in the list below.

> **Note**: The listed requests below are examples and not exhaustive. Actual functionality depends on factors such as the features provided by Siri and Apple Intelligence, the functionality offered by third-party services, or the phrase a person uses.

| Domain | Schema | Swift macro | Example request |
| --- | --- | --- | --- |
| Browser | [`tab`](assistantschemas/browserentity/tab.md) | `@AppEntity(schema: .browser.tab)` | A person might ask Siri questions about the web page. |
| Document reader | [`document`](assistantschemas/readerentity/document.md) | `@AppEntity(schema: .reader.document)` | A person might ask Siri to explain the conclusion of a document. |
| File management | [`file`](assistantschemas/filesentity/file.md) | `@AppEntity(schema: .files.file)` | A person might ask Siri to summarize file content. |
| Mail | [`message`](assistantschemas/mailentity/message.md) | `@AppEntity(schema: .mail.message) ` | A person might ask Siri to provide a summary. |
| Photos | [`asset`](assistantschemas/photosentity/asset.md) | `@AppEntity(schema: .photos.asset)` | A person might ask Siri about things to do with an object in a photo. |
| Presentations | [`document`](assistantschemas/presentationentity/document.md) | `@AppEntity(schema: .presentation.document)` | A person might ask Siri to suggest a creative title for a presentation. |
| Spreadsheets | [`document`](assistantschemas/spreadsheetentity/document.md) | `@AppEntity(schema: .spreadsheet.document)` | A person might ask Siri to give an overview of the spreadsheet’s data. |
| Word processor | [`document`](assistantschemas/wordprocessorentity/document.md) | `@AppEntity(schema: .wordProcessor.document)` | A person might ask Siri to suggest additional content for a text document. |

## Topics

### System protocols
- [protocol AppEntityAnnotatable](appentityannotatable.md)
  A protocol that framework types adopt to enable you to provide content to system experiences.

## See Also

- [Integrating actions with Siri and Apple Intelligence](integrating-actions-with-siri-and-apple-intelligence.md)
  Create app intents, entities, and enumerations that conform to assistant schemas to tap into the enhanced action capabilities of Siri and Apple Intelligence.
- [App intent domains](app-intent-domains.md)
  Make your app’s actions and content available to Siri and Apple Intelligence with assistant schemas.
- [Making your app’s functionality available to Siri](making-your-app-s-functionality-available-to-siri.md)
  Add app intent schemas to your app so Siri can complete requests, and integrate your app with Apple Intelligence, Spotlight, and other system experiences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/making-onscreen-content-available-to-siri-and-apple-intelligence)*