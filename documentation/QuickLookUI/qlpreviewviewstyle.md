# QLPreviewViewStyle

**Framework**: Quick Look UI  
**Kind**: enum  
**Role**: Enumeration

Styles for a Preview View.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum QLPreviewViewStyle
```

```c
enum QLPreviewViewStyle : NSUInteger;
```

## Topics

### Choosing a Preview Style
- [QLPreviewViewStyle.normal](./qlpreviewviewstyle/normal.md)
  Provides the default preview style for larger, full-sized previews.
- [QLPreviewViewStyle.compact](./qlpreviewviewstyle/compact.md)
  Provides a compact preview style suited for smaller previews or inspectors.
### Initializers
- [init?(rawValue: UInt)](./qlpreviewviewstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Preview View
- [init!(frame: NSRect, style: QLPreviewViewStyle)](./qlpreviewview/init%28frame,style%29.md)
  Creates a preview view with the provided frame and style.
- [init!(frame: NSRect)](./qlpreviewview/init%28frame%29.md)
  Creates a preview view with the provided frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewviewstyle)*