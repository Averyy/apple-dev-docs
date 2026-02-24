# loadAllFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Read all of the VPN configurations created by the calling app that have previously been saved to the Network Extension preferences.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class func loadAllFromPreferences() async throws -> [NETunnelProviderManager]
```

## Parameters

- `completionHandler`: A block that takes an [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) of `NETunnelProviderManager` objects, and an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object. This block will be executed on the caller’s main thread after the load operation is complete. If no configurations exist for the calling app then the `managers` parameter will be set to nil and the error parameter will be set to nil. If an error occurred while loading the configurations, the error parameter will be set to an NSError object containing details about the error. See [`NEVPNManager`](nevpnmanager.md) for a list of possible errors.

## See Also

- [func copyAppRules() -> [NEAppRule]?](netunnelprovidermanager/copyapprules.md)
  Returns a copy of the app rules currently set in the configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager/loadallfrompreferences(completionhandler:))*