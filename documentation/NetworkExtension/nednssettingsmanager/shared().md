# shared()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

Access the single instance of a DNS settings manager.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class func shared() -> NEDNSSettingsManager
```

```objc
+ (NEDNSSettingsManager *) sharedManager;
```

## Return Value

The DNS settings manager instance for the calling application.

## See Also

### Managing DNS configurations
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./loadfrompreferences%28completionhandler%29.md)
  Load your DNS settings configuration from the system networking preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](./savetopreferences%28completionhandler%29.md)
  Save your DNS settings configuration to the system networking preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](./removefrompreferences%28completionhandler%29.md)
  Remove your DNS settings configuration from the system networking preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettingsmanager/shared())*