# backgroundViewClass

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The class to use for displaying the popover background content.

**Availability**:
- iOS 5.0+ - Deprecated in 9.0
- iPadOS 5.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

> **Deprecated**: UIPopoverController is deprecated. Popovers are now implemented as UIViewController presentations. Use a modal presentation style of UIModalPresentationPopover and UIPopoverPresentationController.

## Declaration

```swift
var backgroundViewClass: AnyClass? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) Class popoverBackgroundViewClass;
```

#### Discussion

The default value of this property is `nil`, which indicates that the popover controller should use the default popover appearance. Setting this property to a value other than `nil` causes the popover controller to use the specified class to draw the popover’s background content. The class you specify must be a subclass of [`UIPopoverBackgroundView`](../uipopoverbackgroundview.md).

## See Also

### Customizing the popover appearance
- [var layoutMargins: UIEdgeInsets](./layoutmargins.md)
  The margins that define the portion of the screen in which it is permissible to display the popover.
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  The color of the popover’s backdrop view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/backgroundviewclass)*