# preferredIndicatorImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preferred image for indicators.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var preferredIndicatorImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * preferredIndicatorImage;
```

## See Also

### Managing the indicator images
- [func indicatorImage(forPage: Int) -> UIImage?](./indicatorimage%28forpage%29.md)
  Returns the override image for the indicator of the specified page.
- [func setIndicatorImage(UIImage?, forPage: Int)](./setindicatorimage%28_,forpage%29.md)
  Registers an override image for the indicator of the specified page.
- [var preferredCurrentPageIndicatorImage: UIImage?](./preferredcurrentpageindicatorimage.md)
  The preferred image for the current page indicator.
- [func currentPageIndicatorImage(forPage: Int) -> UIImage?](./currentpageindicatorimage%28forpage%29.md)
  Returns the override image for the current page indicator of the specified page.
- [func setCurrentPageIndicatorImage(UIImage?, forPage: Int)](./setcurrentpageindicatorimage%28_,forpage%29.md)
  Registers an override image for the current page indicator of the specified page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/preferredindicatorimage)*