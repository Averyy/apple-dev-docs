# kSecCodeInfoEntitlementsDict

**Framework**: Security  
**Kind**: var

A key whose value is a dictionary of embedded entitlements.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCodeInfoEntitlementsDict: CFString
```

#### Discussion

The value is a [`CFDictionary`](https://developer.apple.com/documentation/CoreFoundation/CFDictionary) object containing the embedded entitlements of the code if it has entitlements and they are in standard dictionary form. The value is absent if the code has no entitlements, or they are in a different format (in which case, see [`kSecCodeInfoEntitlements`](kseccodeinfoentitlements.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccodeinfoentitlementsdict)*