# UIArrangementViewController.ViewState

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

The state of a view within an arrangement.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- tvOS 27.1+
- visionOS 27.1+

## Declaration

```swift
struct ViewState
```

## Topics

### Getting the state
- [var isHidden: Bool](./viewstate/ishidden.md)
  A Boolean value that indicates whether the view is hidden in the current arrangement.
- [var splitAxis: UIAxis](./viewstate/splitaxis.md)
  The axis of the current split for the view within the arrangement if it exists.
- [var zIndex: Int](./viewstate/zindex.md)
  The z-index of the view within the arrangement.

## See Also

### Getting view state
- [func state(for: UIArrangementViewController.ViewPlacement) -> UIArrangementViewController.ViewState?](./state%28for%29.md)
  Returns the view state for a placement in the arrangement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller/viewstate)*