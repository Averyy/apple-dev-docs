# kCFStreamSocketSecurityLevelSSLv3

**Framework**: Core Foundation  
**Kind**: var  
**Role**: Global Variable

Specifies that SSL version 3 be set as the security protocol for a socket stream pair.

**Availability**:
- iOS 2.0+ - Deprecated in 10.0
- iPadOS 2.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.2+ - Deprecated in 10.12
- tvOS - Deprecated in 10.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 3.0

## Declaration

```swift
let kCFStreamSocketSecurityLevelSSLv3: CFString
```

```c
extern CFStringRef const kCFStreamSocketSecurityLevelSSLv3;
```

## Discussion

If SSL version 3 is not available, specifies that SSL version 2 be set as the security protocol for a socket stream.

## See Also

### Constants
- [let kCFStreamSocketSecurityLevelNone: CFString](./kcfstreamsocketsecuritylevelnone.md)
  Specifies that no security level be set.
- [let kCFStreamSocketSecurityLevelSSLv2: CFString](./kcfstreamsocketsecuritylevelsslv2.md)
  Specifies that SSL version 2 be set as the security protocol for a socket stream.
- [let kCFStreamSocketSecurityLevelTLSv1: CFString](./kcfstreamsocketsecurityleveltlsv1.md)
  Specifies that TLS version 1 be set as the security protocol for a socket stream.
- [let kCFStreamSocketSecurityLevelNegotiatedSSL: CFString](./kcfstreamsocketsecuritylevelnegotiatedssl.md)
  Specifies that the highest level security protocol that can be negotiated be set as the security protocol for a socket stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfstreamsocketsecuritylevelsslv3)*