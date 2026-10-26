# CSSearchableItem.UpdateListenerOptions

**Framework**: Core Spotlight  
**Kind**: struct  
**Role**: Structure

The options to generate summarization or prioritization information for a searchable item.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct UpdateListenerOptions
```

```c
enum CSSearchableItemUpdateListenerOptions : NSUInteger;
```

#### Overview

When you configure a [`CSSearchableItem`](../cssearchableitem.md) with a listener option, Core Spotlight conveys your request to Apple Intelligence, which is responsible for generating the information. When the information becomes available, Core Spotlight updates the item and reports the change to the [`searchableItemsDidUpdate(_:)`](../cssearchableindexdelegate/searchableitemsdidupdate%28_%29.md) method of your index’s delegate. If your app isn’t running but has a CoreSpotlight delegate app extension, the system calls your app extension’s implementation of this method instead.

## Topics

### Getting the listener options structure
- [init(rawValue: UInt)](./updatelisteneroptions-swift.struct/init%28rawvalue%29.md)
  An unsigned integer that describes the listener options.
### Getting the listener options attributes
- [static var summarization: CSSearchableItem.UpdateListenerOptions](./updatelisteneroptions-swift.struct/summarization.md)
  An option to summarize the contents of your searchable item. Specify this option only for items that contain emails, messages, or audio transcripts.
- [static var priority: CSSearchableItem.UpdateListenerOptions](./updatelisteneroptions-swift.struct/priority.md)
  An option to classify the priority of SMS message content. Specify this option only if your item contains messages.
### Enumeration Cases
- [CSSearchableItemUpdateListenerOptionDefault](../cssearchableitemupdatelisteneroptions/cssearchableitemupdatelisteneroptiondefault.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Setting attributes on a searchable item
- [var uniqueIdentifier: String](./uniqueidentifier.md)
  The value that uniquely identifies the searchable item within your app.
- [var domainIdentifier: String?](./domainidentifier.md)
  An optional identifier that represents the domain or owner of the item.
- [var attributeSet: CSSearchableItemAttributeSet](./attributeset.md)
  The set of attributes that contain metadata associated with the item in a [`CSSearchableItemAttributeSet`](../cssearchableitemattributeset.md) object.
- [var expirationDate: Date!](./expirationdate.md)
  The date after which the searchable item should no longer exist.
- [var isUpdate: Bool](./isupdate.md)
  A Boolean value that indicates whether to treat the item as an update instead of a new item.
- [var updateListenerOptions: CSSearchableItem.UpdateListenerOptions](./updatelisteneroptions-swift.property.md)
  The types of notifications to request from Spotlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/updatelisteneroptions-swift.struct)*