# UIDragDropSession

**Framework**: UIKit  
**Kind**: protocol

The common interface for querying the state of both drag sessions and drop sessions.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIDragDropSession : NSObjectProtocol
```

## Topics

### Checking for drag items
- [func canLoadObjects(ofClass: any NSItemProviderReading.Type) -> Bool](uidragdropsession/canloadobjects(ofclass:).md)
  Returns a Boolean value that indicates whether at least one drag item in the session can create an instance of the specified class.
- [func hasItemsConforming(toTypeIdentifiers: [String]) -> Bool](uidragdropsession/hasitemsconforming(totypeidentifiers:).md)
  Returns a Boolean value that indicates whether at least one drag item in the session conforms to at least one of the specified UTIs.
- [var items: [UIDragItem]](uidragdropsession/items.md)
  An array of drag items in the drag session or drop session.
### Checking for drag and drop session restrictions
- [var allowsMoveOperation: Bool](uidragdropsession/allowsmoveoperation.md)
  A Boolean value that indicates whether the drag session permits moving drag items within the same app.
- [var isRestrictedToDraggingApplication: Bool](uidragdropsession/isrestrictedtodraggingapplication.md)
  A Boolean value that indicates whether the drag session is confined to the app that started the drag activity.
### Getting the location of a drag activity
- [func location(in: UIView) -> CGPoint](uidragdropsession/location(in:).md)
  Returns the geometrical location of the user’s drag activity within the specified view.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [UIDragSession](uidragsession.md)
- [UIDropSession](uidropsession.md)

## See Also

- [class UIDragItem](uidragitem.md)
  A representation of an underlying data item as a person drags it from one location to another.
- [protocol UIDragSession](uidragsession.md)
  The interface for configuring a drag session.
- [protocol UIDragAnimating](uidraganimating.md)
  The interface for providing custom animation alongside the system’s lift, drop, and cancellation animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragdropsession)*