# presentationIndex(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the selected item to be reflected in the page indicator.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func presentationIndex(for pageViewController: UIPageViewController) -> Int
```

```objc
- (NSInteger) presentationIndexForPageViewController:(UIPageViewController *) pageViewController;
```

#### Return Value

The index of the selected item to be reflected in the page indicator.

## Parameters

- `pageViewController`: The page view controller.

## See Also

### Supporting a Page Indicator
- [func presentationCount(for: UIPageViewController) -> Int](./presentationcount%28for%29.md)
  Returns the number of items to be reflected in the page indicator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource/presentationindex(for:))*