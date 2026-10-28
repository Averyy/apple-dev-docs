# backIndicatorTransitionMaskImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The image used as a mask for content during push and pop transitions.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var backIndicatorTransitionMaskImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * backIndicatorTransitionMaskImage;
```

## Discussion

If you want to customize the back indicator image, you must also set [`backIndicatorImage`](./backindicatorimage.md).

## See Also

### Configuring the Back button
- [var backIndicatorImage: UIImage?](./backindicatorimage.md)
  The image shown beside the Back button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/backindicatortransitionmaskimage)*