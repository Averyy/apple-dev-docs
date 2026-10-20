# UISceneConfigurations

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

The default configuration details the system uses to create new scenes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Details

- **Name**: `UISceneConfigurations` (Scene Configuration)
- **Type**: dictionary

#### Discussion

The keys in the dictionary correspond to the roles played by your scenes.

[`UISceneConfigurations`](./uisceneconfigurations.md) supports the following keys:

- [`UIWindowSceneSessionRoleApplication`](./uisceneconfigurations/uiwindowscenesessionroleapplication.md)
- [`UIWindowSceneSessionRoleExternalDisplayNonInteractive`](./uisceneconfigurations/uiwindowscenesessionroleexternaldisplaynoninteractive.md)

For visionOS apps, it also supports:

- [`UISceneSessionRoleImmersiveSpaceApplication`](./uisceneconfigurations/uiscenesessionroleimmersivespaceapplication.md)
- [`CPSceneSessionRoleImmersiveSpaceApplication`](./uisceneconfigurations/cpscenesessionroleimmersivespaceapplication.md)

For applications with [CarPlay](../../../CarPlay/CarPlay.md) capabilities, it also supports these additional keys:

- [`CPTemplateApplicationSceneSessionRoleApplication`](./uisceneconfigurations/cptemplateapplicationscenesessionroleapplication.md)
- [`CPTemplateApplicationDashboardSceneSessionRoleApplication`](./uisceneconfigurations/cptemplateapplicationdashboardscenesessionroleapplication.md)
- [`CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication`](./uisceneconfigurations/cptemplateapplicationinstrumentclusterscenesessionroleapplication.md)

> **Note**:  If you don’t include this key in your `Info.plist` file, you must implement the [`application(_:configurationForConnecting:options:)`](../../../UIKit/uiapplicationdelegate/application%28_,configurationforconnecting,options%29.md) method in your app delegate.

## Topics

### Window scene roles
- [UIWindowSceneSessionRoleApplication](./uisceneconfigurations/uiwindowscenesessionroleapplication.md)
  Configurations for scenes you use to display content on the device’s main screen and respond to user interactions.
- [UIWindowSceneSessionRoleExternalDisplayNonInteractive](./uisceneconfigurations/uiwindowscenesessionroleexternaldisplaynoninteractive.md)
  Configurations for scenes you use to display noninteractive content on an externally connected display.
- [UIWindowSceneSessionRoleExternalDisplay](./uisceneconfigurations/uiwindowscenesessionroleexternaldisplay.md)
  Configurations for scenes you use to display noninteractive content on an externally connected display.
### Immersize space scene roles
- [UISceneSessionRoleImmersiveSpaceApplication](./uisceneconfigurations/uiscenesessionroleimmersivespaceapplication.md)
  Configurations for scenes you use to display SwiftUI content in an immersive space.
- [CPSceneSessionRoleImmersiveSpaceApplication](./uisceneconfigurations/cpscenesessionroleimmersivespaceapplication.md)
  Configurations for scenes you use to display Compositor Services content in an immersive space.
### CarPlay scene roles
- [CPTemplateApplicationSceneSessionRoleApplication](./uisceneconfigurations/cptemplateapplicationscenesessionroleapplication.md)
  Configurations for scenes that you use to display template content on a CarPlay-enabled vehicle screen.
- [CPTemplateApplicationDashboardSceneSessionRoleApplication](./uisceneconfigurations/cptemplateapplicationdashboardscenesessionroleapplication.md)
  Configurations for scenes that you use to display navigation content on a CarPlay Dashboard.
- [CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication](./uisceneconfigurations/cptemplateapplicationinstrumentclusterscenesessionroleapplication.md)
  Configurations for scenes you use to display navigation content on a CarPlay Instrument Cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations)*