# GCControllerHomeButtonSettingsManager.Activity

**Framework**: Game Controller  
**Kind**: enum

A hint passed to `-openControllerHomeButtonSettingsForActivity:` that indicates the reason the app is requesting to open the Home button settings.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum Activity
```

## Topics

### Enumeration Cases
- [GCControllerHomeButtonSettingsManager.Activity.customizeAction](gccontrollerhomebuttonsettingsmanager/activity/customizeaction.md)
  Customize the action that occurs in response to long press of the Home button.
- [GCControllerHomeButtonSettingsManager.Activity.customizeOverrides](gccontrollerhomebuttonsettingsmanager/activity/customizeoverrides.md)
  Disable the system Home button actions while this app has focus.
### Initializers
- [init?(rawValue: Int)](gccontrollerhomebuttonsettingsmanager/activity/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerhomebuttonsettingsmanager/activity)*