# UISceneConfigurations

**Framework**: Bundle Resources  
**Kind**: dictionary

The default configuration details the system uses to create new scenes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

#### Discussion

The keys in the dictionary correspond to the roles played by your scenes.

[`UISceneConfigurations`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations.md) supports the following keys:

- [`UIWindowSceneSessionRoleApplication`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication.md)
- [`UIWindowSceneSessionRoleExternalDisplayNonInteractive`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleexternaldisplaynoninteractive.md)

For visionOS apps, it also supports:

- [`UISceneSessionRoleImmersiveSpaceApplication`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiscenesessionroleimmersivespaceapplication.md)
- [`CPSceneSessionRoleImmersiveSpaceApplication`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cpscenesessionroleimmersivespaceapplication.md)

For applications with [`CarPlay`](https://developer.apple.com/documentation/CarPlay) capabilities, it also supports these additional keys:

- [`CPTemplateApplicationSceneSessionRoleApplication`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationscenesessionroleapplication.md)
- [`CPTemplateApplicationDashboardSceneSessionRoleApplication`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationdashboardscenesessionroleapplication.md)
- [`CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationinstrumentclusterscenesessionroleapplication.md)

> **Note**:  If you don’t include this key in your `Info.plist` file, you must implement the [`application(_:configurationForConnecting:options:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:configurationForConnecting:options:)) method in your app delegate.

## Topics

### Window scene roles
- [UIWindowSceneSessionRoleApplication](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication.md)
  Configurations for scenes you use to display content on the device’s main screen and respond to user interactions.
- [UIWindowSceneSessionRoleExternalDisplayNonInteractive](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleexternaldisplaynoninteractive.md)
  Configurations for scenes you use to display noninteractive content on an externally connected display.
- [UIWindowSceneSessionRoleExternalDisplay](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleexternaldisplay.md)
  Configurations for scenes you use to display noninteractive content on an externally connected display.
### Immersize space scene roles
- [UISceneSessionRoleImmersiveSpaceApplication](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiscenesessionroleimmersivespaceapplication.md)
  Configurations for scenes you use to display SwiftUI content in an immersive space.
- [CPSceneSessionRoleImmersiveSpaceApplication](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cpscenesessionroleimmersivespaceapplication.md)
  Configurations for scenes you use to display Compositor Services content in an immersive space.
### CarPlay scene roles
- [CPTemplateApplicationSceneSessionRoleApplication](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationscenesessionroleapplication.md)
  Configurations for scenes that you use to display template content on a CarPlay-enabled vehicle screen.
- [CPTemplateApplicationDashboardSceneSessionRoleApplication](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationdashboardscenesessionroleapplication.md)
  Configurations for scenes that you use to display navigation content on a CarPlay Dashboard.
- [CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationinstrumentclusterscenesessionroleapplication.md)
  Configurations for scenes you use to display navigation content on a CarPlay Instrument Cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations)*