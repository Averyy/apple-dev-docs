# setTranslation(_:in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the translation value in the coordinate system of the specified view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setTranslation(_ translation: CGPoint, in view: UIView?)
```

```objc
- (void) setTranslation:(CGPoint) translation inView:(UIView *) view;
```

#### Discussion

Changing the translation value resets the velocity of the pan.

## Parameters

- `translation`: A point that identifies the new translation value.
- `view`: A view in whose coordinate system the translation is to occur.

## See Also

### Tracking the location and velocity of the gesture
- [func translation(in: UIView?) -> CGPoint](./translation%28in%29.md)
  Interprets the pan gesture in the coordinate system of the specified view.
- [func velocity(in: UIView?) -> CGPoint](./velocity%28in%29.md)
  Interprets the velocity of the pan gesture in the coordinate system of the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipangesturerecognizer/settranslation(_:in:))*