# GCControllerHomeButtonSettingCustomizationStatus

**Framework**: Game Controller  
**Kind**: enum  
**Role**: Enumeration

An additional returned flag indicating whether a setting has been modified by the user.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum GCControllerHomeButtonSettingCustomizationStatus
```

```c
enum GCControllerHomeButtonSettingCustomizationStatus : NSInteger;
```

## Topics

### Enumeration Cases
- [GCControllerHomeButtonSettingCustomizationStatus.systemDefault](./gccontrollerhomebuttonsettingcustomizationstatus/systemdefault.md)
  The user has not customized this setting.
- [GCControllerHomeButtonSettingCustomizationStatus.user](./gccontrollerhomebuttonsettingcustomizationstatus/user.md)
  The user has customized this setting at least once.
### Initializers
- [init?(rawValue: Int)](./gccontrollerhomebuttonsettingcustomizationstatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerhomebuttonsettingcustomizationstatus)*