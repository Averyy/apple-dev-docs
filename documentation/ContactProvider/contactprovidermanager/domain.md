# domain

**Framework**: ContactProvider  
**Kind**: property

The domain that this instance manages.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var domain: any ContactProviderDomain { get }
```

#### Discussion

This value defaults to [`DefaultContactProviderDomain`](defaultcontactproviderdomain.md).

## See Also

- [func enable() async throws](contactprovidermanager/enable.md)
  Requests the person using the app to enable the extension domain.
- [var isEnabled: Bool](contactprovidermanager/isenabled.md)
  A Boolean value that indicates whether the person using the app enabled the extension domain.
- [func reset() async throws](contactprovidermanager/reset.md)
  Resets the extension domain.
- [func disable() async throws](contactprovidermanager/disable.md)
  Disables the extension domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidermanager/domain)*