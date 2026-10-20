# error()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns the last error encountered by the keychain save panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func error() -> (any Error)!
```

```objc
- (NSError *) error;
```

## See Also

### Returning Information from the Sheet or Panel
- [func keychain() -> Unmanaged<SecKeychain>!](./keychain%28%29.md)
  Returns the keychain created by the keychain save panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfkeychainsavepanel/error())*