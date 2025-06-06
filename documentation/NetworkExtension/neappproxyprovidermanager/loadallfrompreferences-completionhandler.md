# loadAllFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Load all of the App Proxy configurations associated with the calling app that have previously been saved to the Network Extension preferences.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class func loadAllFromPreferences() async throws -> [NEAppProxyProviderManager]
```

## Parameters

- `completionHandler`: A block that takes an   of   objects, and an   object. This block will be executed on the caller’s main thread after the load operation is complete. If no configurations exist for the calling app then the   parameter will be set to nil and the error parameter will be set to nil. If an error occurred while loading the configurations, the error parameter will be set to an   object containing details about the error. See NEVPNError in   for a list of possible errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyprovidermanager/loadallfrompreferences(completionhandler:))*