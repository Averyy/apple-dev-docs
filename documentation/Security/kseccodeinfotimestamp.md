# kSecCodeInfoTimestamp

**Framework**: Security  
**Kind**: var

A key whose value indicates the actual signing date.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoTimestamp: CFString
```

#### Discussion

The value is a [`CFDate`](https://developer.apple.com/documentation/CoreFoundation/CFDate) object describing the signing date as (securely) certified by a timestamp authority service. This timestamp cannot be falsified by the signer, and is trusted to the same degree as the timestamp service that created the timestamp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfotimestamp)*