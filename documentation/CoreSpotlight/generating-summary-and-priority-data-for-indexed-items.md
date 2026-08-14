# Generating summary and priority data for indexed items

**Framework**: Core Spotlight

Summarize mail, message, and audio transcripts or assess the priority of mail and messages using Spotlight and Apple Intelligence.

#### Overview

Apps that offer email, messaging, or audio transcription can use Spotlight and Apple Intelligence to generate additional information about that content. When you index your app’s email or message threads or your app’s audio transcripts, you can tell Spotlight to summarize that content with the help of Apple Intelligence. You can also ask it to classify the priority of SMS messages to help you assess their importance. Spotlight returns the results of these requests to you asynchronously so you can integrate them into your content.

Apps can use summary and priority information to augment the information they display in their interface. You might highlight SMS message threads with high priorities or elevate them to a more visible part of your interface. Similarly, you might present content summaries for email or message threads when space is constrained.

##### Ask Spotlight to Summarize or Classify Your Searchable Items

Spotlight returns summary and priority data only for the [`CSSearchableItem`](cssearchableitem.md) objects you designate. Generating summaries and classifying the priority of messages requires you to provide specific information in your app’s indexable content. Spotlight also requires you to enable the generation of summary and priority information on an item-by-item basis to minimize the impact on system performance and battery life. For example, you might enable this capability only on your app’s email content and not on your app’s other content.

When preparing your app’s indexable items, update the [`CSSearchableItemAttributeSet`](cssearchableitemattributeset.md) object for each item with the data that Apple Intelligence needs. The following table lists the attributes that you need to populate for the supported app types. For a mail app, you can use either the [`textContent`](cssearchableitemattributeset/textcontent.md) or [`htmlContentData`](cssearchableitemattributeset/htmlcontentdata.md) property, and don’t need to provide content for both.

| Attribute | Required in | Notes |
| --- | --- | --- |
| [`contentType`](cssearchableitemattributeset/contenttype.md) | All apps | This type must be [`message`](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/message), [`emailMessage`](https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/emailmessage), or `public.voice-audio` type. Apple Intelligence doesn’t operate on items with other types. |
| [`domainIdentifier`](cssearchableitemattributeset/domainidentifier.md) | All apps | Specify the identifier for the email, message, or audio conversation thread. Apple Intelligence uses this value to find items from the same thread. |
| [`contentCreationDate`](cssearchableitemattributeset/contentcreationdate.md) | All apps | Apple Intelligence doesn’t summarize items that are more than 24 hours old. |
| [`authors`](cssearchableitemattributeset/authors.md) | Mail and message apps | Apple Intelligence uses this field to distinguish among people in the conversation. |
| [`textContent`](cssearchableitemattributeset/textcontent.md) | Mail and message apps | For summarization, this property must contain at least 200 characters worth of content. In a mail app, use this property or the `htmlContentData` property to specify that content. |
| [`htmlContentData`](cssearchableitemattributeset/htmlcontentdata.md) | Mail apps | For summarization, this property must contain at least 200 characters worth of content. Use this property or the `textContent` property to specify that content. |
| [`transcribedTextContent`](cssearchableitemattributeset/transcribedtextcontent.md) | Audio transcript apps | For summarization, this property must contain at least 200 characters worth of content. |

After you populate the attributes and create your [`CSSearchableItem`](cssearchableitem.md) object, update its [`updateListenerOptions`](cssearchableitem/updatelisteneroptions-swift.property.md) property to tell Apple Intelligence what information to generate. The following example configures a searchable item for an app’s custom email type. Each instance of this type contains the text of the email plus information about the sender, recipients, and other content. The code uses this data to configure the indexable attributes and listener options of the item prior to indexing.

```swift
func indexEmail(email: MyEmail)  {
    let attributeSet = CSSearchableItemAttributeSet()
    attributeSet.contentType = UTType.emailMessage.identifier
    attributeSet.textContent = email.content
    attributeSet.domainIdentifier = email.domainID
    attributeSet.contentCreationDate = email.creationDate
    attributeSet.authors = [CSPerson(displayName: email.senderName, 
                                        handles: [email.senderEmail], 
                                        handleIdentifier: CNContactEmailAddressesKey)]

    let csItem = CSSearchableItem(uniqueIdentifier: email.id.uuidString, 
                    domainIdentifier: email.domainID, 
                    attributeSet: attributeSet)

    // Ask for summary and priority information.
    csItem.updateListenerOptions = [.priority, .summarization]

    itemsToIndex.append(csItem)   // Index this item with other emails.
}
```

When you submit an item for indexing, Apple Intelligence generates the requested summary or priority information if the item contains the required data. The system doesn’t report any errors if the required data isn’t present or the resources to generate the content aren’t available. For example, the system might forego generating summaries when battery power is limited.

##### Receive Item Updates in Your Indexing Delegate

When Apple Intelligence successfully generates summary or priority data for an item, Spotlight adds that data to the item’s attributes and notifies your app. Spotlight stores content summaries in the [`textContentSummary`](cssearchableitemattributeset/textcontentsummary.md), or [`transcribedTextContent`](cssearchableitemattributeset/transcribedtextcontent.md) property of the item’s attribute set. When classifying the priority of messages, Spotlight updates the [`isPriority`](cssearchableitemattributeset/ispriority.md) property of the item’s attributes.

When Spotlight updates the attributes of one of your items, it notifies the delegate of your app’s [`CSSearchableIndex`](cssearchableindex.md) if your app is running. Specifically, it calls the delegate’s [`searchableItemsDidUpdate(_:)`](cssearchableindexdelegate/searchableitemsdidupdate(_:).md) method, providing you with the updated items. Use the information in these items to update your app’s interface.

If your app isn’t running when an update occurs, Spotlight notifies your Spotlight delegate app extension if one is available. Implement the [`searchableItemsDidUpdate(_:)`](cssearchableindexdelegate/searchableitemsdidupdate(_:).md) method in your app extension’s [`CSIndexExtensionRequestHandler`](csindexextensionrequesthandler.md) object to receive the updates and take any appropriate actions. For example, you might use the content to update a widget or send notifications for high-priority content.

For information about how to implement a Spotlight delegate app extension, see [`Regenerating your app’s indexes on demand`](regenerating-your-app-s-indexes-on-demand.md).

## See Also

- [class CSSearchableIndex](cssearchableindex.md)
  An on-device index for your app’s searchable content.
- [protocol CSSearchableIndexDelegate](cssearchableindexdelegate.md)
  A protocol that defines methods a delegate object or app extension uses to handle communication from the on-device index.
- [class CSSearchableIndexDescription](cssearchableindexdescription.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/generating-summary-and-priority-data-for-indexed-items)*