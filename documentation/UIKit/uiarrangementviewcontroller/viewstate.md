# UIArrangementViewController.ViewState

**Framework**: UIKit  
**Kind**: struct

The state of a view within an arrangement.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
struct ViewState
```

## Topics

### Getting the state
- [var isHidden: Bool](uiarrangementviewcontroller/viewstate/ishidden.md)
  A Boolean value that indicates whether the view is hidden in the current arrangement.
- [var splitAxis: UIAxis](uiarrangementviewcontroller/viewstate/splitaxis.md)
  The axis of the current split for the view within the arrangement if it exists.
- [var zIndex: Int](uiarrangementviewcontroller/viewstate/zindex.md)
  The z-index of the view within the arrangement.

## See Also

- [func state(for: UIArrangementViewController.ViewPlacement) -> UIArrangementViewController.ViewState?](uiarrangementviewcontroller/state(for:).md)
  Returns the view state for a placement in the arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/viewstate)*