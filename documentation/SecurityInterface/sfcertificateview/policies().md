# policies()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns an array of policies used to evaluate the status of the displayed certificate.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func policies() -> [Any]!
```

```objc
- (NSArray *) policies;
```

#### Discussion

This method returns an autoreleased [`NSArray`](../../Foundation/nsarray.md) containing one or more instances of [`SecPolicy`](../../Security/secpolicy.md). The array always contains at least one item (the Apple X.509 Basic policy, if you have never called the [`setPolicies(_:)`](./setpolicies%28_%29.md) method).

## See Also

### Getting Information About the View
- [func certificate() -> Unmanaged<SecCertificate>!](./certificate%28%29.md)
  Returns the certificate currently displayed in the view.
- [func detailsDisplayed() -> Bool](./detailsdisplayed%28%29.md)
  Indicates if the view currently shows the certificate’s details.
- [func detailsDisclosed() -> Bool](./detailsdisclosed%28%29.md)
  Returns whether the view currently shows the certificate’s details.
- [func isTrustDisplayed() -> Bool](./istrustdisplayed%28%29.md)
  Indicates if the view currently shows the certificate’s trust settings.
- [func isEditable() -> Bool](./iseditable%28%29.md)
  Indicates if the view allows the user to edit the certificate’s trust.
- [func policiesDisclosed() -> Bool](./policiesdisclosed%28%29.md)
  Returns whether the trust policy subview is disclosed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/policies())*