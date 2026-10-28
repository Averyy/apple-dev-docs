# CPTemplateApplicationSceneSessionRoleApplication

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

Configurations for scenes that you use to display template content on a CarPlay-enabled vehicle screen.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Details

- **Name**: `CPTemplateApplicationSceneSessionRoleApplication`
- **Type**: array of dictionary 

## Discussion

Use this key to specify the scene configuration you use when displaying content on a CarPlay-enabled vehicle screen.

For more information, see [Displaying Content in CarPlay](../../../../CarPlay/displaying-content-in-carplay.md).

## Topics

### Configuration name
- [UISceneConfigurationName](./cptemplateapplicationscenesessionroleapplication/uisceneconfigurationname.md)
  The app-specific name you use to identify the scene.
### Scene objects
- [UISceneClassName](./cptemplateapplicationscenesessionroleapplication/uisceneclassname.md)
  The name of the scene class you want UIKit to instantiate.
- [UISceneDelegateClassName](./cptemplateapplicationscenesessionroleapplication/uiscenedelegateclassname.md)
  The name of the app-specific class you want UIKit to instantiate and use as the delegate of your app’s main scene.

## See Also

### CarPlay scene roles
- [CPTemplateApplicationDashboardSceneSessionRoleApplication](./cptemplateapplicationdashboardscenesessionroleapplication.md)
  Configurations for scenes that you use to display navigation content on a CarPlay Dashboard.
- [CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication](./cptemplateapplicationinstrumentclusterscenesessionroleapplication.md)
  Configurations for scenes you use to display navigation content on a CarPlay Instrument Cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationscenesessionroleapplication)*