# preferredStatusBarUpdateAnimation

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The animation style to use when hiding or showing the status bar for this view controller.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency override dynamic var preferredStatusBarUpdateAnimation: UIStatusBarAnimation { get }
```

## See Also

### Configuring the status bar
- [var preferredStatusBarStyle: UIStatusBarStyle](./preferredstatusbarstyle.md)
  The preferred status bar style for the view controller.
- [var prefersStatusBarHidden: Bool](./prefersstatusbarhidden.md)
  A Boolean value that indicates whether the view controller prefers the status bar to be hidden or shown.
- [var childForStatusBarStyle: UIViewController?](./childforstatusbarstyle.md)
- [var childForStatusBarHidden: UIViewController?](./childforstatusbarhidden.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingcontroller/preferredstatusbarupdateanimation)*