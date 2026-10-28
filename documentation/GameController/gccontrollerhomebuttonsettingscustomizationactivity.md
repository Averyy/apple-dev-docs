# GCControllerHomeButtonSettingsCustomizationActivity

**Framework**: Game Controller  
**Kind**: enum  
**Role**: Enumeration

A hint passed to `-openControllerHomeButtonSettingsForActivity:` to indicate the reason the app is requesting to open Settings.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum GCControllerHomeButtonSettingsCustomizationActivity
```

```c
enum GCControllerHomeButtonSettingsCustomizationActivity : NSInteger;
```

## Overview

The system uses this hint to navigate to the appropriate screen in the Settings application.

## Topics

### Enumeration Cases
- [GCControllerHomeButtonSettingsCustomizationActivity.customizeInAppAction](./gccontrollerhomebuttonsettingscustomizationactivity/customizeinappaction.md)
  Customize the in-app action.
- [GCControllerHomeButtonSettingsCustomizationActivity.customizeSystemAction](./gccontrollerhomebuttonsettingscustomizationactivity/customizesystemaction.md)
  Customize the system action.
### Initializers
- [init?(rawValue: Int)](./gccontrollerhomebuttonsettingscustomizationactivity/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerhomebuttonsettingscustomizationactivity)*