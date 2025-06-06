# setAuthorization(_:)

**Framework**: Network Extension  
**Kind**: method

**Availability**:
- macOS 10.11+

## Declaration

```swift
func setAuthorization(_ authorization: AuthorizationRef)
```

## See Also

- [class func shared() -> NEVPNManager](nevpnmanager/shared.md)
  Access the single instance of `NEVPNManager`.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nevpnmanager/loadfrompreferences(completionhandler:).md)
  Load the VPN configuration from the Network Extension preferences.
- [func saveToPreferences(completionHandler: (((any Error)?) -> Void)?)](nevpnmanager/savetopreferences(completionhandler:).md)
  Save the VPN configuration in the Network Extension preferences.
- [func removeFromPreferences(completionHandler: (((any Error)?) -> Void)?)](nevpnmanager/removefrompreferences(completionhandler:).md)
  Remove the VPN configuration from the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/setauthorization(_:))*