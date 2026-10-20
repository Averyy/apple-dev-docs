# keychain()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns the keychain created by the keychain save panel.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func keychain() -> Unmanaged<SecKeychain>!
```

```objc
- (SecKeychainRef) keychain;
```

## See Also

### Returning Information from the Sheet or Panel
- [func error() -> (any Error)!](./error%28%29.md)
  Returns the last error encountered by the keychain save panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsavepanel/keychain())*