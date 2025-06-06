# contentInsets

**Framework**: UIKit  
**Kind**: property

The distance from the button’s content area to its bounds.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
var contentInsets: NSDirectionalEdgeInsets { get set }
```

#### Discussion

A button has a default inset based on its styling. This property is an additional inset applied after that default inset.

## See Also

- [var buttonSize: UIButton.Configuration.Size](uibutton/configuration-swift.struct/buttonsize.md)
  A size that requests a preferred size for the button.
- [UIButton.Configuration.Size](uibutton/configuration-swift.struct/size.md)
  A predefined size for button elements.
- [func setDefaultContentInsets()](uibutton/configuration-swift.struct/setdefaultcontentinsets.md)
  Restores the default content insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/contentinsets)*