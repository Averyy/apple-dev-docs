# removeFromPreferences()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Removes the hotspot manager configuration from the Network Extension preferences.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
final func removeFromPreferences() async throws
```

## Discussion

This method throws [`NEHotspotManager.Error`](./error.md) value asynchronously on failure.

## See Also

### Managing the saved configuration
- [func loadFromPreferences() async throws](./loadfrompreferences%28%29.md)
  Loads the hotspot manager configuration from the Network Extension preferences.
- [func saveToPreferences() async throws](./savetopreferences%28%29.md)
  Saves the HotspotManager configuration in the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotmanager/removefrompreferences())*