# setBackIndicatorImage(_:transitionMaskImage:)

**Framework**: UIKit  
**Kind**: method

Sets the back button indicator image and its transition mask.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setBackIndicatorImage(_ backIndicatorImage: UIImage?, transitionMaskImage backIndicatorTransitionMaskImage: UIImage?)
```

#### Discussion

If you specify `nil` for either [`backIndicatorImage`](uinavigationbarappearance/backindicatorimage.md) or [`backIndicatorTransitionMaskImage`](uinavigationbarappearance/backindicatortransitionmaskimage.md), this method resets both images to their default values.

## Parameters

- `backIndicatorImage`: The image to display on the leading edge of the back button.
- `backIndicatorTransitionMaskImage`: The image for masking content flowing under the back indicator image during push and pop transitions.

## See Also

- [var backButtonAppearance: UIBarButtonItemAppearance](uinavigationbarappearance/backbuttonappearance.md)
  The appearance attributes for the back button.
- [var backIndicatorImage: UIImage](uinavigationbarappearance/backindicatorimage.md)
  The image to display on the leading edge of the back button.
- [var backIndicatorTransitionMaskImage: UIImage](uinavigationbarappearance/backindicatortransitionmaskimage.md)
  The image for masking content flowing under the back indicator image during push and pop transitions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbarappearance/setbackindicatorimage(_:transitionmaskimage:))*