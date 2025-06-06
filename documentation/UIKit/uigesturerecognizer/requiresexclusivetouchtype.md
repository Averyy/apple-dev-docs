# requiresExclusiveTouchType

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the gesture recognizer considers touches of different types simultaneously.

**Availability**:
- iOS 9.2+
- iPadOS 9.2+
- Mac Catalyst 13.1+
- tvOS 9.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var requiresExclusiveTouchType: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the gesture recognizer automatically ignores new touches whose type doesn’t match the type of the initial touch. When the value is [`false`](https://developer.apple.com/documentation/swift/false), the gesture recognizer receives all touches whose types are listed in the [`allowedTouchTypes`](uigesturerecognizer/allowedtouchtypes.md) property.

## See Also

- [var allowedPressTypes: [NSNumber]](uigesturerecognizer/allowedpresstypes.md)
  An array of press types used to distinguish the type of button press.
- [var allowedTouchTypes: [NSNumber]](uigesturerecognizer/allowedtouchtypes.md)
  An array of touch types used to distinguish type of touches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/requiresexclusivetouchtype)*