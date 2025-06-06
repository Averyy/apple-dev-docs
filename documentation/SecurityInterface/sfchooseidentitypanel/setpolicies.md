# setPolicies(_:)

**Framework**: Security Interface  
**Kind**: method

Specifies one or more policies that apply to the displayed certificates.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func setPolicies(_ policies: Any!)
```

#### Discussion

The [`SFChooseIdentityPanel`](sfchooseidentitypanel.md) class evaluates trust for the certificates it displays. Applications typically display certificates in the context of a specific use, such as SSL or S/MIME. You should set only the policy references that apply to your intended use. See [`Certificate, Key, and Trust Services`](https://developer.apple.com/documentation/Security/certificate-key-and-trust-services) for a list of policies and object identifiers provided by the [`AppleX509TP Module`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/CDSA/CDSA.html#//apple_ref/doc/uid/TP40011172-CH4-CHDEEDBE).

## Parameters

- `policies`: The policies to use when evaluating the certificates’ status. You can pass either a   object or an   (containing one or more   instances) in this parameter. If   is set to  , the Apple X.509 Basic Policy is used.

## See Also

- [func setAlternateButtonTitle(String!)](sfchooseidentitypanel/setalternatebuttontitle(_:).md)
  Customizes the title of the alternate button.
- [func setDefaultButtonTitle(String!)](sfchooseidentitypanel/setdefaultbuttontitle(_:).md)
  Customizes the title of the default button.
- [func policies() -> [Any]!](sfchooseidentitypanel/policies.md)
  Returns an array of policies used to evaluate the status of the displayed certificates.
- [func informativeText() -> String!](sfchooseidentitypanel/informativetext.md)
  Returns the informative text currently displayed in the panel.
- [func setInformativeText(String!)](sfchooseidentitypanel/setinformativetext(_:).md)
  Sets the optional informative text displayed in the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel/setpolicies(_:))*