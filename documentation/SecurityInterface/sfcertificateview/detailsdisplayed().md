# detailsDisplayed()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Indicates if the view currently shows the certificate’s details.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func detailsDisplayed() -> Bool
```

```objc
- (BOOL) detailsDisplayed;
```

## See Also

### Getting Information About the View
- [func certificate() -> Unmanaged<SecCertificate>!](./certificate%28%29.md)
  Returns the certificate currently displayed in the view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/detailsdisplayed())*