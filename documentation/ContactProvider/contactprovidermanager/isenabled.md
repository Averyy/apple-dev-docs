# isEnabled

**Framework**: ContactProvider  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the person using the app enabled the extension domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var isEnabled: Bool { get }
```

## See Also

### Managing the domain
- [var domain: any ContactProviderDomain](./domain.md)
  The domain that this instance manages.
- [func enable() async throws](./enable%28%29.md)
  Requests the person using the app to enable the extension domain.
- [func reset() async throws](./reset%28%29.md)
  Resets the extension domain.
- [func disable() async throws](./disable%28%29.md)
  Disables the extension domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidermanager/isenabled)*