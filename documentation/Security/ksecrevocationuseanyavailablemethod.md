# kSecRevocationUseAnyAvailableMethod

**Framework**: Security  
**Kind**: var

Perform either OCSP or CRL checking.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var kSecRevocationUseAnyAvailableMethod: CFOptionFlags { get }
```

#### Discussion

The checking is performed according to the method(s) specified in the certificate and the value of [`kSecRevocationPreferCRL`](ksecrevocationprefercrl.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecrevocationuseanyavailablemethod)*