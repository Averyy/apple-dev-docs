# AMLogLevel

**Framework**: Automator  
**Kind**: enum  
**Role**: Enumeration

Logging levels that Automator supports.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
enum AMLogLevel
```

```c
enum AMLogLevel : NSUInteger;
```

## Topics

### Constants
- [AMLogLevel.debug](./amloglevel/debug.md)
  The debug log level.
- [AMLogLevel.info](./amloglevel/info.md)
  The informational log level.
- [AMLogLevel.warn](./amloglevel/warn.md)
  The warning log level.
- [AMLogLevel.error](./amloglevel/error.md)
  The error log level.
### Initializers
- [init?(rawValue: UInt)](./amloglevel/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Performing Logging
- [- logMessageWithLevel:format:](./amaction/logmessagewithlevel_format_.md)
  Displays a message in Automator’s log area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amloglevel)*