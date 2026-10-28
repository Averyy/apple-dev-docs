# loadFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Load the VPN configuration from the Network Extension preferences.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func loadFromPreferences(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func loadFromPreferences() async throws
```

```objc
- (void) loadFromPreferencesWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

You must call this method at least once before calling `saveToPreferencesWithCompletionHandler:` for the first time after your app launches.

## Parameters

- `completionHandler`: A block that takes an [`NSError`](../../Foundation/nserror.md) object. This block will be executed on the caller’s main thread after the load operation is complete. If the configuration does not exist in the preferences or is loaded successfully, the error parameter will be nil. If an error occurred while loading the configuration, the error parameter will be set to an `NSError` object containing details about the error. See `NEVPN Errors` for a list of possible errors.

## See Also

### Managing VPN configurations
- [class func shared() -> NEVPNManager](./shared%28%29.md)
  Access the single instance of `NEVPNManager`.
- [func saveToPreferences(completionHandler: (((any Error)?) -> Void)?)](./savetopreferences%28completionhandler%29.md)
  Save the VPN configuration in the Network Extension preferences.
- [func setAuthorization(AuthorizationRef)](./setauthorization%28_%29.md)
- [func removeFromPreferences(completionHandler: (((any Error)?) -> Void)?)](./removefrompreferences%28completionhandler%29.md)
  Remove the VPN configuration from the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnmanager/loadfrompreferences(completionhandler:))*