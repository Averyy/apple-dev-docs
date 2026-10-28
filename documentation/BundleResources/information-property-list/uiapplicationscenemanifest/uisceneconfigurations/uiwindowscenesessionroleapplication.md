# UIWindowSceneSessionRoleApplication

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

Configurations for scenes you use to display content on the device’s main screen and respond to user interactions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+

## Details

- **Name**: `UIWindowSceneSessionRoleApplication` (Application Session Role)
- **Type**: array of dictionary 

## Discussion

Use this key to specify scene configurations for a session role. Each scene configuration corresponds to one you use for content you display on the device. The first item in the array represents the default scene configuration for this role.

## Topics

### Configuration name
- [UISceneConfigurationName](./uiwindowscenesessionroleapplication/uisceneconfigurationname.md)
  The app-specific name you use to identify the scene.
### Scene objects
- [UISceneClassName](./uiwindowscenesessionroleapplication/uisceneclassname.md)
  The name of the scene class you want UIKit to instantiate.
- [UISceneDelegateClassName](./uiwindowscenesessionroleapplication/uiscenedelegateclassname.md)
  The name of the app-specific class that you want UIKit to instantiate and use as the scene delegate object.
### Storyboard
- [UISceneStoryboardFile](./uiwindowscenesessionroleapplication/uiscenestoryboardfile.md)
  The name of the storyboard file containing the scene’s initial user interface.

## See Also

### Window scene roles
- [UIWindowSceneSessionRoleExternalDisplayNonInteractive](./uiwindowscenesessionroleexternaldisplaynoninteractive.md)
  Configurations for scenes you use to display noninteractive content on an externally connected display.
- [UIWindowSceneSessionRoleExternalDisplay](./uiwindowscenesessionroleexternaldisplay.md)
  Configurations for scenes you use to display noninteractive content on an externally connected display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication)*