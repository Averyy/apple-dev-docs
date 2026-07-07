# GCControllerHomeButtonSettingSystemAction

**Framework**: Game Controller  
**Kind**: enum

How the system responds to a press of the game controller Home button outside of contexts where an action of the front-most app takes priority.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum GCControllerHomeButtonSettingSystemAction
```

## Topics

### Enumeration Cases
- [GCControllerHomeButtonSettingSystemAction.disabled](gccontrollerhomebuttonsettingsystemaction/disabled.md)
  System response to the game controller Home button press is disabled.
- [GCControllerHomeButtonSettingSystemAction.openCurrentApplication](gccontrollerhomebuttonsettingsystemaction/opencurrentapplication.md)
  The controller home button system action opens the current application.
- [GCControllerHomeButtonSettingSystemAction.other](gccontrollerhomebuttonsettingsystemaction/other.md)
  The controller home button system action performs some other action.
- [GCControllerHomeButtonSettingSystemAction.unavailable](gccontrollerhomebuttonsettingsystemaction/unavailable.md)
  The setting value could not be retrieved.
### Initializers
- [init?(rawValue: Int)](gccontrollerhomebuttonsettingsystemaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerhomebuttonsettingsystemaction)*