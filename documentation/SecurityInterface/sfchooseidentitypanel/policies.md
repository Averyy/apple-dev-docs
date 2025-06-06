# policies()

**Framework**: Security Interface  
**Kind**: method

Returns an array of policies used to evaluate the status of the displayed certificates.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func policies() -> [Any]!
```

#### Discussion

This method returns an autoreleased [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) containing one or more objects of type [`SecPolicy`](https://developer.apple.com/documentation/Security/SecPolicy) , as set by a previous [`setPolicies(_:)`](sfchooseidentitypanel/setpolicies(_:).md) call, or the Apple X.509 Basic Policy if [`setPolicies(_:)`](sfchooseidentitypanel/setpolicies(_:).md) has not been called. See [`Certificate, Key, and Trust Services`](https://developer.apple.com/documentation/Security/certificate-key-and-trust-services) in [`Certificate, Key, and Trust Services`](https://developer.apple.com/documentation/Security/certificate-key-and-trust-services) for a list of policies and object identifiers provided by the [`AppleX509TP Module`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/CDSA/CDSA.html#//apple_ref/doc/uid/TP40011172-CH4-CHDEEDBE).

## See Also

- [func setAlternateButtonTitle(String!)](sfchooseidentitypanel/setalternatebuttontitle(_:).md)
  Customizes the title of the alternate button.
- [func setDefaultButtonTitle(String!)](sfchooseidentitypanel/setdefaultbuttontitle(_:).md)
  Customizes the title of the default button.
- [func setPolicies(Any!)](sfchooseidentitypanel/setpolicies(_:).md)
  Specifies one or more policies that apply to the displayed certificates.
- [func informativeText() -> String!](sfchooseidentitypanel/informativetext.md)
  Returns the informative text currently displayed in the panel.
- [func setInformativeText(String!)](sfchooseidentitypanel/setinformativetext(_:).md)
  Sets the optional informative text displayed in the panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfchooseidentitypanel/policies())*