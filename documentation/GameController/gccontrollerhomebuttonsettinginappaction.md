# GCControllerHomeButtonSettingInAppAction

**Framework**: Game Controller  
**Kind**: enum  
**Role**: Enumeration

How the system responds to a press of the game controller Home button while your application is front-most.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum GCControllerHomeButtonSettingInAppAction
```

```c
enum GCControllerHomeButtonSettingInAppAction : NSInteger;
```

## Topics

### Enumeration Cases
- [GCControllerHomeButtonSettingInAppAction.defer](./gccontrollerhomebuttonsettinginappaction/defer.md)
  The system defers its handling to your app’s preference.
- [GCControllerHomeButtonSettingInAppAction.disabled](./gccontrollerhomebuttonsettinginappaction/disabled.md)
  System response to the game controller Home button press is disabled.
- [GCControllerHomeButtonSettingInAppAction.systemDefault](./gccontrollerhomebuttonsettinginappaction/systemdefault.md)
  The system maintains its default handling regardless of your app’s preference.
- [GCControllerHomeButtonSettingInAppAction.unavailable](./gccontrollerhomebuttonsettinginappaction/unavailable.md)
  The setting value could not be retrieved.
### Initializers
- [init?(rawValue: Int)](./gccontrollerhomebuttonsettinginappaction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerhomebuttonsettinginappaction)*