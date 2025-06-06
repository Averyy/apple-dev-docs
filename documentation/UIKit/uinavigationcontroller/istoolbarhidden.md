# isToolbarHidden

**Framework**: UIKit  
**Kind**: property

A Boolean indicating whether the navigation controller’s built-in toolbar is visible.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isToolbarHidden: Bool { get set }
```

#### Discussion

If this property is set to [`true`](https://developer.apple.com/documentation/swift/true), the toolbar is not visible. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var toolbar: UIToolbar!](uinavigationcontroller/toolbar.md)
  The custom toolbar associated with the navigation controller.
- [func setToolbarHidden(Bool, animated: Bool)](uinavigationcontroller/settoolbarhidden(_:animated:).md)
  Changes the visibility of the navigation controller’s built-in toolbar.
- [class let hideShowBarDuration: CGFloat](uinavigationcontroller/hideshowbarduration.md)
  A variable that specifies the duration when animating the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/istoolbarhidden)*