# enable()

**Framework**: ContactProvider  
**Kind**: method

Requests the person using the app to enable the extension domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func enable() async throws
```

#### Discussion

If necessary, this call waits for the person using the app to explicitly approve or deny using the extension domain.

> **Note**: `ContactProviderError.deniedByUser` if the person dismisses the prompt without enabling the extension domain.

`ContactProviderError.deniedByUser` if the person dismisses the prompt without enabling the extension domain.

## See Also

- [var domain: any ContactProviderDomain](contactprovidermanager/domain.md)
  The domain that this instance manages.
- [var isEnabled: Bool](contactprovidermanager/isenabled.md)
  A Boolean value that indicates whether the person using the app enabled the extension domain.
- [func reset() async throws](contactprovidermanager/reset.md)
  Resets the extension domain.
- [func disable() async throws](contactprovidermanager/disable.md)
  Disables the extension domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidermanager/enable())*