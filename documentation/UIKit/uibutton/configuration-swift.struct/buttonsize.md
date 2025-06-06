# buttonSize

**Framework**: UIKit  
**Kind**: property

A size that requests a preferred size for the button.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
var buttonSize: UIButton.Configuration.Size { get set }
```

#### Discussion

The size indicates a system-defined size you prefer for this button. The exact size of the button may change regardless of this value.

## See Also

- [UIButton.Configuration.Size](uibutton/configuration-swift.struct/size.md)
  A predefined size for button elements.
- [var contentInsets: NSDirectionalEdgeInsets](uibutton/configuration-swift.struct/contentinsets.md)
  The distance from the button’s content area to its bounds.
- [func setDefaultContentInsets()](uibutton/configuration-swift.struct/setdefaultcontentinsets.md)
  Restores the default content insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/buttonsize)*