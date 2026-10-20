# NSPrinter.TableStatus

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the state of a printer information table stored by a printer object.

**Availability**:
- macOS

## Declaration

```swift
enum TableStatus
```

```c
enum NSPrinterTableStatus : NSUInteger;
```

#### Overview

These constants are used by [`statusForTable:`](./statusfortable_.md).

## Topics

### Constants
- [NSPrinter.TableStatus.ok](./tablestatus/ok.md)
  Printer table was found and is valid.
- [NSPrinter.TableStatus.notFound](./tablestatus/notfound.md)
  Printer table was not found.
- [NSPrinter.TableStatus.error](./tablestatus/error.md)
  Printer table is not valid.
### Initializers
- [init?(rawValue: UInt)](./tablestatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Deprecated
- [Deprecated symbols](../nsprinter-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/tablestatus)*