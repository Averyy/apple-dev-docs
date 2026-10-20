# enable()

**Framework**: ContactProvider  
**Kind**: method  
**Role**: Instance Method

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

> **Throws**: `ContactProviderError.deniedByUser` if the person dismisses the prompt without enabling the extension domain.

## See Also

### Managing the domain
- [var domain: any ContactProviderDomain](./domain.md)
  The domain that this instance manages.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the person using the app enabled the extension domain.
- [func reset() async throws](./reset%28%29.md)
  Resets the extension domain.
- [func disable() async throws](./disable%28%29.md)
  Disables the extension domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidermanager/enable())*