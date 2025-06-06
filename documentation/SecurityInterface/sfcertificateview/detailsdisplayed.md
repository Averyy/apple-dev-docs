# detailsDisplayed()

**Framework**: Security Interface  
**Kind**: method

Indicates if the view currently shows the certificate’s details.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func detailsDisplayed() -> Bool
```

## See Also

- [func certificate() -> Unmanaged<SecCertificate>!](sfcertificateview/certificate.md)
  Returns the certificate currently displayed in the view.
- [func detailsDisclosed() -> Bool](sfcertificateview/detailsdisclosed.md)
  Returns whether the view currently shows the certificate’s details.
- [func isTrustDisplayed() -> Bool](sfcertificateview/istrustdisplayed.md)
  Indicates if the view currently shows the certificate’s trust settings.
- [func isEditable() -> Bool](sfcertificateview/iseditable.md)
  Indicates if the view allows the user to edit the certificate’s trust.
- [func policies() -> [Any]!](sfcertificateview/policies.md)
  Returns an array of policies used to evaluate the status of the displayed certificate.
- [func policiesDisclosed() -> Bool](sfcertificateview/policiesdisclosed.md)
  Returns whether the trust policy subview is disclosed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/detailsdisplayed())*