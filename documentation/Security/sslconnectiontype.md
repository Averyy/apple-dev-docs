# SSLConnectionType

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

The flags that indicate whether a context is to be used for streaming or datagram-based communication.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SSLConnectionType
```

```c
enum SSLConnectionType : int;
```

#### Overview

Use one of these flags with the [`SSLCreateContext(_:_:_:)`](./sslcreatecontext%28_,_,_%29.md) function to indicate whether the context is intended for use in stream-based or datagram-based communication.

## Topics

### Constants
- [SSLConnectionType.streamType](./sslconnectiontype/streamtype.md)
  Stream-based communication (TCP).
- [SSLConnectionType.datagramType](./sslconnectiontype/datagramtype.md)
  Datagram-based communication (UDP).
### Initializers
- [init?(rawValue: Int32)](./sslconnectiontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslconnectiontype)*