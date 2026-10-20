# isToolbarHidden

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether the navigation controller’s built-in toolbar is visible.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var isToolbarHidden: Bool { get set }
```

```objc
@property (nonatomic, getter=isToolbarHidden) BOOL toolbarHidden;
```

#### Discussion

If this property is set to [`true`](../../Swift/true.md), the toolbar is not visible. The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Configuring custom toolbars
- [var toolbar: UIToolbar!](./toolbar.md)
  The custom toolbar associated with the navigation controller.
- [func setToolbarHidden(Bool, animated: Bool)](./settoolbarhidden%28_,animated%29.md)
  Changes the visibility of the navigation controller’s built-in toolbar.
- [class let hideShowBarDuration: CGFloat](./hideshowbarduration.md)
  A variable that specifies the duration when animating the navigation bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationcontroller/istoolbarhidden)*