# setBackIndicatorImage(_:transitionMaskImage:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the back button indicator image and its transition mask.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setBackIndicatorImage(_ backIndicatorImage: UIImage?, transitionMaskImage backIndicatorTransitionMaskImage: UIImage?)
```

```objc
- (void) setBackIndicatorImage:(UIImage *) backIndicatorImage transitionMaskImage:(UIImage *) backIndicatorTransitionMaskImage;
```

## Discussion

If you specify `nil` for either [`backIndicatorImage`](./backindicatorimage.md) or [`backIndicatorTransitionMaskImage`](./backindicatortransitionmaskimage.md), this method resets both images to their default values.

## Parameters

- `backIndicatorImage`: The image to display on the leading edge of the back button.
- `backIndicatorTransitionMaskImage`: The image for masking content flowing under the back indicator image during push and pop transitions.

## See Also

### Configuring the Back button
- [var backButtonAppearance: UIBarButtonItemAppearance](./backbuttonappearance.md)
  The appearance attributes for the back button.
- [var backIndicatorImage: UIImage](./backindicatorimage.md)
  The image to display on the leading edge of the back button.
- [var backIndicatorTransitionMaskImage: UIImage](./backindicatortransitionmaskimage.md)
  The image for masking content flowing under the back indicator image during push and pop transitions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbarappearance/setbackindicatorimage(_:transitionmaskimage:))*