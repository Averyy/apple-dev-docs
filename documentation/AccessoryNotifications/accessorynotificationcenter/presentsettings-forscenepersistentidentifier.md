# presentSettings(for:scenePersistentIdentifier:)

**Framework**: Accessory Notifications  
**Kind**: method

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
func presentSettings(for accessory: ASAccessory, scenePersistentIdentifier: String? = nil) async throws -> ForwardingDecision
```

## Parameters

- `scenePersistentIdentifier`: The `persistentIdentifier` of the specific `UISceneSession` from the target app associated with the presentation, if available


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorynotifications/accessorynotificationcenter/presentsettings(for:scenepersistentidentifier:))*