# UISceneSessionRoleImmersiveSpaceApplication

**Framework**: Bundle Resources  
**Kind**: dictionary

Configurations for scenes you use to display SwiftUI content in an immersive space.

**Availability**:
- visionOS 1.0+

#### Discussion

Use this key to specify scene configurations for a session role. Each scene configuration corresponds to one you use for content you display on the device. The first item in the array represents the default scene configuration for this role. Use [`UIApplicationPreferredDefaultSceneSessionRole`](information-property-list/uiapplicationpreferreddefaultscenesessionrole.md) to indicate a preferred initial scene session role for your app.

> **Note**:  Immersive space scenes don’t provide support for custom scene delegate classes or scene sub-classes. The system ignores [`UISceneClassName`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneclassname.md), [`UISceneStoryboardFile`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenestoryboardfile.md) and [`UISceneDelegateClassName`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenedelegateclassname.md) keys you provide in a `UISceneSessionRoleImmersiveSpaceApplication` dictionary.

 Immersive space scenes don’t provide support for custom scene delegate classes or scene sub-classes. The system ignores [`UISceneClassName`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneclassname.md), [`UISceneStoryboardFile`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenestoryboardfile.md) and [`UISceneDelegateClassName`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenedelegateclassname.md) keys you provide in a `UISceneSessionRoleImmersiveSpaceApplication` dictionary.

## Topics

### Configuration name
- [UISceneConfigurationName](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneconfigurationname.md)
  The app-specific name you use to identify the scene.
### Immersion style
- [UISceneInitialImmersionStyle](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiscenesessionroleimmersivespaceapplication/uisceneinitialimmersionstyle.md)
  Provide a preferred initial scene style for an immersive space scene.

## See Also

- [CPSceneSessionRoleImmersiveSpaceApplication](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cpscenesessionroleimmersivespaceapplication.md)
  Configurations for scenes you use to display Compositor Services content in an immersive space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiscenesessionroleimmersivespaceapplication)*