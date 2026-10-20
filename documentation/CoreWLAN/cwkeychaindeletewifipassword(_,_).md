# CWKeychainDeleteWiFiPassword(_:_:)

**Framework**: Core WLAN  
**Kind**: func  
**Role**: Function

Deletes the password for the SSID and keychain domain you specify.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func CWKeychainDeleteWiFiPassword(_ domain: CWKeychainDomain, _ ssid: Data) -> OSStatus
```

```c
OSStatus CWKeychainDeleteWiFiPassword(CWKeychainDomain domain, NSData *ssid);
```

## See Also

### Functions
- [func CWKeychainCopyWiFiEAPIdentity(CWKeychainDomain, Data, UnsafeMutablePointer<Unmanaged<SecIdentity>?>?) -> OSStatus](./cwkeychaincopywifieapidentity%28_,_,_%29.md)
  Finds and returns the identity stored for the SSID and keychain domain you specify.
- [func CWKeychainDeleteWiFiEAPUsernameAndPassword(CWKeychainDomain, Data) -> OSStatus](./cwkeychaindeletewifieapusernameandpassword%28_,_%29.md)
  Deletes the 802.1X username and password for the SSID and keychain domain you specify.
- [func CWKeychainFindWiFiEAPUsernameAndPassword(CWKeychainDomain, Data, AutoreleasingUnsafeMutablePointer<NSString?>?, AutoreleasingUnsafeMutablePointer<NSString?>?) -> OSStatus](./cwkeychainfindwifieapusernameandpassword%28_,_,_,_%29.md)
  Finds and returns the 802.1X username and password stored for the SSID and keychain domain you specify.
- [func CWKeychainFindWiFiPassword(CWKeychainDomain, Data, AutoreleasingUnsafeMutablePointer<NSString?>?) -> OSStatus](./cwkeychainfindwifipassword%28_,_,_%29.md)
  Finds and returns, by reference, the password for the SSID and keychain domain you specify.
- [func CWKeychainSetWiFiEAPIdentity(CWKeychainDomain, Data, SecIdentity?) -> OSStatus](./cwkeychainsetwifieapidentity%28_,_,_%29.md)
  Associates an identity to the SSID and keychain domain you specify.
- [func CWKeychainSetWiFiEAPUsernameAndPassword(CWKeychainDomain, Data, String?, String?) -> OSStatus](./cwkeychainsetwifieapusernameandpassword%28_,_,_,_%29.md)
  Sets the 802.1X username and password for the SSID and keychain domain you specify.
- [func CWKeychainSetWiFiPassword(CWKeychainDomain, Data, String) -> OSStatus](./cwkeychainsetwifipassword%28_,_,_%29.md)
  Sets the Wi-Fi network keychain password for the SSID and keychain domain you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwkeychaindeletewifipassword(_:_:))*