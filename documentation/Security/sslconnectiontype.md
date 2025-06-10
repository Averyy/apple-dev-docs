# SSLConnectionType

**Framework**: Security  
**Kind**: enum

The flags that indicate whether a context is to be used for streaming or datagram-based communication.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum SSLConnectionType
```

#### Overview

Use one of these flags with the [`SSLCreateContext(_:_:_:)`](sslcreatecontext(_:_:_:).md) function to indicate whether the context is intended for use in stream-based or datagram-based communication.

## Topics

### Constants
- [SSLConnectionType.streamType](sslconnectiontype/streamtype.md)
  Stream-based communication (TCP).
- [SSLConnectionType.datagramType](sslconnectiontype/datagramtype.md)
  Datagram-based communication (UDP).
### Initializers
- [init?(rawValue: Int32)](sslconnectiontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslconnectiontype)*