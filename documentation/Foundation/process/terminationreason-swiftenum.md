# Process.TerminationReason

**Framework**: Foundation  
**Kind**: enum

Constants that specify the termination reason values that the system returns.

**Availability**:
- macOS 10.6+

## Declaration

```swift
enum TerminationReason
```

## Topics

### Constants
- [Process.TerminationReason.exit](process/terminationreason-swift.enum/exit.md)
  The task exited normally.
- [Process.TerminationReason.uncaughtSignal](process/terminationreason-swift.enum/uncaughtsignal.md)
  The task exited due to an uncaught signal.
### Initializers
- [init?(rawValue: Int)](process/terminationreason-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum QualityOfService](qualityofservice.md)
  Constants that indicate the nature and importance of work to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/terminationreason-swift.enum)*