# UIHingeInteraction

**Framework**: UIKit  
**Kind**: class

An interaction for observing the hinge state associated with the view’s hierarchy.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
@MainActor
class UIHingeInteraction
```

#### Overview

Add a `UIHingeInteraction` to a view to receive hinge state updates. The interaction’s handler is called when the hinge state changes, or when the interaction moves between hierarchies. When the interaction moves out of a hierarchy that provides hinge updates, the update’s `hinge` is nil.

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

### Creating a hinge interaction
- [init(updateHandler: (UIHingeInteraction, UIHingeInteraction.Update) -> Void)](uihingeinteraction/init(updatehandler:).md)
  Creates a new hinge interaction with the provided update handler.
### Configuring the interaction
- [var isEnabled: Bool](uihingeinteraction/isenabled.md)
  Whether the interaction is enabled.
### Getting hinge updates
- [UIHingeInteraction.Update](uihingeinteraction/update.md)
  An update for a `UIHingeInteraction`

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [UIInteraction](uiinteraction.md)

## See Also

- [class UIDevice](uidevice.md)
  A representation of the current device.
- [class UIStatusBarManager](uistatusbarmanager.md)
  An object that describes the configuration of the status bar.
- [class UIHinge](uihinge.md)
  An object encapsulating the state of a single hinge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihingeinteraction)*