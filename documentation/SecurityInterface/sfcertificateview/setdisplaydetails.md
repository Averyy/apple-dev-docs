# setDisplayDetails(_:)

**Framework**: Security Interface  
**Kind**: method

Specifies whether the user can see the certificate details.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setDisplayDetails(_ display: Bool)
```

#### Discussion

For behavioral compatibility with macOS 10.3, certificate details are displayed by default. To hide the details of a certificate, you must explicitly set the display value to [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `display`: Pass   to display the certificate details, or   to hide them.

## See Also

- [func detailsDisplayed() -> Bool](sfcertificateview/detailsdisplayed.md)
  Indicates if the view currently shows the certificate’s details.
- [func setDetailsDisclosed(Bool)](sfcertificateview/setdetailsdisclosed(_:).md)
  Sets whether the certificate details subview is disclosed.
- [func setDisplayTrust(Bool)](sfcertificateview/setdisplaytrust(_:).md)
  Specifies whether the user can see the certificate’s trust settings.
- [func setEditableTrust(Bool)](sfcertificateview/seteditabletrust(_:).md)
  Specifies whether the user can edit the certificate’s trust settings.
- [func setPolicies(Any!)](sfcertificateview/setpolicies(_:).md)
  Specifies the policies to use when evaluating this certificate’s status.
- [func setPoliciesDisclosed(Bool)](sfcertificateview/setpoliciesdisclosed(_:).md)
  Specifies whether the trust policy settings subview is disclosed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/setdisplaydetails(_:))*