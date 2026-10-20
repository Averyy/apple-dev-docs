# NSPasteboard.WritingOptions

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Type to specify options for writing to a pasteboard.

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct WritingOptions
```

```c
enum NSPasteboardWritingOptions : NSUInteger;
```

#### Overview

For possible values, see [Pasteboard Writing Options](../pasteboard-writing-options.md).

## Topics

### Options
- [static var promised: NSPasteboard.WritingOptions](./writingoptions/promised.md)
  Data for a type with this option is promised, not immediately written.
### Initializers
- [init(rawValue: UInt)](./writingoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/writingoptions)*