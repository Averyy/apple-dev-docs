# allowedTouchTypes

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of touch types used to distinguish type of touches.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allowedTouchTypes: [NSNumber] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSNumber *> * allowedTouchTypes;
```

#### Discussion

This property is an array of touch types that recognizes whether the touch is direct or indirect. For a list of all possible touch types, see [`UITouch.TouchType`](../uitouch/touchtype.md) enumeration in [`UITouch`](../uitouch.md). The default value of this property contains all touch types.

## See Also

### Recognizing different gestures
- [var allowedPressTypes: [NSNumber]](./allowedpresstypes.md)
  An array of press types used to distinguish the type of button press.
- [var requiresExclusiveTouchType: Bool](./requiresexclusivetouchtype.md)
  A Boolean value that indicates whether the gesture recognizer considers touches of different types simultaneously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/allowedtouchtypes)*