# GCControllerHomeButtonSettingsCustomizationActivity

**Framework**: Game Controller  
**Kind**: enum

A hint passed to `-openControllerHomeButtonSettingsForActivity:` to indicate the reason the app is requesting to open Settings.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum GCControllerHomeButtonSettingsCustomizationActivity
```

#### Overview

The system uses this hint to navigate to the appropriate screen in the Settings application.

## Topics

### Enumeration Cases
- [GCControllerHomeButtonSettingsCustomizationActivity.customizeInAppAction](gccontrollerhomebuttonsettingscustomizationactivity/customizeinappaction.md)
  Customize the in-app action.
- [GCControllerHomeButtonSettingsCustomizationActivity.customizeSystemAction](gccontrollerhomebuttonsettingscustomizationactivity/customizesystemaction.md)
  Customize the system action.
### Initializers
- [init?(rawValue: Int)](gccontrollerhomebuttonsettingscustomizationactivity/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerhomebuttonsettingscustomizationactivity)*