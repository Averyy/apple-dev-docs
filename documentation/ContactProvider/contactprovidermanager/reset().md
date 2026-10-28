# reset()

**Framework**: ContactProvider  
**Kind**: method  
**Role**: Instance Method

Resets the extension domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func reset() async throws
```

## Discussion

You typically call this when you need to delete all previously-provided contacts for the domain. The next invocation of the app extension restarts content enumeration for the domain.

## See Also

### Managing the domain
- [var domain: any ContactProviderDomain](./domain.md)
  The domain that this instance manages.
- [func enable() async throws](./enable%28%29.md)
  Requests the person using the app to enable the extension domain.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the person using the app enabled the extension domain.
- [func disable() async throws](./disable%28%29.md)
  Disables the extension domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidermanager/reset())*