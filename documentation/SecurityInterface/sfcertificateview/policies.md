# policies()

**Framework**: Security Interface  
**Kind**: method

Returns an array of policies used to evaluate the status of the displayed certificate.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func policies() -> [Any]!
```

#### Discussion

This method returns an autoreleased [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) containing one or more instances of [`SecPolicy`](https://developer.apple.com/documentation/Security/SecPolicy). The array always contains at least one item (the Apple X.509 Basic policy, if you have never called the [`setPolicies(_:)`](sfcertificateview/setpolicies(_:).md) method).

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
- [func policiesDisclosed() -> Bool](sfcertificateview/policiesdisclosed.md)
  Returns whether the trust policy subview is disclosed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/policies())*