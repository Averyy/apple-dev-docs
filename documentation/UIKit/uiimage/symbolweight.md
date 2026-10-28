# UIImage.SymbolWeight

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate which weight variant of a symbol image to use.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum SymbolWeight
```

```c
enum UIImageSymbolWeight : NSInteger;
```

## Overview

The definition of a symbol image includes multiple scale and weight variants. The weight variants offer a way to progressively thicken some or all of the image’s lines. Weights do not correspond to a specific line thickness.

## Topics

### Symbol image weights
- [UIImage.SymbolWeight.unspecified](./symbolweight/unspecified.md)
  An unspecified symbol image weight.
- [UIImage.SymbolWeight.ultraLight](./symbolweight/ultralight.md)
  An ultralight weight.
- [UIImage.SymbolWeight.thin](./symbolweight/thin.md)
  A thin weight
- [UIImage.SymbolWeight.light](./symbolweight/light.md)
  A light weight.
- [UIImage.SymbolWeight.regular](./symbolweight/regular.md)
  A regular weight.
- [UIImage.SymbolWeight.medium](./symbolweight/medium.md)
  A medium weight.
- [UIImage.SymbolWeight.semibold](./symbolweight/semibold.md)
  A semibold weight.
- [UIImage.SymbolWeight.bold](./symbolweight/bold.md)
  A bold weight.
- [UIImage.SymbolWeight.heavy](./symbolweight/heavy.md)
  A heavy weight.
- [UIImage.SymbolWeight.black](./symbolweight/black.md)
  An ultra-heavy weight.
### Getting the font weight
- [func fontWeight() -> UIFont.Weight](./symbolweight/fontweight%28%29.md)
  The font weight for the specified symbol weight.
### Initializers
- [init?(rawValue: Int)](./symbolweight/init%28rawvalue%29.md)

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
- [UIImage.SymbolColorRenderingMode](./symbolcolorrenderingmode.md)
- [UIImage.SymbolVariableValueMode](./symbolvariablevaluemode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolweight)*