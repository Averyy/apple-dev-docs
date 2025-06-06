# keychain

**Framework**: Security  
**Kind**: property

A reference to the keychain in which the event occurred. If the event did not involve a keychain, this field is not valid.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var keychain: Unmanaged<SecKeychain>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaincallbackinfo/keychain)*