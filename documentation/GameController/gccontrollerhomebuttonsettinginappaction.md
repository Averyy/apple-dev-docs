# GCControllerHomeButtonSettingInAppAction

**Framework**: Game Controller  
**Kind**: enum

How the system responds to a press of the game controller Home button while your application is front-most.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum GCControllerHomeButtonSettingInAppAction
```

## Topics

### Enumeration Cases
- [GCControllerHomeButtonSettingInAppAction.defer](gccontrollerhomebuttonsettinginappaction/defer.md)
  The system defers its handling to your app’s preference.
- [GCControllerHomeButtonSettingInAppAction.disabled](gccontrollerhomebuttonsettinginappaction/disabled.md)
  System response to the game controller Home button press is disabled.
- [GCControllerHomeButtonSettingInAppAction.systemDefault](gccontrollerhomebuttonsettinginappaction/systemdefault.md)
  The system maintains its default handling regardless of your app’s preference.
- [GCControllerHomeButtonSettingInAppAction.unavailable](gccontrollerhomebuttonsettinginappaction/unavailable.md)
  The setting value could not be retrieved.
### Initializers
- [init?(rawValue: Int)](gccontrollerhomebuttonsettinginappaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerhomebuttonsettinginappaction)*