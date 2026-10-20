# domain

**Framework**: ContactProvider  
**Kind**: property  
**Role**: Instance Property

The domain that this instance manages.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var domain: any ContactProviderDomain { get }
```

#### Discussion

This value defaults to [`DefaultContactProviderDomain`](../defaultcontactproviderdomain.md).

## See Also

### Managing the domain
- [func enable() async throws](./enable%28%29.md)
  Requests the person using the app to enable the extension domain.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the person using the app enabled the extension domain.
- [func reset() async throws](./reset%28%29.md)
  Resets the extension domain.
- [func disable() async throws](./disable%28%29.md)
  Disables the extension domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidermanager/domain)*