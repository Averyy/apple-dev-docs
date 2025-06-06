# UIDragAnimating

**Framework**: UIKit  
**Kind**: protocol

The interface for providing custom animation alongside the system’s lift, drop, and cancellation animations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIDragAnimating : NSObjectProtocol
```

#### Overview

You can use a [`UIDragAnimating`](uidraganimating.md) object to animate your own changes to the preview displayed during system-provided drag and drop animations.

## Topics

### Adding animations
- [func addAnimations(() -> Void)](uidraganimating/addanimations(_:).md)
  Adds an animation block for modifying a view animation while it’s running.
- [func addCompletion((UIViewAnimatingPosition) -> Void)](uidraganimating/addcompletion(_:).md)
  Adds an animation completion block to run when a view animation has ended.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [UICollectionViewDropPlaceholderContext](uicollectionviewdropplaceholdercontext.md)
- [UITableViewDropPlaceholderContext](uitableviewdropplaceholdercontext.md)

## See Also

- [class UIDragItem](uidragitem.md)
  A representation of an underlying data item as a person drags it from one location to another.
- [protocol UIDragDropSession](uidragdropsession.md)
  The common interface for querying the state of both drag sessions and drop sessions.
- [protocol UIDragSession](uidragsession.md)
  The interface for configuring a drag session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraganimating)*