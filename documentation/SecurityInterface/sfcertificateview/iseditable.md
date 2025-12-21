# isEditable()

**Framework**: Security Interface  
**Kind**: method

Indicates if the view allows the user to edit the certificate’s trust.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func isEditable() -> Bool
```

## See Also

- [func setEditableTrust(Bool)](sfcertificateview/seteditabletrust(_:).md)
  Specifies whether the user can edit the certificate’s trust settings.
- [func certificate() -> Unmanaged<SecCertificate>!](sfcertificateview/certificate.md)
  Returns the certificate currently displayed in the view.
- [func detailsDisplayed() -> Bool](sfcertificateview/detailsdisplayed.md)
  Indicates if the view currently shows the certificate’s details.
- [func detailsDisclosed() -> Bool](sfcertificateview/detailsdisclosed.md)
  Returns whether the view currently shows the certificate’s details.
- [func isTrustDisplayed() -> Bool](sfcertificateview/istrustdisplayed.md)
  Indicates if the view currently shows the certificate’s trust settings.
- [func policies() -> [Any]!](sfcertificateview/policies.md)
  Returns an array of policies used to evaluate the status of the displayed certificate.
- [func policiesDisclosed() -> Bool](sfcertificateview/policiesdisclosed.md)
  Returns whether the trust policy subview is disclosed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/iseditable())*