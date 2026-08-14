# UISceneDelegateClassName

**Framework**: Bundle Resources  
**Kind**: typealias

The name of the app-specific class that you want UIKit to instantiate and use as the scene delegate object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+



**Type**: string

#### Discussion

The class you specify for this key must adopt the [`UISceneDelegate`](https://developer.apple.com/documentation/uikit/uiscenedelegate) protocol. If the class you specify for the [`UISceneClassName`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneclassname.md) key is [`UIWindowScene`](https://developer.apple.com/documentation/uikit/uiwindowscene), your class must adopt the [`UIWindowSceneDelegate`](https://developer.apple.com/documentation/uikit/uiwindowscenedelegate) protocol.

## See Also

- [UISceneClassName](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneclassname.md)
  The name of the scene class you want UIKit to instantiate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenedelegateclassname)*