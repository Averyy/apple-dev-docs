# backButtonAppearance

**Framework**: UIKit  
**Kind**: property

The appearance attributes for the back button.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var backButtonAppearance: UIBarButtonItemAppearance { get set }
```

#### Discussion

If you don’t change the value of this property, the navigation bar applies the attributes from the [`buttonAppearance`](uinavigationbarappearance/buttonappearance.md) property.

## See Also

- [var backIndicatorImage: UIImage](uinavigationbarappearance/backindicatorimage.md)
  The image to display on the leading edge of the back button.
- [var backIndicatorTransitionMaskImage: UIImage](uinavigationbarappearance/backindicatortransitionmaskimage.md)
  The image for masking content flowing under the back indicator image during push and pop transitions.
- [func setBackIndicatorImage(UIImage?, transitionMaskImage: UIImage?)](uinavigationbarappearance/setbackindicatorimage(_:transitionmaskimage:).md)
  Sets the back button indicator image and its transition mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbarappearance/backbuttonappearance)*