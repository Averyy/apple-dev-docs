# loadFromPreferences()

**Framework**: Network Extension  
**Kind**: method

Loads the hotspot manager configuration from the Network Extension preferences.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func loadFromPreferences() async throws
```

#### Discussion

If you haven’t previously saved a configuration with [`saveToPreferences()`](nehotspotmanager/savetopreferences().md), this call loads a default configuration.

This method throws [`NEHotspotManager.Error`](nehotspotmanager/error.md) value asynchronously on failure.

## See Also

- [func saveToPreferences() async throws](nehotspotmanager/savetopreferences.md)
  Saves the HotspotManager configuration in the Network Extension preferences.
- [func removeFromPreferences() async throws](nehotspotmanager/removefrompreferences.md)
  Removes the hotspot manager configuration from the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotmanager/loadfrompreferences())*