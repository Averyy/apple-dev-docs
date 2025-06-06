# saveToPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Save your DNS settings configuration to the system networking preferences.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func saveToPreferences() async throws
```

#### Discussion

You must call [`loadFromPreferences(completionHandler:)`](nednssettingsmanager/loadfrompreferences(completionhandler:).md) at least once before calling this method the first time after your app launches.

## Parameters

- `completionHandler`: An optional block that takes an   object. If specified, this block runs on your application’s main thread after the save operation completes. If an error occurs while saving the configuration, the block returns an   object.

## See Also

- [class func shared() -> NEDNSSettingsManager](nednssettingsmanager/shared.md)
  Access the single instance of a DNS settings manager.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nednssettingsmanager/loadfrompreferences(completionhandler:).md)
  Load your DNS settings configuration from the system networking preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](nednssettingsmanager/removefrompreferences(completionhandler:).md)
  Remove your DNS settings configuration from the system networking preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettingsmanager/savetopreferences(completionhandler:))*