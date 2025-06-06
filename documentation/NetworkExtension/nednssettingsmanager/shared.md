# shared()

**Framework**: Network Extension  
**Kind**: method

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

#### Return Value

The DNS settings manager instance for the calling application.

## See Also

- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](nednssettingsmanager/loadfrompreferences(completionhandler:).md)
  Load your DNS settings configuration from the system networking preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](nednssettingsmanager/savetopreferences(completionhandler:).md)
  Save your DNS settings configuration to the system networking preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](nednssettingsmanager/removefrompreferences(completionhandler:).md)
  Remove your DNS settings configuration from the system networking preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nednssettingsmanager/shared())*