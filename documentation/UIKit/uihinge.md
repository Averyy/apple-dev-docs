# UIHinge

**Framework**: UIKit  
**Kind**: class

An object encapsulating the state of a single hinge.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
@MainActor
class UIHinge
```

#### Overview

You observe hinge state by adding a `UIHingeInteraction` to a view and reading it from the update delivered to its handler.

```None
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

## Topics

### Getting the hinge state
- [var angle: CGFloat](uihinge/angle.md)
  The current angle of the hinge, in radians.
- [var status: UIHinge.Status](uihinge/status-swift.property.md)
  The current status of the hinge
- [UIHinge.Status](uihinge/status-swift.enum.md)
  The status of an individual hinge

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)

## See Also

- [class UIDevice](uidevice.md)
  A representation of the current device.
- [class UIStatusBarManager](uistatusbarmanager.md)
  An object that describes the configuration of the status bar.
- [class UIHingeInteraction](uihingeinteraction.md)
  An interaction for observing the hinge state associated with the view’s hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihinge)*