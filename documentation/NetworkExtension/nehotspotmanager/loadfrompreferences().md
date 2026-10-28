# loadFromPreferences()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Loads the hotspot manager configuration from the Network Extension preferences.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
final func loadFromPreferences() async throws
```

## Discussion

If you haven’t previously saved a configuration with [`saveToPreferences()`](./savetopreferences%28%29.md), this call loads a default configuration.

This method throws [`NEHotspotManager.Error`](./error.md) value asynchronously on failure.

## See Also

### Managing the saved configuration
- [func saveToPreferences() async throws](./savetopreferences%28%29.md)
  Saves the HotspotManager configuration in the Network Extension preferences.
- [func removeFromPreferences() async throws](./removefrompreferences%28%29.md)
  Removes the hotspot manager configuration from the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotmanager/loadfrompreferences())*