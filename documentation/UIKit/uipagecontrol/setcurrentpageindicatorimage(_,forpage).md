# setCurrentPageIndicatorImage(_:forPage:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Registers an override image for the current page indicator of the specified page.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setCurrentPageIndicatorImage(_ image: UIImage?, forPage page: Int)
```

```objc
- (void) setCurrentPageIndicatorImage:(UIImage *) image forPage:(NSInteger) page;
```

## Parameters

- `image`: The image to use instead of the preferred image. Use `nil` to reset the image to [`preferredCurrentPageIndicatorImage`](./preferredcurrentpageindicatorimage.md).
- `page`: The index of the page. A value that’s greater than or equal to `0` and less than [`numberOfPages`](./numberofpages.md).

## See Also

### Managing the indicator images
- [var preferredIndicatorImage: UIImage?](./preferredindicatorimage.md)
  The preferred image for indicators.
- [func indicatorImage(forPage: Int) -> UIImage?](./indicatorimage%28forpage%29.md)
  Returns the override image for the indicator of the specified page.
- [func setIndicatorImage(UIImage?, forPage: Int)](./setindicatorimage%28_,forpage%29.md)
  Registers an override image for the indicator of the specified page.
- [var preferredCurrentPageIndicatorImage: UIImage?](./preferredcurrentpageindicatorimage.md)
  The preferred image for the current page indicator.
- [func currentPageIndicatorImage(forPage: Int) -> UIImage?](./currentpageindicatorimage%28forpage%29.md)
  Returns the override image for the current page indicator of the specified page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/setcurrentpageindicatorimage(_:forpage:))*