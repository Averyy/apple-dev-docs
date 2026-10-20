# backgroundColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The color of the popover’s backdrop view.

**Availability**:
- iOS 7.0+ - Deprecated in 9.0
- iPadOS 7.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

> **Deprecated**: UIPopoverController is deprecated. Popovers are now implemented as UIViewController presentations. Use a modal presentation style of UIModalPresentationPopover and UIPopoverPresentationController.

## Declaration

```swift
@NSCopying
var backgroundColor: UIColor? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIColor * backgroundColor;
```

#### Discussion

Use this property to customize the background color of your popover. Changing the value of this property while the popover is visible triggers an animated changeover to the new color. The default value of this property is `nil`, which corresponds to the default background color.

## See Also

### Customizing the popover appearance
- [var layoutMargins: UIEdgeInsets](./layoutmargins.md)
  The margins that define the portion of the screen in which it is permissible to display the popover.
- [var backgroundViewClass: AnyClass?](./backgroundviewclass.md)
  The class to use for displaying the popover background content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/backgroundcolor)*