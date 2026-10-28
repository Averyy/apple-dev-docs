# setPolicies(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Specifies the policies to use when evaluating this certificate’s status.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setPolicies(_ policies: Any!)
```

```objc
- (void) setPolicies:(id) policies;
```

## Discussion

Applications typically display a certificate view in the context of a specific use, such as SSL or S/MIME. You should set only the policy references that apply to your intended use.

## Parameters

- `policies`: The policy or policies to use. You can pass either a `SecPolicyRef` object or an NSArray (containing one or more objects of type `SecPolicyRef` ) in this parameter. If `policies` is set to nil, the Apple X.509 Basic Policy is used. See [Certificate, Key, and Trust Services](../../Security/certificate-key-and-trust-services.md) for a list of policies and object identifiers provided by the AppleX509TP module.

## See Also

### Related Documentation
- [func policies() -> [Any]!](./policies%28%29.md)
  Returns an array of policies used to evaluate the status of the displayed certificate.
### Customizing the Appearance and Behavior of the View
- [func setDetailsDisclosed(Bool)](./setdetailsdisclosed%28_%29.md)
  Sets whether the certificate details subview is disclosed.
- [func setDisplayDetails(Bool)](./setdisplaydetails%28_%29.md)
  Specifies whether the user can see the certificate details.
- [func setDisplayTrust(Bool)](./setdisplaytrust%28_%29.md)
  Specifies whether the user can see the certificate’s trust settings.
- [func setEditableTrust(Bool)](./seteditabletrust%28_%29.md)
  Specifies whether the user can edit the certificate’s trust settings.
- [func setPoliciesDisclosed(Bool)](./setpoliciesdisclosed%28_%29.md)
  Specifies whether the trust policy settings subview is disclosed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificateview/setpolicies(_:))*