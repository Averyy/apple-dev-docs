# SWAttributionView.BackgroundStyle

**Framework**: Shared with You  
**Kind**: enum  
**Role**: Enumeration

The background styling of the attribution view’s contents.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum BackgroundStyle
```

```c
enum SWAttributionViewBackgroundStyle : NSInteger;
```

## Topics

### Background styles
- [SWAttributionView.BackgroundStyle.default](./backgroundstyle-swift.enum/default.md)
  The default background style the system chooses.
- [SWAttributionView.BackgroundStyle.color](./backgroundstyle-swift.enum/color.md)
  A non-material background color for the view’s contents, best when placed over monochrome backgrounds.
- [SWAttributionView.BackgroundStyle.material](./backgroundstyle-swift.enum/material.md)
  A material background blur for the view’s contents, best when placed over multicolored backgrounds.
### Initializers
- [init?(rawValue: Int)](./backgroundstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Customizing the view
- [SWAttributionView.DisplayContext](./displaycontext-swift.enum.md)
  The context for the content that influences the ranking of this view’s highlight.
- [SWAttributionView.HorizontalAlignment](./horizontalalignment-swift.enum.md)
  The horizontal alignment of attribution view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swattributionview/backgroundstyle-swift.enum)*