# backIndicatorImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The image shown beside the Back button.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var backIndicatorImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * backIndicatorImage;
```

#### Discussion

If you want to customize the back-indicator image, you must also set [`backIndicatorTransitionMaskImage`](./backindicatortransitionmaskimage.md).

## See Also

### Configuring the Back button
- [var backIndicatorTransitionMaskImage: UIImage?](./backindicatortransitionmaskimage.md)
  The image used as a mask for content during push and pop transitions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationbar/backindicatorimage)*