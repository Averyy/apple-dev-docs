# reset()

**Framework**: ContactProvider  
**Kind**: method

Resets the extension domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func reset() async throws
```

#### Discussion

You typically call this when you need to delete all previously-provided contacts for the domain. The next invocation of the app extension restarts content enumeration for the domain.

## See Also

- [var domain: any ContactProviderDomain](contactprovidermanager/domain.md)
  The domain that this instance manages.
- [func enable() async throws](contactprovidermanager/enable.md)
  Requests the person using the app to enable the extension domain.
- [var isEnabled: Bool](contactprovidermanager/isenabled.md)
  A Boolean value that indicates whether the person using the app enabled the extension domain.
- [func disable() async throws](contactprovidermanager/disable.md)
  Disables the extension domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidermanager/reset())*