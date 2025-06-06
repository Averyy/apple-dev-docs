# UIWindowSceneSessionRoleExternalDisplayNonInteractive

**Framework**: Bundle Resources  
**Kind**: dictionary

Configurations for scenes you use to display noninteractive content on an externally connected display.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

#### Discussion

Use this key to specify scene configurations for a session role. Each scene configuration corresponds to one you use for content you display on the device. The first item in the array represents the default scene configuration for this role.

## Topics

### Configuration name
- [UISceneConfigurationName](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneconfigurationname.md)
  The app-specific name you use to identify the scene.
### Scene objects
- [UISceneClassName](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneclassname.md)
  The name of the scene class you want UIKit to instantiate.
- [UISceneDelegateClassName](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenedelegateclassname.md)
  The name of the app-specific class that you want UIKit to instantiate and use as the scene delegate object.
### Storyboard
- [UISceneStoryboardFile](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenestoryboardfile.md)
  The name of the storyboard file containing the scene’s initial user interface.

## See Also

- [Presenting content on a connected display](../UIKit/presenting-content-on-a-connected-display.md)
  Fill connected displays with additional content from your app.
- [UIWindowSceneSessionRoleApplication](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication.md)
  Configurations for scenes you use to display content on the device’s main screen and respond to user interactions.
- [UIWindowSceneSessionRoleExternalDisplay](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleexternaldisplay.md)
  Configurations for scenes you use to display noninteractive content on an externally connected display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleexternaldisplaynoninteractive)*