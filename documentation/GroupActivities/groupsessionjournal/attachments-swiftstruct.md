# GroupSessionJournal.Attachments

**Framework**: Group Activities  
**Kind**: struct

An asynchronous sequence that contains one or more incoming attachment containers for you to process.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct Attachments
```

#### Overview

After a participant uploads a file or data, the system makes that content available on the [`GroupSessionJournal.Attachments`](groupsessionjournal/attachments-swift.struct.md) asynchronous sequence of each session participant. Configure an asynchronous task to monitor this sequence and process results when they arrive.

The following example shows you how to configure this task and use it to iterate over the available items. The `journal` variable contains a previously configured [`GroupSessionJournal`](groupsessionjournal.md) object.

```swift
let attachmentListener = Task {
   for await attachments in journal.attachments {
      for attachment in attachments {
         // Download and process each attachment.
      }
   }
}
```

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> GroupSessionJournal.Attachments.Iterator](groupsessionjournal/attachments-swift.struct/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [GroupSessionJournal.Attachments.Iterator](groupsessionjournal/attachments-swift.struct/iterator.md)
  The asynchronous iterator that produces a sequence of attachments.
- [GroupSessionJournal.Attachments.Element](groupsessionjournal/attachments-swift.struct/element.md)
  The type of element this asynchronous sequence produces.
### Type Aliases
- [GroupSessionJournal.Attachments.AsyncIterator](groupsessionjournal/attachments-swift.struct/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](groupsessionjournal/attachments-swift.struct/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var attachments: GroupSessionJournal.Attachments](groupsessionjournal/attachments-swift.property.md)
  The currently available attachments for you to download and incorporate into your app.
- [GroupSessionJournal.Attachment](groupsessionjournal/attachment.md)
  A container for the data you download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionjournal/attachments-swift.struct)*