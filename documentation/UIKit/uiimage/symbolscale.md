# UIImage.SymbolScale

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate which scale variant of a symbol image to use.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum SymbolScale
```

```c
enum UIImageSymbolScale : NSInteger;
```

## Mentions

- [Configuring and displaying symbol images in your UI](../configuring-and-displaying-symbol-images-in-your-ui.md)

#### Overview

The definition of a symbol image includes multiple scale and weight variants. Scale variants offer a way to define the size of the image relative to layout guides in the symbol image’s definition file. The system chooses the appropriate size variant based on the available space and configuration options.

## Topics

### Symbol image scales
- [UIImage.SymbolScale.default](./symbolscale/default.md)
  The default scale variant that matches the system usage.
- [UIImage.SymbolScale.unspecified](./symbolscale/unspecified.md)
  An unspecified scale.
- [UIImage.SymbolScale.small](./symbolscale/small.md)
  The small variant of the symbol image.
- [UIImage.SymbolScale.medium](./symbolscale/medium.md)
  The medium variant of the symbol image
- [UIImage.SymbolScale.large](./symbolscale/large.md)
  The large variant of the symbol image.
### Initializers
- [init?(rawValue: Int)](./symbolscale/init%28rawvalue%29.md)

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
- [UIImage.SymbolWeight](./symbolweight.md)
  Constants that indicate which weight variant of a symbol image to use.
- [UIImage.SymbolColorRenderingMode](./symbolcolorrenderingmode.md)
- [UIImage.SymbolVariableValueMode](./symbolvariablevaluemode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolscale)*