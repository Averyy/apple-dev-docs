# UISceneDelegateClassName

**Framework**: Bundle Resources  
**Kind**: typealias

The name of the app-specific class you want UIKit to instantiate and use as the delegate for your app’s dashboard scene.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+



**Type**: string

#### Discussion

Include this key in the one of the dictionaries you specify for the value of the [`CPTemplateApplicationDashboardSceneSessionRoleApplication`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationdashboardscenesessionroleapplication.md) key.

This key tells the system where to find the delegate class for your app’s main CarPlay scene. The value of this key is a string with the format `<app-name>.<class-name>`, in which `<app-name>` is the name of your iOS app and `<class-name>` is the name of a class that adopts the [`CPTemplateApplicationDashboardSceneDelegate`](https://developer.apple.com/documentation/carplay/cptemplateapplicationdashboardscenedelegate) protocol.

## See Also

- [UISceneClassName](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationdashboardscenesessionroleapplication/uisceneclassname.md)
  The name of the scene class you want UIKit to instantiate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationdashboardscenesessionroleapplication/uiscenedelegateclassname)*