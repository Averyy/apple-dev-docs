# translation(in:)

**Framework**: UIKit  
**Kind**: method

Interprets the pan gesture in the coordinate system of the specified view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func translation(in view: UIView?) -> CGPoint
```

## Mentions

- [Handling pan gestures](handling-pan-gestures.md)

#### Return Value

A point identifying the new location of a view in the coordinate system of its designated superview.

#### Discussion

The x and y values report the total translation over time. They aren’t delta values from the last time that the translation was reported. Apply the translation value to the state of the view when the gesture is first recognized — don’t concatenate the value each time the handler is called.

## Parameters

- `view`: The view in whose coordinate system the translation of the pan gesture should be computed. If you want to adjust a view’s location to keep it under the user’s finger, request the translation in that view’s superview’s coordinate system.

## See Also

- [func setTranslation(CGPoint, in: UIView?)](uipangesturerecognizer/settranslation(_:in:).md)
  Sets the translation value in the coordinate system of the specified view.
- [func velocity(in: UIView?) -> CGPoint](uipangesturerecognizer/velocity(in:).md)
  Interprets the velocity of the pan gesture in the coordinate system of the specified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipangesturerecognizer/translation(in:))*