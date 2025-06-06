# allowedTouchTypes

**Framework**: UIKit  
**Kind**: property

An array of touch types used to distinguish type of touches.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowedTouchTypes: [NSNumber] { get set }
```

#### Discussion

This property is an array of touch types that recognizes whether the touch is direct or indirect. For a list of all possible touch types, see [`UITouch.TouchType`](uitouch/touchtype.md) enumeration in [`UITouch`](uitouch.md). The default value of this property contains all touch types.

## See Also

- [var allowedPressTypes: [NSNumber]](uigesturerecognizer/allowedpresstypes.md)
  An array of press types used to distinguish the type of button press.
- [var requiresExclusiveTouchType: Bool](uigesturerecognizer/requiresexclusivetouchtype.md)
  A Boolean value that indicates whether the gesture recognizer considers touches of different types simultaneously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/allowedtouchtypes)*