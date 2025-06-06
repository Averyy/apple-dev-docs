# init(version:item:keychain:pid:)

**Framework**: Security  
**Kind**: init

Creates a new keychain callback information structure.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init(version: UInt32, item: Unmanaged<SecKeychainItem>, keychain: Unmanaged<SecKeychain>, pid: pid_t)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychaincallbackinfo/init(version:item:keychain:pid:))*