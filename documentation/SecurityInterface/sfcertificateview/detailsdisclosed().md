# detailsDisclosed()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns whether the view currently shows the certificate’s details.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func detailsDisclosed() -> Bool
```

```objc
- (BOOL) detailsDisclosed;
```

## Discussion

The certificate details can be shown or hidden depending on whether the user clicks the disclosure triangle. This method returns the state of that disclosure triangle.

## See Also

### Getting Information About the View
- [func certificate() -> Unmanaged<SecCertificate>!](./certificate%28%29.md)
  Returns the certificate currently displayed in the view.
- [func detailsDisplayed() -> Bool](./detailsdisplayed%28%29.md)
  Indicates if the view currently shows the certificate’s details.
- [func isTrustDisplayed() -> Bool](./istrustdisplayed%28%29.md)
  Indicates if the view currently shows the certificate’s trust settings.
- [func isEditable() -> Bool](./iseditable%28%29.md)
  Indicates if the view allows the user to edit the certificate’s trust.
- [func policies() -> [Any]!](./policies%28%29.md)
  Returns an array of policies used to evaluate the status of the displayed certificate.
- [func policiesDisclosed() -> Bool](./policiesdisclosed%28%29.md)
  Returns whether the trust policy subview is disclosed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/detailsdisclosed())*