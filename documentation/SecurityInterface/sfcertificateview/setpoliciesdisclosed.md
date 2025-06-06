# setPoliciesDisclosed(_:)

**Framework**: Security Interface  
**Kind**: method

Specifies whether the trust policy settings subview is disclosed.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func setPoliciesDisclosed(_ disclosed: Bool)
```

#### Discussion

The trust policy settings can be shown or hidden depending on whether the user clicks the disclosure triangle. This method sets the state of that disclosure triangle and the visibility of the corresponding view.

## Parameters

- `disclosed`: Pass   to display the certificate details, or   to hide them.

## See Also

- [func setDetailsDisclosed(Bool)](sfcertificateview/setdetailsdisclosed(_:).md)
  Sets whether the certificate details subview is disclosed.
- [func setDisplayDetails(Bool)](sfcertificateview/setdisplaydetails(_:).md)
  Specifies whether the user can see the certificate details.
- [func setDisplayTrust(Bool)](sfcertificateview/setdisplaytrust(_:).md)
  Specifies whether the user can see the certificate’s trust settings.
- [func setEditableTrust(Bool)](sfcertificateview/seteditabletrust(_:).md)
  Specifies whether the user can edit the certificate’s trust settings.
- [func setPolicies(Any!)](sfcertificateview/setpolicies(_:).md)
  Specifies the policies to use when evaluating this certificate’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/setpoliciesdisclosed(_:))*