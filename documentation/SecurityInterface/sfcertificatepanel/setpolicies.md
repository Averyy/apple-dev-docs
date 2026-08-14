# setPolicies(_:)

**Framework**: Security Interface  
**Kind**: method

Specifies one or more policies that apply to the displayed certificates.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setPolicies(_ policies: Any!)
```

#### Discussion

Applications typically display a certificate panel in the context of a specific use, such as SSL or S/MIME. You should set only the policy references that apply to your intended use. See [`Certificate, Key, and Trust Services`](https://developer.apple.com/documentation/security/certificate-key-and-trust-services) for a list of policies and object identifiers provided by the [`AppleX509TP Module`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/CDSA/CDSA.html#//apple_ref/doc/uid/TP40011172-CH4-CHDEEDBE).

## Parameters

- `policies`: The policies to use when evaluating the certificates’ status. You can pass either a [`SecPolicy`](https://developer.apple.com/documentation/security/secpolicy) object or an [`NSArray`](https://developer.apple.com/documentation/foundation/nsarray) (containing one or more [`SecPolicy`](https://developer.apple.com/documentation/security/secpolicy) instances) in this parameter. If `policies` is set to `nil`, the Apple X.509 Basic Policy is used.

## See Also

- [func setAlternateButtonTitle(String!)](sfcertificatepanel/setalternatebuttontitle(_:).md)
  Customizes the title of the alternate button.
- [func setDefaultButtonTitle(String!)](sfcertificatepanel/setdefaultbuttontitle(_:).md)
  Customizes the title of the default button.
- [func policies() -> [Any]!](sfcertificatepanel/policies.md)
  Returns an array of policies used to evaluate the status of the displayed certificates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel/setpolicies(_:))*