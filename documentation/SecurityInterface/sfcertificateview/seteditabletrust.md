# setEditableTrust(_:)

**Framework**: Security Interface  
**Kind**: method

Specifies whether the user can edit the certificate’s trust settings.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func setEditableTrust(_ editable: Bool)
```

#### Discussion

For behavioral compatibility with macOS 10.3, this method causes the certificate trust settings to be displayed if they are not currently visible (that is, if [`setDisplayTrust(_:)`](sfcertificateview/setdisplaytrust(_:).md) is set to [`false`](https://developer.apple.com/documentation/Swift/false)).

## Parameters

- `editable`: Pass   if the trust settings should be editable.

## See Also

- [func setDisplayTrust(Bool)](sfcertificateview/setdisplaytrust(_:).md)
  Specifies whether the user can see the certificate’s trust settings.
- [func setDetailsDisclosed(Bool)](sfcertificateview/setdetailsdisclosed(_:).md)
  Sets whether the certificate details subview is disclosed.
- [func setDisplayDetails(Bool)](sfcertificateview/setdisplaydetails(_:).md)
  Specifies whether the user can see the certificate details.
- [func setDisplayTrust(Bool)](sfcertificateview/setdisplaytrust(_:).md)
  Specifies whether the user can see the certificate’s trust settings.
- [func setPolicies(Any!)](sfcertificateview/setpolicies(_:).md)
  Specifies the policies to use when evaluating this certificate’s status.
- [func setPoliciesDisclosed(Bool)](sfcertificateview/setpoliciesdisclosed(_:).md)
  Specifies whether the trust policy settings subview is disclosed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/seteditabletrust(_:))*