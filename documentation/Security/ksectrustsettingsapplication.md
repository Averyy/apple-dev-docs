# kSecTrustSettingsApplication

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A trusted application reference for the application checking the certificate’s trust settings.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kSecTrustSettingsApplication: String { get }
```

```c
#define kSecTrustSettingsApplication
```

#### Discussion

The value is a [`SecTrustedApplication`](./sectrustedapplication.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectrustsettingsapplication)*