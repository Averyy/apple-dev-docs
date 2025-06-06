# keychain()

**Framework**: Security Interface  
**Kind**: method

Returns the keychain created by the keychain save panel.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func keychain() -> Unmanaged<SecKeychain>!
```

## See Also

- [func error() -> (any Error)!](sfkeychainsavepanel/error.md)
  Returns the last error encountered by the keychain save panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsavepanel/keychain())*