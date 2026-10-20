# setPolicies(_:)

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Specifies one or more policies that apply to the displayed certificates.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func setPolicies(_ policies: Any!)
```

```objc
- (void) setPolicies:(id) policies;
```

#### Discussion

The [`SFChooseIdentityPanel`](../sfchooseidentitypanel.md) class evaluates trust for the certificates it displays. Applications typically display certificates in the context of a specific use, such as SSL or S/MIME. You should set only the policy references that apply to your intended use. See [Certificate, Key, and Trust Services](../../Security/certificate-key-and-trust-services.md) for a list of policies and object identifiers provided by the [AppleX509TP Module](https://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/CDSA/CDSA.html#//apple_ref/doc/uid/TP40011172-CH4-CHDEEDBE).

## Parameters

- `policies`: The policies to use when evaluating the certificates’ status. You can pass either a [`SecPolicy`](../../Security/secpolicy.md) object or an [`NSArray`](../../Foundation/nsarray.md) (containing one or more [`SecPolicy`](../../Security/secpolicy.md) instances) in this parameter. If `policies` is set to `nil`, the Apple X.509 Basic Policy is used.

## See Also

### Customizing the Appearance of the Sheet or Panel
- [func setAlternateButtonTitle(String!)](./setalternatebuttontitle%28_%29.md)
  Customizes the title of the alternate button.
- [func setDefaultButtonTitle(String!)](./setdefaultbuttontitle%28_%29.md)
  Customizes the title of the default button.
- [func policies() -> [Any]!](./policies%28%29.md)
  Returns an array of policies used to evaluate the status of the displayed certificates.
- [func informativeText() -> String!](./informativetext%28%29.md)
  Returns the informative text currently displayed in the panel.
- [func setInformativeText(String!)](./setinformativetext%28_%29.md)
  Sets the optional informative text displayed in the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel/setpolicies(_:))*