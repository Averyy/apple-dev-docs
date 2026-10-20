# UISceneClassName

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The name of the scene class you want UIKit to instantiate.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Details

- **Name**: `UISceneClassName` (Class Name)
- **Type**: string

## Possible Values

- `CPTemplateApplicationScene`

#### Discussion

CarPlay doesn’t support custom classes. Omit this key or specify [`CPTemplateApplicationScene`](../../../../../CarPlay/cptemplateapplicationscene.md) for scenes meant for a CarPlay-enabled vehicle screen.

## See Also

### Scene objects
- [UISceneDelegateClassName](./uiscenedelegateclassname.md)
  The name of the app-specific class you want UIKit to instantiate and use as the delegate of your app’s main scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationscenesessionroleapplication/uisceneclassname)*