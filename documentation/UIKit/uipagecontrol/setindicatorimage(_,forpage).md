# setIndicatorImage(_:forPage:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Registers an override image for the indicator of the specified page.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func setIndicatorImage(_ image: UIImage?, forPage page: Int)
```

```objc
- (void) setIndicatorImage:(UIImage *) image forPage:(NSInteger) page;
```

## Parameters

- `image`: The image to use instead of the preferred image. Use `nil` to reset the image to [`preferredIndicatorImage`](./preferredindicatorimage.md).
- `page`: The index of the page. A value that’s greater than or equal to `0` and less than [`numberOfPages`](./numberofpages.md).

## See Also

### Managing the indicator images
- [var preferredIndicatorImage: UIImage?](./preferredindicatorimage.md)
  The preferred image for indicators.
- [func indicatorImage(forPage: Int) -> UIImage?](./indicatorimage%28forpage%29.md)
  Returns the override image for the indicator of the specified page.
- [var preferredCurrentPageIndicatorImage: UIImage?](./preferredcurrentpageindicatorimage.md)
  The preferred image for the current page indicator.
- [func currentPageIndicatorImage(forPage: Int) -> UIImage?](./currentpageindicatorimage%28forpage%29.md)
  Returns the override image for the current page indicator of the specified page.
- [func setCurrentPageIndicatorImage(UIImage?, forPage: Int)](./setcurrentpageindicatorimage%28_,forpage%29.md)
  Registers an override image for the current page indicator of the specified page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/setindicatorimage(_:forpage:))*