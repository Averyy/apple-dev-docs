# MTLLogLevel

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

The supported log levels for shader logging.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
enum MTLLogLevel
```

```c
enum MTLLogLevel : NSInteger;
```

## Topics

### Enumeration cases
- [MTLLogLevel.debug](./mtlloglevel/debug.md)
  The log level that captures diagnostic information.
- [MTLLogLevel.info](./mtlloglevel/info.md)
  The log level that captures additional information.
- [MTLLogLevel.notice](./mtlloglevel/notice.md)
  The log level that captures notifications.
- [MTLLogLevel.error](./mtlloglevel/error.md)
  The log level that captures error information.
- [MTLLogLevel.fault](./mtlloglevel/fault.md)
  The log level that captures fault information.
- [MTLLogLevel.undefined](./mtlloglevel/undefined.md)
  The log level when the log level hasn’t been configured.
### Initializers
- [init?(rawValue: Int)](./mtlloglevel/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlloglevel)*