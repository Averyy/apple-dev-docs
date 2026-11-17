# CPInstrumentClusterSetting

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate when to include or exclude vehicle-related data in your custom content.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
enum CPInstrumentClusterSetting
```

```c
enum CPInstrumentClusterSetting : NSUInteger;
```

## Overview

In an instrument cluster interface, the vehicle’s system can ask your app to display specific types of information with navigation or other app-specific content. For example, the vehicle can ask you to display the current compass heading or speed limits for the current road. Use these settings to determine when to include or exclude information from your interface.

## Topics

### Getting the instrument cluster settings
- [CPInstrumentClusterSetting.disabled](./cpinstrumentclustersetting/disabled.md)
  An option to disable the specified setting.
- [CPInstrumentClusterSetting.enabled](./cpinstrumentclustersetting/enabled.md)
  An option to enable the specified setting.
- [CPInstrumentClusterSetting.unspecified](./cpinstrumentclustersetting/unspecified.md)
  An option that represents no configured value.
- [CPInstrumentClusterSetting.userPreference](./cpinstrumentclustersetting/userpreference.md)
  An option to enable the setting according to personal preferences your app manages.
### Initializers
- [init?(rawValue: UInt)](./cpinstrumentclustersetting/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Instrument cluster display
- [class CPTemplateApplicationInstrumentClusterScene](./cptemplateapplicationinstrumentclusterscene.md)
  A CarPlay scene that presents navigation-related instructions in the vehicle’s instrument display.
- [protocol CPTemplateApplicationInstrumentClusterSceneDelegate](./cptemplateapplicationinstrumentclusterscenedelegate.md)
  The methods for responding to the life cycle events in your app’s instrument cluster scene.
- [class CPInstrumentClusterController](./cpinstrumentclustercontroller.md)
  The controller you use to configure and manage your instrument cluster interface.
- [protocol CPInstrumentClusterControllerDelegate](./cpinstrumentclustercontrollerdelegate.md)
  The methods for responding to changes to instrument cluster settings.
- [CPSupportsInstrumentClusterNavigationScene](../BundleResources/information-property-list/uiapplicationscenemanifest/cpsupportsinstrumentclusternavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Instrument Cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinstrumentclustersetting)*