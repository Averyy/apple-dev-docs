# velocity(in:)

**Framework**: UIKit  
**Kind**: method

Interprets the velocity of the pan gesture in the coordinate system of the specified view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func velocity(in view: UIView?) -> CGPoint
```

#### Return Value

The velocity of the pan gesture, which is expressed in points per second. The velocity is broken into horizontal and vertical components.

## Parameters

- `view`: The view in whose coordinate system the velocity of the pan gesture is computed.

## See Also

- [func translation(in: UIView?) -> CGPoint](uipangesturerecognizer/translation(in:).md)
  Interprets the pan gesture in the coordinate system of the specified view.
- [func setTranslation(CGPoint, in: UIView?)](uipangesturerecognizer/settranslation(_:in:).md)
  Sets the translation value in the coordinate system of the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipangesturerecognizer/velocity(in:))*