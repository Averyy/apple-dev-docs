# hoverEffect(_:)

**Framework**: FamilyControls  
**Kind**: method

Applies a hover effect to this view.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func hoverEffect(_ effect: HoverEffect = .automatic) -> some View
```

#### Return Value

A new view that applies a hover effect to `self`.

#### Discussion

By default, `HoverEffect/automatic` is used. You can control the behavior of the automatic effect with the `View/defaultHoverEffect(_:)` modifier.

## Parameters

- `effect`: The effect to apply to this view.
- `isEnabled`: Whether the effect is enabled or not.

## See Also

- [func onHover(perform: (Bool) -> Void) -> some View](familyactivitypicker/onhover(perform:).md)
  Adds an action to perform when the user moves the pointer over or away from the view’s frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/hovereffect(_:))*