# NSTextField.BezelStyle

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The style of bezel the text field displays.

**Availability**:
- macOS

## Declaration

```swift
enum BezelStyle
```

```c
enum NSTextFieldBezelStyle : NSUInteger;
```

## Overview

Use [`bezelStyle`](../nstextfieldcell/bezelstyle.md) to set a text field’s bezel style.

## Topics

### Constants
- [NSTextField.BezelStyle.squareBezel](./bezelstyle-swift.enum/squarebezel.md)
  A style that draws a bezel with square corners around a text field.
- [NSTextField.BezelStyle.roundedBezel](./bezelstyle-swift.enum/roundedbezel.md)
  A style that draws a bezel with rounded corners around a single-line text field.
### Initializers
- [init?(rawValue: UInt)](./bezelstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Controlling the background
- [var backgroundColor: NSColor?](./backgroundcolor.md)
  The color of the background the text field’s cell draws behind the text.
- [var drawsBackground: Bool](./drawsbackground.md)
  A Boolean value that controls whether the text field’s cell draws a background color behind the text.
- [var isBezeled: Bool](./isbezeled.md)
  A Boolean value that controls whether the text field draws a bezeled background around its contents.
- [var bezelStyle: NSTextField.BezelStyle](./bezelstyle-swift.property.md)
  The text field’s bezel style, square or rounded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/bezelstyle-swift.enum)*