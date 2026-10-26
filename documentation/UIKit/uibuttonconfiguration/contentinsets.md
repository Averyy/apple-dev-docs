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
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, assign, readwrite) NSDirectionalEdgeInsets contentInsets;
```

#### Discussion

A button has a default inset based on its styling. This property is an additional inset applied after that default inset.

## See Also

### Configuring layout
- [buttonSize](./buttonsize.md)
  A size that requests a preferred size for the button.
- [UIButtonConfigurationSize](../uibuttonconfigurationsize.md)
  A predefined size for button elements.
- [- setDefaultContentInsets](./setdefaultcontentinsets.md)
  Restores the default content insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibuttonconfiguration/contentinsets)*