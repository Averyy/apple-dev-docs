# isEnabled

**Framework**: ContactProvider  
**Kind**: property

A Boolean value that indicates whether the person using the app enabled the extension domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var isEnabled: Bool { get }
```

## See Also

- [var domain: any ContactProviderDomain](contactprovidermanager/domain.md)
  The domain that this instance manages.
- [func enable() async throws](contactprovidermanager/enable.md)
  Requests the person using the app to enable the extension domain.
- [func reset() async throws](contactprovidermanager/reset.md)
  Resets the extension domain.
- [func disable() async throws](contactprovidermanager/disable.md)
  Disables the extension domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidermanager/isenabled)*