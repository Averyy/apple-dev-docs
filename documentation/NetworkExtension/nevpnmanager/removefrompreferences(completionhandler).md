# removeFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

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
func removeFromPreferences(completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func removeFromPreferences() async throws
```

```objc
- (void) removeFromPreferencesWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

After the configuration is removed from the preferences the `NEVPNManager` object will still contain the configuration parameters. Calling [`loadFromPreferences(completionHandler:)`](./loadfrompreferences%28completionhandler%29.md): will clear out the configuration parameters from the `NEVPNManager` object.

## Parameters

- `completionHandler`: An optional block that takes an [`NSError`](../../Foundation/nserror.md) object. If specified, this block will be executed on the caller’s main thread after the removal operation is complete. If the configuration does not exist or an error occurs while removing it, the error parameter will be set to an `NSError` object containing details about the error. See `NEVPN Errors` for a list of possible errors. If the configuration is removed successfully then the error parameter will be set to nil.

## See Also

### Managing VPN configurations
- [class func shared() -> NEVPNManager](./shared%28%29.md)
  Access the single instance of `NEVPNManager`.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./loadfrompreferences%28completionhandler%29.md)
  Load the VPN configuration from the Network Extension preferences.
- [func saveToPreferences(completionHandler: (((any Error)?) -> Void)?)](./savetopreferences%28completionhandler%29.md)
  Save the VPN configuration in the Network Extension preferences.
- [func setAuthorization(AuthorizationRef)](./setauthorization%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/removefrompreferences(completionhandler:))*