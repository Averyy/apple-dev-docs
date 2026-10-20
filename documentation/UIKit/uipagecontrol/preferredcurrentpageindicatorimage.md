# preferredCurrentPageIndicatorImage

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preferred image for the current page indicator.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var preferredCurrentPageIndicatorImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * preferredCurrentPageIndicatorImage;
```

#### Discussion

When `nil`, the page control uses [`preferredIndicatorImage`](./preferredindicatorimage.md) as its current page indicator.

The default value of this property is `nil`.

## See Also

### Managing the indicator images
- [var preferredIndicatorImage: UIImage?](./preferredindicatorimage.md)
  The preferred image for indicators.
- [func indicatorImage(forPage: Int) -> UIImage?](./indicatorimage%28forpage%29.md)
  Returns the override image for the indicator of the specified page.
- [func setIndicatorImage(UIImage?, forPage: Int)](./setindicatorimage%28_,forpage%29.md)
  Registers an override image for the indicator of the specified page.
- [func currentPageIndicatorImage(forPage: Int) -> UIImage?](./currentpageindicatorimage%28forpage%29.md)
  Returns the override image for the current page indicator of the specified page.
- [func setCurrentPageIndicatorImage(UIImage?, forPage: Int)](./setcurrentpageindicatorimage%28_,forpage%29.md)
  Registers an override image for the current page indicator of the specified page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/preferredcurrentpageindicatorimage)*