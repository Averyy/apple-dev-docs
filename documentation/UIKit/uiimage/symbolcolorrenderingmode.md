# UIImage.SymbolColorRenderingMode

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum SymbolColorRenderingMode
```

```c
enum UIImageSymbolColorRenderingMode : NSInteger;
```

## Topics

### Enumeration Cases
- [UIImage.SymbolColorRenderingMode.automatic](./symbolcolorrenderingmode/automatic.md)
  Automatically uses an appropriate color rendering mode for the symbol’s color layers.
- [UIImage.SymbolColorRenderingMode.flat](./symbolcolorrenderingmode/flat.md)
  Renders the symbol’s color layers using flat colors.
- [UIImage.SymbolColorRenderingMode.gradient](./symbolcolorrenderingmode/gradient.md)
  Renders the symbol’s color layers using gradients.
### Initializers
- [init?(rawValue: Int)](./symbolcolorrenderingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a symbol configuration
- [convenience init(pointSize: CGFloat)](./symbolconfiguration-swift.class/init%28pointsize%29.md)
  Creates a configuration object with the specified point-size information.
- [convenience init(pointSize: CGFloat, weight: UIImage.SymbolWeight)](./symbolconfiguration-swift.class/init%28pointsize,weight%29.md)
  Creates a configuration object with the specified point-size and weight information.
- [convenience init(pointSize: CGFloat, weight: UIImage.SymbolWeight, scale: UIImage.SymbolScale)](./symbolconfiguration-swift.class/init%28pointsize,weight,scale%29.md)
  Creates a configuration object with the specified point-size, weight, and scale information.
- [convenience init(scale: UIImage.SymbolScale)](./symbolconfiguration-swift.class/init%28scale%29.md)
  Creates a configuration object with the specified scale information.
- [convenience init(textStyle: UIFont.TextStyle)](./symbolconfiguration-swift.class/init%28textstyle%29.md)
  Creates a configuration object with the specified font text style information.
- [convenience init(textStyle: UIFont.TextStyle, scale: UIImage.SymbolScale)](./symbolconfiguration-swift.class/init%28textstyle,scale%29.md)
  Creates a configuration object with the specified font text style and scale information.
- [convenience init(weight: UIImage.SymbolWeight)](./symbolconfiguration-swift.class/init%28weight%29.md)
  Creates a configuration object with the specified weight information.
- [convenience init(font: UIFont)](./symbolconfiguration-swift.class/init%28font%29.md)
  Creates a configuration object with the specified font information.
- [convenience init(font: UIFont, scale: UIImage.SymbolScale)](./symbolconfiguration-swift.class/init%28font,scale%29.md)
  Creates a configuration object with the specified font and scale information.
- [UIImage.SymbolScale](./symbolscale.md)
  Constants that indicate which scale variant of a symbol image to use.
- [UIImage.SymbolWeight](./symbolweight.md)
  Constants that indicate which weight variant of a symbol image to use.
- [UIImage.SymbolVariableValueMode](./symbolvariablevaluemode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolcolorrenderingmode)*