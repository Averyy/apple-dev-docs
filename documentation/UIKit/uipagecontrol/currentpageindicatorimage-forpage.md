# currentPageIndicatorImage(forPage:)

**Framework**: UIKit  
**Kind**: method

Returns the override image for the current page indicator of the specified page.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func currentPageIndicatorImage(forPage page: Int) -> UIImage?
```

#### Return Value

The override image, or `nil` if you haven’t overidden the image for the specified page number.

## Parameters

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
- [func setCurrentPageIndicatorImage(UIImage?, forPage: Int)](uipagecontrol/setcurrentpageindicatorimage(_:forpage:).md)
  Registers an override image for the current page indicator of the specified page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipagecontrol/currentpageindicatorimage(forpage:))*