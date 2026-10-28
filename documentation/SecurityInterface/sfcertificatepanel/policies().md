# policies()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns an array of policies used to evaluate the status of the displayed certificates.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func policies() -> [Any]!
```

```objc
- (NSArray *) policies;
```

## Discussion

This method returns an autoreleased [`NSArray`](../../Foundation/nsarray.md) containing one or more objects of type [`SecPolicy`](../../Security/secpolicy.md), as set by a previous [`setPolicies(_:)`](./setpolicies%28_%29.md) call, or the Apple X.509 Basic Policy if [`setPolicies(_:)`](./setpolicies%28_%29.md) has not been called. See [Certificate, Key, and Trust Services](../../Security/certificate-key-and-trust-services.md) in [Certificate, Key, and Trust Services](../../Security/certificate-key-and-trust-services.md) for a list of policies and object identifiers provided by the [AppleX509TP Module](https://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/CDSA/CDSA.html#//apple_ref/doc/uid/TP40011172-CH4-CHDEEDBE).

## See Also

### Customizing the Appearance of the Sheet or Panel
- [func setAlternateButtonTitle(String!)](./setalternatebuttontitle%28_%29.md)
  Customizes the title of the alternate button.
- [func setDefaultButtonTitle(String!)](./setdefaultbuttontitle%28_%29.md)
  Customizes the title of the default button.
- [func setPolicies(Any!)](./setpolicies%28_%29.md)
  Specifies one or more policies that apply to the displayed certificates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel/policies())*