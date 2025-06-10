# CFStreamErrorDomain

**Framework**: Core Foundation  
**Kind**: enum

Defines constants for values returned in the domain field of the `CFStreamError` structure.

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
enum CFStreamErrorDomain
```

#### Overview

These constants indicate how the error code in the `error` field in the [`CFStreamError`](cfstreamerror.md) structure should be interpreted.

## Topics

### Constants
- [CFStreamErrorDomain.custom](cfstreamerrordomain/custom.md)
  The error code is a custom error code.
- [CFStreamErrorDomain.POSIX](cfstreamerrordomain/posix.md)
  The error code is an error code defined in `errno.h`.
- [CFStreamErrorDomain.macOSStatus](cfstreamerrordomain/macosstatus.md)
  The error is an OSStatus value defined in `MacErrors.h`.
### Initializers
- [init?(rawValue: CFIndex)](cfstreamerrordomain/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum CFStreamStatus](cfstreamstatus.md)
  Constants that describe the status of a stream.
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreamerrordomain)*