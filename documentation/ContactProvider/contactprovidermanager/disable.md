# disable()

**Framework**: ContactProvider  
**Kind**: method

Disables the extension domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func disable() async throws
```

#### Discussion

Disabling the extension deletes all previously-provided contacts for the domain.

## See Also

- [var domain: any ContactProviderDomain](contactprovidermanager/domain.md)
  The domain that this instance manages.
- [func enable() async throws](contactprovidermanager/enable.md)
  Requests the person using the app to enable the extension domain.
- [var isEnabled: Bool](contactprovidermanager/isenabled.md)
  A Boolean value that indicates whether the person using the app enabled the extension domain.
- [func reset() async throws](contactprovidermanager/reset.md)
  Resets the extension domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidermanager/disable())*