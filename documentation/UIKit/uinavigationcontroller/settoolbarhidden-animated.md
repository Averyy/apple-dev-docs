# setToolbarHidden(_:animated:)

**Framework**: UIKit  
**Kind**: method

Changes the visibility of the navigation controller’s built-in toolbar.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setToolbarHidden(_ hidden: Bool, animated: Bool)
```

#### Discussion

You can use this method to animate changes to the visibility of the built-in toolbar.

Calling this method with the `animated` parameter set to [`false`](https://developer.apple.com/documentation/swift/false) is equivalent to setting the value of the [`isToolbarHidden`](uinavigationcontroller/istoolbarhidden.md) property directly. The toolbar simply appears or disappears depending on the value in the `hidden` parameter.

## Parameters

- `hidden`: Specify   to hide the toolbar or   to show it.
- `animated`: Specify   if you want the toolbar to be animated on or off the screen.

## See Also

- [var toolbar: UIToolbar!](uinavigationcontroller/toolbar.md)
  The custom toolbar associated with the navigation controller.
- [var isToolbarHidden: Bool](uinavigationcontroller/istoolbarhidden.md)
  A Boolean indicating whether the navigation controller’s built-in toolbar is visible.
- [class let hideShowBarDuration: CGFloat](uinavigationcontroller/hideshowbarduration.md)
  A variable that specifies the duration when animating the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/settoolbarhidden(_:animated:))*