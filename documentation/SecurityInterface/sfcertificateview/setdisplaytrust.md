# setDisplayTrust(_:)

**Framework**: Security Interface  
**Kind**: method

Specifies whether the user can see the certificate’s trust settings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func setDisplayTrust(_ display: Bool)
```

#### Discussion

Certificate trust settings are not displayed by default. To show the certificate’s trust settings, you must explicitly set the display value to [`true`](https://developer.apple.com/documentation/Swift/true). with either this method or the [`setEditableTrust(_:)`](sfcertificateview/seteditabletrust(_:).md) method.

## Parameters

- `display`: Pass   to display the trust settings, or   to hide them.

## See Also

- [func isTrustDisplayed() -> Bool](sfcertificateview/istrustdisplayed.md)
  Indicates if the view currently shows the certificate’s trust settings.
- [func setDetailsDisclosed(Bool)](sfcertificateview/setdetailsdisclosed(_:).md)
  Sets whether the certificate details subview is disclosed.
- [func setDisplayDetails(Bool)](sfcertificateview/setdisplaydetails(_:).md)
  Specifies whether the user can see the certificate details.
- [func setEditableTrust(Bool)](sfcertificateview/seteditabletrust(_:).md)
  Specifies whether the user can edit the certificate’s trust settings.
- [func setPolicies(Any!)](sfcertificateview/setpolicies(_:).md)
  Specifies the policies to use when evaluating this certificate’s status.
- [func setPoliciesDisclosed(Bool)](sfcertificateview/setpoliciesdisclosed(_:).md)
  Specifies whether the trust policy settings subview is disclosed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/setdisplaytrust(_:))*