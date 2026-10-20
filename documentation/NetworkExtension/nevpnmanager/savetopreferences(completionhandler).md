# saveToPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

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
func saveToPreferences(completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func saveToPreferences() async throws
```

```objc
- (void) saveToPreferencesWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

#### Discussion

You must call [`loadFromPreferences(completionHandler:)`](./loadfrompreferences%28completionhandler%29.md): at least once before calling this method the first time after your app launches.

## Parameters

- `completionHandler`: An optional block that takes an [`NSError`](../../Foundation/nserror.md) object. If specified, this block will be executed on the caller’s main thread after the save operation is complete. If the configuration could not be saved to the preferences, the error parameter will be set to an `NSError` object containing details about the error. See `NEVPN Errors` for a list of possible errors. If the configuration is saved successfully then the error parameter will be set to nil.

## See Also

### Related Documentation
- [class NEVPNManager](../nevpnmanager.md)
  An object to create and manage a Personal VPN configuration.
### Managing VPN configurations
- [class func shared() -> NEVPNManager](./shared%28%29.md)
  Access the single instance of `NEVPNManager`.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./loadfrompreferences%28completionhandler%29.md)
  Load the VPN configuration from the Network Extension preferences.
- [func setAuthorization(AuthorizationRef)](./setauthorization%28_%29.md)
- [func removeFromPreferences(completionHandler: (((any Error)?) -> Void)?)](./removefrompreferences%28completionhandler%29.md)
  Remove the VPN configuration from the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/savetopreferences(completionhandler:))*