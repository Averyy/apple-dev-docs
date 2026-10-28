# UISceneDelegateClassName

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The name of the app-specific class that you want UIKit to instantiate and use as the scene delegate object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+

## Details

- **Name**: `UISceneDelegateClassName` (Delegate Class Name)
- **Type**: string

## Discussion

The class you specify for this key must adopt the [`UISceneDelegate`](../../../../../UIKit/uiscenedelegate.md) protocol. If the class you specify for the [`UISceneClassName`](./uisceneclassname.md) key is [`UIWindowScene`](../../../../../UIKit/uiwindowscene.md), your class must adopt the [`UIWindowSceneDelegate`](../../../../../UIKit/uiwindowscenedelegate.md) protocol.

## See Also

### Scene objects
- [UISceneClassName](./uisceneclassname.md)
  The name of the scene class you want UIKit to instantiate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenedelegateclassname)*