# CFStreamStatus

**Framework**: Core Foundation  
**Kind**: enum

Constants that describe the status of a stream.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CFStreamStatus
```

#### Overview

The `CFStreamStatus` enumeration defines constants that describe the status of a stream. These values are returned by [`CFReadStreamGetStatus(_:)`](cfreadstreamgetstatus(_:).md) and [`CFWriteStreamGetStatus(_:)`](cfwritestreamgetstatus(_:).md).

## Topics

### Constants
- [CFStreamStatus.notOpen](cfstreamstatus/notopen.md)
  The stream is not open for reading or writing.
- [CFStreamStatus.opening](cfstreamstatus/opening.md)
  The stream is being opened for reading or for writing.
- [CFStreamStatus.open](cfstreamstatus/open.md)
  The stream is open.
- [CFStreamStatus.reading](cfstreamstatus/reading.md)
  The stream is being read from.
- [CFStreamStatus.writing](cfstreamstatus/writing.md)
  The stream is being written to.
- [CFStreamStatus.atEnd](cfstreamstatus/atend.md)
  There is no more data to read, or no more data can be written.
- [CFStreamStatus.closed](cfstreamstatus/closed.md)
  The stream is closed.
- [CFStreamStatus.error](cfstreamstatus/error.md)
  An error occurred on the stream.
### Initializers
- [init?(rawValue: CFIndex)](cfstreamstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum CFStreamErrorDomain](cfstreamerrordomain.md)
  Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [CFStream Error Domain Constants (CFHost)](cfstream-error-domain-constants-cfhost.md)
  Defines constants for values returned in the domain field of the `CFStreamError` structure.
- [Error Subdomains](error-subdomains.md)
  Subdomains used to determine how to interpret an error in the `kCFStreamErrorDomainSOCKS` domain.
- [Secure Sockets (SOCKS) Errors](../CFNetwork/1518266-secure-sockets-socks-errors.md)
  Error codes returned by the `kCFStreamErrorDomainSOCKS` error domain.
- [struct CFStreamEventType](cfstreameventtype.md)
  Defines constants for stream-related events.
- [Stream Properties](stream-properties.md)
  Stream property names that can be set or copied.
- [CFStream Property SSL Settings Constants](cfstream-property-ssl-settings-constants.md)
  Constants for use in a `CFDictionary` object that is the value of the `kCFStreamPropertySSLSettings` stream property key.
- [CFStream Socket Security Level Constants](cfstream-socket-security-level-constants.md)
  Constants for setting the security level of a socket stream.
- [CFStream SOCKS Proxy Key Constants](cfstream-socks-proxy-key-constants.md)
  Constants for SOCKS Proxy `CFDictionary` keys.
- [Stream Service Types](stream-service-types.md)
  String constants that specify the service type of a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreamstatus)*