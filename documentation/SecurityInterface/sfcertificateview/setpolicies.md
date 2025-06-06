# setPolicies(_:)

**Framework**: Security Interface  
**Kind**: method

Specifies the policies to use when evaluating this certificate’s status.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setPolicies(_ policies: Any!)
```

#### Discussion

Applications typically display a certificate view in the context of a specific use, such as SSL or S/MIME. You should set only the policy references that apply to your intended use.

## Parameters

- `policies`: The policy or policies to use. You can pass either a   object or an NSArray (containing one or more objects of type   ) in this parameter. If   is set to nil, the Apple X.509 Basic Policy is used. See   for a list of policies and object identifiers provided by the AppleX509TP module.

## See Also

- [func policies() -> [Any]!](sfcertificateview/policies.md)
  Returns an array of policies used to evaluate the status of the displayed certificate.
- [func setDetailsDisclosed(Bool)](sfcertificateview/setdetailsdisclosed(_:).md)
  Sets whether the certificate details subview is disclosed.
- [func setDisplayDetails(Bool)](sfcertificateview/setdisplaydetails(_:).md)
  Specifies whether the user can see the certificate details.
- [func setDisplayTrust(Bool)](sfcertificateview/setdisplaytrust(_:).md)
  Specifies whether the user can see the certificate’s trust settings.
- [func setEditableTrust(Bool)](sfcertificateview/seteditabletrust(_:).md)
  Specifies whether the user can edit the certificate’s trust settings.
- [func setPoliciesDisclosed(Bool)](sfcertificateview/setpoliciesdisclosed(_:).md)
  Specifies whether the trust policy settings subview is disclosed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/setpolicies(_:))*