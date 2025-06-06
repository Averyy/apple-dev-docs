# allowedPressTypes

**Framework**: UIKit  
**Kind**: property

An array of press types used to distinguish the type of button press.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowedPressTypes: [NSNumber] { get set }
```

#### Discussion

This property is an array of `UIPressTypes` that activates the gesture recognizer to distinguish the type of button press. The default press type is [`UIPress.PressType.select`](uipress/presstype/select.md). When this property is set to an empty array, the gesture recognizer will respond to taps like a touch pad like surface. For a list of possible press types, see [`UIPress.PressType`](uipress/presstype.md) enumeration in the [`UIPress`](uipress.md).

## See Also

- [var allowedTouchTypes: [NSNumber]](uigesturerecognizer/allowedtouchtypes.md)
  An array of touch types used to distinguish type of touches.
- [var requiresExclusiveTouchType: Bool](uigesturerecognizer/requiresexclusivetouchtype.md)
  A Boolean value that indicates whether the gesture recognizer considers touches of different types simultaneously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/allowedpresstypes)*