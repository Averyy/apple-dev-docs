# contentInsets

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The distance from the button’s content area to its bounds.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS

## Declaration

```swift
var contentInsets: NSDirectionalEdgeInsets { get set }
```

## Discussion

A button has a default inset based on its styling. This property is an additional inset applied after that default inset.

## See Also

### Configuring layout
- [var buttonSize: UIButton.Configuration.Size](./buttonsize.md)
  A size that requests a preferred size for the button.
- [UIButton.Configuration.Size](./size.md)
  A predefined size for button elements.
- [func setDefaultContentInsets()](./setdefaultcontentinsets%28%29.md)
  Restores the default content insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/contentinsets)*