# setCurrentPageIndicatorImage(_:forPage:)

**Framework**: UIKit  
**Kind**: method

Registers an override image for the current page indicator of the specified page.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setCurrentPageIndicatorImage(_ image: UIImage?, forPage page: Int)
```

## Parameters

- `image`: The image to use instead of the preferred image. Use   to reset the image to  .
- `page`: The index of the page. A value that’s greater than or equal to   and less than  .

## See Also

- [var preferredIndicatorImage: UIImage?](uipagecontrol/preferredindicatorimage.md)
  The preferred image for indicators.
- [func indicatorImage(forPage: Int) -> UIImage?](uipagecontrol/indicatorimage(forpage:).md)
  Returns the override image for the indicator of the specified page.
- [func setIndicatorImage(UIImage?, forPage: Int)](uipagecontrol/setindicatorimage(_:forpage:).md)
  Registers an override image for the indicator of the specified page.
- [var preferredCurrentPageIndicatorImage: UIImage?](uipagecontrol/preferredcurrentpageindicatorimage.md)
  The preferred image for the current page indicator.
- [func currentPageIndicatorImage(forPage: Int) -> UIImage?](uipagecontrol/currentpageindicatorimage(forpage:).md)
  Returns the override image for the current page indicator of the specified page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/setcurrentpageindicatorimage(_:forpage:))*