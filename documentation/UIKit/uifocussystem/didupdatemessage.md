# UIFocusSystem.DidUpdateMessage

**Framework**: UIKit  
**Kind**: struct

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct DidUpdateMessage
```

## Topics

### Initializers
- [init(updateContext: UIFocusUpdateContext?, animationCoordinator: UIFocusAnimationCoordinator?, focusSystem: UIFocusSystem)](uifocussystem/didupdatemessage/init(updatecontext:animationcoordinator:focussystem:).md)
### Instance Properties
- [var animationCoordinator: UIFocusAnimationCoordinator?](uifocussystem/didupdatemessage/animationcoordinator.md)
- [var focusSystem: UIFocusSystem](uifocussystem/didupdatemessage/focussystem.md)
- [var updateContext: UIFocusUpdateContext?](uifocussystem/didupdatemessage/updatecontext.md)
### Type Methods
- [static func makeNotification(UIFocusSystem.DidUpdateMessage) -> Notification](uifocussystem/didupdatemessage/makenotification(_:).md)

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocussystem/didupdatemessage)*