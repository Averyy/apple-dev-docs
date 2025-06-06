# backgroundColor

**Framework**: UIKit  
**Kind**: property

The color of the popover’s backdrop view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@NSCopying
@MainActor var backgroundColor: UIColor? { get set }
```

#### Discussion

Use this property to customize the background color of your popover. Changing the value of this property while the popover is visible triggers an animated changeover to the new color. The default value of this property is `nil`, which corresponds to the default background color.

## See Also

- [var layoutMargins: UIEdgeInsets](uipopovercontroller/layoutmargins.md)
  The margins that define the portion of the screen in which it is permissible to display the popover.
- [var backgroundViewClass: AnyClass?](uipopovercontroller/backgroundviewclass.md)
  The class to use for displaying the popover background content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/backgroundcolor)*