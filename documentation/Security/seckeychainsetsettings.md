# SecKeychainSetSettings(_:_:)

**Framework**: Security  
**Kind**: func

Changes the settings of a keychain.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecKeychainSetSettings(_ keychain: SecKeychain?, _ newSettings: UnsafePointer<SecKeychainSettings>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `keychain`: A reference to a keychain whose settings you wish to change. Pass   to change the settings of the default keychain.
- `newSettings`: A pointer to a keychain settings structure that defines whether the keychain locks when sleeping, or locks after a set time period of inactivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainsetsettings(_:_:))*