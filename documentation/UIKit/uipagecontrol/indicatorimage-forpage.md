# indicatorImage(forPage:)

**Framework**: UIKit  
**Kind**: method

Returns the override image for the indicator of the specified page.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func indicatorImage(forPage page: Int) -> UIImage?
```

#### Return Value

The override image, or `nil` if you haven’t overidden the image for the specified page number.

## Parameters

- `page`: The index of the page. A value that’s greater than or equal to   and less than  .

## See Also

- [var preferredIndicatorImage: UIImage?](uipagecontrol/preferredindicatorimage.md)
  The preferred image for indicators.
- [func setIndicatorImage(UIImage?, forPage: Int)](uipagecontrol/setindicatorimage(_:forpage:).md)
  Registers an override image for the indicator of the specified page.
- [var preferredCurrentPageIndicatorImage: UIImage?](uipagecontrol/preferredcurrentpageindicatorimage.md)
  The preferred image for the current page indicator.
- [func currentPageIndicatorImage(forPage: Int) -> UIImage?](uipagecontrol/currentpageindicatorimage(forpage:).md)
  Returns the override image for the current page indicator of the specified page.
- [func setCurrentPageIndicatorImage(UIImage?, forPage: Int)](uipagecontrol/setcurrentpageindicatorimage(_:forpage:).md)
  Registers an override image for the current page indicator of the specified page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/indicatorimage(forpage:))*