# CPTemplateApplicationDashboardSceneSessionRoleApplication

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

Configurations for scenes that you use to display navigation content on a CarPlay Dashboard.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+

## Details

- **Name**: `CPTemplateApplicationDashboardSceneSessionRoleApplication`
- **Type**: array of dictionary 

#### Discussion

After setting [`CPSupportsDashboardNavigationScene`](../cpsupportsdashboardnavigationscene.md) to `YES`, use this key to specify the scene configuration when displaying navigation content in the CarPlay Dashboard.

For more information, see [Displaying Content in CarPlay](../../../../CarPlay/displaying-content-in-carplay.md).

## Topics

### Configuration name
- [UISceneConfigurationName](./cptemplateapplicationdashboardscenesessionroleapplication/uisceneconfigurationname.md)
  The app-specific name you use to identify the scene.
### Scene objects
- [UISceneClassName](./cptemplateapplicationdashboardscenesessionroleapplication/uisceneclassname.md)
  The name of the scene class you want UIKit to instantiate.
- [UISceneDelegateClassName](./cptemplateapplicationdashboardscenesessionroleapplication/uiscenedelegateclassname.md)
  The name of the app-specific class you want UIKit to instantiate and use as the delegate for your app’s dashboard scene.

## See Also

### CarPlay scene roles
- [CPTemplateApplicationSceneSessionRoleApplication](./cptemplateapplicationscenesessionroleapplication.md)
  Configurations for scenes that you use to display template content on a CarPlay-enabled vehicle screen.
- [CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication](./cptemplateapplicationinstrumentclusterscenesessionroleapplication.md)
  Configurations for scenes you use to display navigation content on a CarPlay Instrument Cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationdashboardscenesessionroleapplication)*