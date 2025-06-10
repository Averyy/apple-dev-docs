# saveToPreferences()

**Framework**: Network Extension  
**Kind**: method

Saves the HotspotManager configuration in the Network Extension preferences.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func saveToPreferences() async throws
```

#### Discussion

Only call this method after previously calling [`loadFromPreferences()`](nehotspotmanager/loadfrompreferences().md) to load the configuration.

This method throws [`NEHotspotManager.Error`](nehotspotmanager/error.md) value asynchronously on failure.

## See Also

- [func loadFromPreferences() async throws](nehotspotmanager/loadfrompreferences.md)
  Loads the hotspot manager configuration from the Network Extension preferences.
- [func removeFromPreferences() async throws](nehotspotmanager/removefrompreferences.md)
  Removes the hotspot manager configuration from the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotmanager/savetopreferences())*