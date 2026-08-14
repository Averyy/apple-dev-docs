# NSPasteboard.WritingOptions

**Framework**: AppKit  
**Kind**: struct

Type to specify options for writing to a pasteboard.

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct WritingOptions
```

#### Overview

For possible values, see [`Pasteboard Writing Options`](pasteboard-writing-options.md).

## Topics

### Options
- [static var promised: NSPasteboard.WritingOptions](nspasteboard/writingoptions/promised.md)
  Data for a type with this option is promised, not immediately written.
### Initializers
- [init(rawValue: UInt)](nspasteboard/writingoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/writingoptions)*