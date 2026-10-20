# negotiatedSSL

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Specifies that the highest level security protocol that can be negotiated be set as the security protocol for a socket stream.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let negotiatedSSL: StreamSocketSecurityLevel
```

```c
extern NSStreamSocketSecurityLevel const NSStreamSocketSecurityLevelNegotiatedSSL;
```

## See Also

### Type Properties
- [static let none: StreamSocketSecurityLevel](./none.md)
  Specifies that no security level be set for a socket stream.
- [static let ssLv2: StreamSocketSecurityLevel](./sslv2.md)
  Specifies that SSL version 2 be set as the security protocol for a socket stream.
- [static let ssLv3: StreamSocketSecurityLevel](./sslv3.md)
  Specifies that SSL version 3 be set as the security protocol for a socket stream.
- [static let tlSv1: StreamSocketSecurityLevel](./tlsv1.md)
  Specifies that TLS version 1 be set as the security protocol for a socket stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/streamsocketsecuritylevel/negotiatedssl)*