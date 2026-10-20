# buttonSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A size that requests a preferred size for the button.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS

## Declaration

```swift
var buttonSize: UIButton.Configuration.Size { get set }
```

#### Discussion

The size indicates a system-defined size you prefer for this button. The exact size of the button may change regardless of this value.

## See Also

### Configuring layout
- [UIButton.Configuration.Size](./size.md)
  A predefined size for button elements.
- [var contentInsets: NSDirectionalEdgeInsets](./contentinsets.md)
  The distance from the button’s content area to its bounds.
- [func setDefaultContentInsets()](./setdefaultcontentinsets%28%29.md)
  Restores the default content insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/buttonsize)*