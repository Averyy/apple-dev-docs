# removeFromPreferences(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Remove your DNS settings configuration from the system networking preferences.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func removeFromPreferences() async throws
```

#### Discussion

After you remove your configuration, the `NEDNSSettingsManager` object still contains the configuration parameters. Calling [`loadFromPreferences(completionHandler:)`](nednssettingsmanager/loadfrompreferences(completionhandler:).md) clears out the configuration parameters from the `NEDNSSettingsManager` object.

## Parameters

- `completionHandler`: An optional block that takes an   object. If specified, this block runs on your application’s main thread after your configuration is removed. If an error occurs while removing the configuration, the block returns an   object.

## See Also

- [class func shared() -> NEDNSSettingsManager](nednssettingsmanager/shared.md)
  Access the single instance of a DNS settings manager.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nednssettingsmanager/loadfrompreferences(completionhandler:).md)
  Load your DNS settings configuration from the system networking preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](nednssettingsmanager/savetopreferences(completionhandler:).md)
  Save your DNS settings configuration to the system networking preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettingsmanager/removefrompreferences(completionhandler:))*