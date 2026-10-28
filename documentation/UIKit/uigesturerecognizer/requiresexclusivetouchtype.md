# requiresExclusiveTouchType

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the gesture recognizer considers touches of different types simultaneously.

**Availability**:
- iOS 9.2+
- iPadOS 9.2+
- Mac Catalyst 13.1+
- tvOS 9.1+
- visionOS 1.0+

## Declaration

```swift
var requiresExclusiveTouchType: Bool { get set }
```

```objc
@property (nonatomic) BOOL requiresExclusiveTouchType;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the gesture recognizer automatically ignores new touches whose type doesn’t match the type of the initial touch. When the value is [`false`](../../Swift/false.md), the gesture recognizer receives all touches whose types are listed in the [`allowedTouchTypes`](./allowedtouchtypes.md) property.

## See Also

### Recognizing different gestures
- [var allowedPressTypes: [NSNumber]](./allowedpresstypes.md)
  An array of press types used to distinguish the type of button press.
- [var allowedTouchTypes: [NSNumber]](./allowedtouchtypes.md)
  An array of touch types used to distinguish type of touches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/requiresexclusivetouchtype)*