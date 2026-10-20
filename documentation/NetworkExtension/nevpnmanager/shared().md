# shared()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NEVPNManager *) sharedManager;
```

#### Return Value

The `NEVPNManager` instance for the calling application.

## See Also

### Managing VPN configurations
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./loadfrompreferences%28completionhandler%29.md)
  Load the VPN configuration from the Network Extension preferences.
- [func saveToPreferences(completionHandler: (((any Error)?) -> Void)?)](./savetopreferences%28completionhandler%29.md)
  Save the VPN configuration in the Network Extension preferences.
- [func setAuthorization(AuthorizationRef)](./setauthorization%28_%29.md)
- [func removeFromPreferences(completionHandler: (((any Error)?) -> Void)?)](./removefrompreferences%28completionhandler%29.md)
  Remove the VPN configuration from the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/shared())*