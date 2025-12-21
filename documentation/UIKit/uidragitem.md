# UIDragItem

**Framework**: UIKit  
**Kind**: class

A representation of an underlying data item as a person drags it from one location to another.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDragItem
```

## Mentions

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md)
- [Supporting drag and drop in table views](supporting-drag-and-drop-in-table-views.md)

## Topics

### Initializing a drag item
- [init(itemProvider: NSItemProvider)](uidragitem/init(itemprovider:).md)
  Initializes a new drag item with a specified item provider.
### Accessing the drag item’s data
- [var itemProvider: NSItemProvider](uidragitem/itemprovider.md)
  The item provider associated with the drag item.
- [var localObject: Any?](uidragitem/localobject.md)
  A custom object associated with the drag item.
### Changing the drag item preview
- [var previewProvider: (() -> UIDragPreview?)?](uidragitem/previewprovider.md)
  A visual preview of the drag item, displayed while the user drags the item across the screen.
- [func setNeedsDropPreviewUpdate()](uidragitem/setneedsdroppreviewupdate.md)
  Notifies the operating system that an updated drop preview is available for the item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol UIDragDropSession](uidragdropsession.md)
  The common interface for querying the state of both drag sessions and drop sessions.
- [protocol UIDragSession](uidragsession.md)
  The interface for configuring a drag session.
- [protocol UIDragAnimating](uidraganimating.md)
  The interface for providing custom animation alongside the system’s lift, drop, and cancellation animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragitem)*