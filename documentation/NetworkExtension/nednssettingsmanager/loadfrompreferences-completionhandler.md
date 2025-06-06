# loadFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Load your DNS settings configuration from the system networking preferences.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func loadFromPreferences() async throws
```

#### Discussion

You must call this method at least once before calling [`saveToPreferences(completionHandler:)`](nednssettingsmanager/savetopreferences(completionhandler:).md) for the first time after your app launches.

## Parameters

- `completionHandler`: A block that takes an   object. This block runs on your application’s main thread after the load operation is complete. If an error occurs while loading the configuration, the block returns an   object.

## See Also

- [class func shared() -> NEDNSSettingsManager](nednssettingsmanager/shared.md)
  Access the single instance of a DNS settings manager.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](nednssettingsmanager/savetopreferences(completionhandler:).md)
  Save your DNS settings configuration to the system networking preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](nednssettingsmanager/removefrompreferences(completionhandler:).md)
  Remove your DNS settings configuration from the system networking preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettingsmanager/loadfrompreferences(completionhandler:))*