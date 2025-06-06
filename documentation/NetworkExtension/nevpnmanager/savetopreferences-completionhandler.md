# saveToPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Save the VPN configuration in the Network Extension preferences.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func saveToPreferences() async throws
```

#### Discussion

You must call [`loadFromPreferences(completionHandler:)`](nevpnmanager/loadfrompreferences(completionhandler:).md): at least once before calling this method the first time after your app launches.

## Parameters

- `completionHandler`: An optional block that takes an   object. If specified, this block will be executed on the caller’s main thread after the save operation is complete. If the configuration could not be saved to the preferences, the error parameter will be set to an   object containing details about the error. See   for a list of possible errors. If the configuration is saved successfully then the error parameter will be set to nil.

## See Also

- [class NEVPNManager](nevpnmanager.md)
  An object to create and manage a Personal VPN configuration.
- [class func shared() -> NEVPNManager](nevpnmanager/shared.md)
  Access the single instance of `NEVPNManager`.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nevpnmanager/loadfrompreferences(completionhandler:).md)
  Load the VPN configuration from the Network Extension preferences.
- [func setAuthorization(AuthorizationRef)](nevpnmanager/setauthorization(_:).md)
- [func removeFromPreferences(completionHandler: (((any Error)?) -> Void)?)](nevpnmanager/removefrompreferences(completionhandler:).md)
  Remove the VPN configuration from the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/savetopreferences(completionhandler:))*