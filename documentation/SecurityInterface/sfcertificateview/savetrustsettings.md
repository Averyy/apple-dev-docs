# saveTrustSettings()

**Framework**: Security Interface  
**Kind**: method

Saves the user’s current trust settings for the displayed certificate.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func saveTrustSettings()
```

#### Discussion

If trust settings are not editable, this method effectively does nothing. You can use `SecTrustGetUserTrust` to subsequently retrieve the trust settings.

## See Also

- [func setEditableTrust(Bool)](sfcertificateview/seteditabletrust(_:).md)
  Specifies whether the user can edit the certificate’s trust settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/savetrustsettings())*