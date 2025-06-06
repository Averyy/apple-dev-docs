# CPSceneSessionRoleImmersiveSpaceApplication

**Framework**: Bundle Resources  
**Kind**: dictionary

Configurations for scenes you use to display Compositor Services content in an immersive space.

**Availability**:
- visionOS 1.0+

#### Discussion

Use this key to specify scene configurations for a session role. Each scene corresponds to one you use for content you display on the device. Make the default scene the first entry in the array. Use [`UIApplicationPreferredDefaultSceneSessionRole`](information-property-list/uiapplicationpreferreddefaultscenesessionrole.md) to indicate a preferred initial scene session role.

> **Note**:  Immersive space scenes don’t provide support for custom scene delegate classes or scene sub-classes, the system ignores [`UISceneClassName`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneclassname.md), [`UISceneStoryboardFile`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenestoryboardfile.md) and [`UISceneDelegateClassName`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenedelegateclassname.md) keys your provide in a [`CPSceneSessionRoleImmersiveSpaceApplication`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cpscenesessionroleimmersivespaceapplication.md) dictionary.

 Immersive space scenes don’t provide support for custom scene delegate classes or scene sub-classes, the system ignores [`UISceneClassName`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneclassname.md), [`UISceneStoryboardFile`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenestoryboardfile.md) and [`UISceneDelegateClassName`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenedelegateclassname.md) keys your provide in a [`CPSceneSessionRoleImmersiveSpaceApplication`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cpscenesessionroleimmersivespaceapplication.md) dictionary.

## Topics

### Configuration name
- [UISceneConfigurationName](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneconfigurationname.md)
  The app-specific name you use to identify the scene.

## See Also

- [UISceneSessionRoleImmersiveSpaceApplication](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiscenesessionroleimmersivespaceapplication.md)
  Configurations for scenes you use to display SwiftUI content in an immersive space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cpscenesessionroleimmersivespaceapplication)*