# dataSource

**Framework**: UIKit  
**Kind**: property

The object that provides view controllers.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var dataSource: (any UIPageViewControllerDataSource)? { get set }
```

#### Discussion

Methods of the data source are called in response to gesture-based navigation. If the value of this property is `nil`, then gesture-based navigation is disabled.

## See Also

- [protocol UIPageViewControllerDataSource](uipageviewcontrollerdatasource.md)
  The [`UIPageViewControllerDataSource`](uipageviewcontrollerdatasource.md) protocol is adopted by an object that provides view controllers to the page view controller on an as-needed basis, in response to navigation gestures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipageviewcontroller/datasource)*