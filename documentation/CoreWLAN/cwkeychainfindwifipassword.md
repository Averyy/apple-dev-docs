# CWKeychainFindWiFiPassword(_:_:_:)

**Framework**: Core WLAN  
**Kind**: func

Finds and returns, by reference, the password for the SSID and keychain domain you specify.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func CWKeychainFindWiFiPassword(_ domain: CWKeychainDomain, _ ssid: Data, _ password: AutoreleasingUnsafeMutablePointer<NSString?>?) -> OSStatus
```

## See Also

- [func CWKeychainCopyWiFiEAPIdentity(CWKeychainDomain, Data, UnsafeMutablePointer<Unmanaged<SecIdentity>?>?) -> OSStatus](cwkeychaincopywifieapidentity(_:_:_:).md)
  Finds and returns the identity stored for the SSID and keychain domain you specify.
- [func CWKeychainDeleteWiFiEAPUsernameAndPassword(CWKeychainDomain, Data) -> OSStatus](cwkeychaindeletewifieapusernameandpassword(_:_:).md)
  Deletes the 802.1X username and password for the SSID and keychain domain you specify.
- [func CWKeychainDeleteWiFiPassword(CWKeychainDomain, Data) -> OSStatus](cwkeychaindeletewifipassword(_:_:).md)
  Deletes the password for the SSID and keychain domain you specify.
- [func CWKeychainFindWiFiEAPUsernameAndPassword(CWKeychainDomain, Data, AutoreleasingUnsafeMutablePointer<NSString?>?, AutoreleasingUnsafeMutablePointer<NSString?>?) -> OSStatus](cwkeychainfindwifieapusernameandpassword(_:_:_:_:).md)
  Finds and returns the 802.1X username and password stored for the SSID and keychain domain you specify.
- [func CWKeychainSetWiFiEAPIdentity(CWKeychainDomain, Data, SecIdentity?) -> OSStatus](cwkeychainsetwifieapidentity(_:_:_:).md)
  Associates an identity to the SSID and keychain domain you specify.
- [func CWKeychainSetWiFiEAPUsernameAndPassword(CWKeychainDomain, Data, String?, String?) -> OSStatus](cwkeychainsetwifieapusernameandpassword(_:_:_:_:).md)
  Sets the 802.1X username and password for the SSID and keychain domain you specify.
- [func CWKeychainSetWiFiPassword(CWKeychainDomain, Data, String) -> OSStatus](cwkeychainsetwifipassword(_:_:_:).md)
  Sets the Wi-Fi network keychain password for the SSID and keychain domain you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwkeychainfindwifipassword(_:_:_:))*