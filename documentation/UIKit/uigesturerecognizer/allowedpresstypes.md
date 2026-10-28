# allowedPressTypes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of press types used to distinguish the type of button press.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allowedPressTypes: [NSNumber] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSNumber *> * allowedPressTypes;
```

## Discussion

This property is an array of `UIPressTypes` that activates the gesture recognizer to distinguish the type of button press. The default press type is [`UIPress.PressType.select`](../uipress/presstype/select.md). When this property is set to an empty array, the gesture recognizer will respond to taps like a touch pad like surface. For a list of possible press types, see [`UIPress.PressType`](../uipress/presstype.md) enumeration in the [`UIPress`](../uipress.md).

## See Also

### Recognizing different gestures
- [var allowedTouchTypes: [NSNumber]](./allowedtouchtypes.md)
  An array of touch types used to distinguish type of touches.
- [var requiresExclusiveTouchType: Bool](./requiresexclusivetouchtype.md)
  A Boolean value that indicates whether the gesture recognizer considers touches of different types simultaneously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/allowedpresstypes)*