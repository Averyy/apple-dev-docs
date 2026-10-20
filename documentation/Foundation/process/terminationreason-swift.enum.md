# Process.TerminationReason

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the termination reason values that the system returns.

**Availability**:
- macOS 10.6+

## Declaration

```swift
enum TerminationReason
```

```c
enum NSTaskTerminationReason : NSInteger;
```

## Topics

### Constants
- [Process.TerminationReason.exit](./terminationreason-swift.enum/exit.md)
  The task exited normally.
- [Process.TerminationReason.uncaughtSignal](./terminationreason-swift.enum/uncaughtsignal.md)
  The task exited due to an uncaught signal.
### Initializers
- [init?(rawValue: Int)](./terminationreason-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with constants
- [enum QualityOfService](../qualityofservice.md)
  Constants that indicate the nature and importance of work to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/terminationreason-swift.enum)*