# UIButton.Configuration.Size

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

A predefined size for button elements.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS

## Declaration

```swift
enum Size
```

#### Overview

You can use this enumeration to choose a predefined size for elements in a button. The value you choose for button size can be effectively overridden by explicitly assigning values for configuration elements like padding, corner style, or title and subtitle font sizes.

## Topics

### Button sizes
- [UIButton.Configuration.Size.large](./size/large.md)
  Displays button elements at a large size.
- [UIButton.Configuration.Size.medium](./size/medium.md)
  Displays button elements at a standard size.
- [UIButton.Configuration.Size.small](./size/small.md)
  Displays button elements at a small size.
- [UIButton.Configuration.Size.mini](./size/mini.md)
  Displays button elements at the smallest size.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)

## See Also

### Configuring layout
- [var buttonSize: UIButton.Configuration.Size](./buttonsize.md)
  A size that requests a preferred size for the button.
- [var contentInsets: NSDirectionalEdgeInsets](./contentinsets.md)
  The distance from the button’s content area to its bounds.
- [func setDefaultContentInsets()](./setdefaultcontentinsets%28%29.md)
  Restores the default content insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/size)*