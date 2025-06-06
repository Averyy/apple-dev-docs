# shared()

**Framework**: Network Extension  
**Kind**: method

Access the single instance of `NEVPNManager`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class func shared() -> NEVPNManager
```

#### Return Value

The `NEVPNManager` instance for the calling application.

## See Also

- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nevpnmanager/loadfrompreferences(completionhandler:).md)
  Load the VPN configuration from the Network Extension preferences.
- [func saveToPreferences(completionHandler: (((any Error)?) -> Void)?)](nevpnmanager/savetopreferences(completionhandler:).md)
  Save the VPN configuration in the Network Extension preferences.
- [func setAuthorization(AuthorizationRef)](nevpnmanager/setauthorization(_:).md)
- [func removeFromPreferences(completionHandler: (((any Error)?) -> Void)?)](nevpnmanager/removefrompreferences(completionhandler:).md)
  Remove the VPN configuration from the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/shared())*