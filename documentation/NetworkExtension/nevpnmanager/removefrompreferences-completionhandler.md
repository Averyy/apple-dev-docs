# removeFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Remove the VPN configuration from the Network Extension preferences.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func removeFromPreferences() async throws
```

#### Discussion

After the configuration is removed from the preferences the `NEVPNManager` object will still contain the configuration parameters. Calling [`loadFromPreferences(completionHandler:)`](nevpnmanager/loadfrompreferences(completionhandler:).md): will clear out the configuration parameters from the `NEVPNManager` object.

## Parameters

- `completionHandler`: An optional block that takes an   object. If specified, this block will be executed on the caller’s main thread after the removal operation is complete. If the configuration does not exist or an error occurs while removing it, the error parameter will be set to an   object containing details about the error. See   for a list of possible errors. If the configuration is removed successfully then the error parameter will be set to nil.

## See Also

- [class func shared() -> NEVPNManager](nevpnmanager/shared.md)
  Access the single instance of `NEVPNManager`.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nevpnmanager/loadfrompreferences(completionhandler:).md)
  Load the VPN configuration from the Network Extension preferences.
- [func saveToPreferences(completionHandler: (((any Error)?) -> Void)?)](nevpnmanager/savetopreferences(completionhandler:).md)
  Save the VPN configuration in the Network Extension preferences.
- [func setAuthorization(AuthorizationRef)](nevpnmanager/setauthorization(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/removefrompreferences(completionhandler:))*