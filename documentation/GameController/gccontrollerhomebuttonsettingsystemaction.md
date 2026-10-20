# GCControllerHomeButtonSettingSystemAction

**Framework**: Game Controller  
**Kind**: enum  
**Role**: Enumeration

How the system responds to a press of the game controller Home button outside of contexts where an action of the front-most app takes priority.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum GCControllerHomeButtonSettingSystemAction
```

```c
enum GCControllerHomeButtonSettingSystemAction : NSInteger;
```

## Topics

### Enumeration Cases
- [GCControllerHomeButtonSettingSystemAction.disabled](./gccontrollerhomebuttonsettingsystemaction/disabled.md)
  System response to the game controller Home button press is disabled.
- [GCControllerHomeButtonSettingSystemAction.openCurrentApplication](./gccontrollerhomebuttonsettingsystemaction/opencurrentapplication.md)
  The controller home button system action opens the current application.
- [GCControllerHomeButtonSettingSystemAction.other](./gccontrollerhomebuttonsettingsystemaction/other.md)
  The controller home button system action performs some other action.
- [GCControllerHomeButtonSettingSystemAction.unavailable](./gccontrollerhomebuttonsettingsystemaction/unavailable.md)
  The setting value could not be retrieved.
### Initializers
- [init?(rawValue: Int)](./gccontrollerhomebuttonsettingsystemaction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerhomebuttonsettingsystemaction)*