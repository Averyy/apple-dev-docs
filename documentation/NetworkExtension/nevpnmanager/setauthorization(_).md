# setAuthorization(_:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.11+

## Declaration

```swift
func setAuthorization(_ authorization: AuthorizationRef)
```

```objc
- (void) setAuthorization:(AuthorizationRef) authorization;
```

## See Also

### Managing VPN configurations
- [class func shared() -> NEVPNManager](./shared%28%29.md)
  Access the single instance of `NEVPNManager`.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./loadfrompreferences%28completionhandler%29.md)
  Load the VPN configuration from the Network Extension preferences.
- [func saveToPreferences(completionHandler: (((any Error)?) -> Void)?)](./savetopreferences%28completionhandler%29.md)
  Save the VPN configuration in the Network Extension preferences.
- [func removeFromPreferences(completionHandler: (((any Error)?) -> Void)?)](./removefrompreferences%28completionhandler%29.md)
  Remove the VPN configuration from the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/setauthorization(_:))*