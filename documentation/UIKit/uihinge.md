# UIHinge

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object encapsulating the state of a single hinge.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
@MainActor
class UIHinge
```

```objc
@interface UIHinge : NSObject
```

## Overview

You observe hinge state by adding a `UIHingeInteraction` to a view and reading it from the update delivered to its handler.

```
override func viewDidLoad() {
    super.viewDidLoad()

    let interaction = UIHingeInteraction { [weak self] _, update in
        guard let self else { return }
        // A nil `hinge` indicates the interaction has left a
        // hierarchy that provides hinge updates.
        guard let hinge = update.hinge else {
            handleHingeUnavailable()
            return
        }

        updateAngleDisplay(with: hinge.angle)
        updateStatusDisplay(with: hinge.status)
    }

    view.addInteraction(interaction)
}
```

In the example above, the current angle and status of the hinge are displayed as the user interacts with the hinge.

> ❗ **Important**: Use hinge updates when your app treats the hinge as input, such as driving an animation that responds to granular hinge angle changes, controlling a game, or showing the current angle. Hinge updates arrive while the hinge is moving, at a pace the system sets.
>
> Don’t use hinge updates for layout. To adapt your layout to the fold, use [`UIArrangementViewController`](./uiarrangementviewcontroller.md) or [`UIView.ReservedRegion`](./uiview/reservedregion.md) instead. Reserved region updates arrive during a layout pass, which might be animated.

## Topics

### Getting the hinge state
- [var angle: CGFloat](./uihinge/angle.md)
  The current angle of the hinge, in radians.
- [var status: UIHinge.Status](./uihinge/status-swift.property.md)
  The current status of the hinge
- [UIHinge.Status](./uihinge/status-swift.enum.md)
  The status of an individual hinge

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Device environment
- [class UIDevice](./uidevice.md)
  A representation of the current device.
- [class UIStatusBarManager](./uistatusbarmanager.md)
  An object that describes the configuration of the status bar.
- [class UIHingeInteraction](./uihingeinteraction.md)
  An interaction for observing the hinge state associated with the view’s hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihinge)*