# certificate()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns the certificate currently displayed in the view.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func certificate() -> Unmanaged<SecCertificate>!
```

```objc
- (SecCertificateRef) certificate;
```

## See Also

### Getting Information About the View
- [func detailsDisplayed() -> Bool](./detailsdisplayed%28%29.md)
  Indicates if the view currently shows the certificate’s details.
- [func detailsDisclosed() -> Bool](./detailsdisclosed%28%29.md)
  Returns whether the view currently shows the certificate’s details.
- [func isTrustDisplayed() -> Bool](./istrustdisplayed%28%29.md)
  Indicates if the view currently shows the certificate’s trust settings.
- [func isEditable() -> Bool](./iseditable%28%29.md)
  Indicates if the view allows the user to edit the certificate’s trust.
- [func policies() -> [Any]!](./policies%28%29.md)
  Returns an array of policies used to evaluate the status of the displayed certificate.
- [func policiesDisclosed() -> Bool](./policiesdisclosed%28%29.md)
  Returns whether the trust policy subview is disclosed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/certificate())*