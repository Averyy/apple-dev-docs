# policiesDisclosed()

**Framework**: Security Interface  
**Kind**: method

Returns whether the trust policy subview is disclosed.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func policiesDisclosed() -> Bool
```

#### Discussion

The trust policy settings can be shown or hidden depending on whether the user clicks the disclosure triangle. This method returns the state of that disclosure triangle.

## See Also

- [func certificate() -> Unmanaged<SecCertificate>!](sfcertificateview/certificate.md)
  Returns the certificate currently displayed in the view.
- [func detailsDisplayed() -> Bool](sfcertificateview/detailsdisplayed.md)
  Indicates if the view currently shows the certificate’s details.
- [func detailsDisclosed() -> Bool](sfcertificateview/detailsdisclosed.md)
  Returns whether the view currently shows the certificate’s details.
- [func isTrustDisplayed() -> Bool](sfcertificateview/istrustdisplayed.md)
  Indicates if the view currently shows the certificate’s trust settings.
- [func isEditable() -> Bool](sfcertificateview/iseditable.md)
  Indicates if the view allows the user to edit the certificate’s trust.
- [func policies() -> [Any]!](sfcertificateview/policies.md)
  Returns an array of policies used to evaluate the status of the displayed certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/policiesdisclosed())*