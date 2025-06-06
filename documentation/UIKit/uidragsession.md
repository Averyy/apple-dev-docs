# UIDragSession

**Framework**: UIKit  
**Kind**: protocol

The interface for configuring a drag session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIDragSession : UIDragDropSession
```

## Mentions

- [Making a view into a drag source](making-a-view-into-a-drag-source.md)

## Topics

### Accessing local information
- [var localContext: Any?](uidragsession/localcontext.md)
  The optional custom data that you attach to a drag session, visible only to the app in which the drag activity begins.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIDragDropSession](uidragdropsession.md)

## See Also

- [class UIDragItem](uidragitem.md)
  A representation of an underlying data item as a person drags it from one location to another.
- [protocol UIDragDropSession](uidragdropsession.md)
  The common interface for querying the state of both drag sessions and drop sessions.
- [protocol UIDragAnimating](uidraganimating.md)
  The interface for providing custom animation alongside the system’s lift, drop, and cancellation animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragsession)*