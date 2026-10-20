# UISceneClassName

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The name of the scene class you want UIKit to instantiate.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+

## Details

- **Name**: `UISceneClassName` (Class Name)
- **Type**: string

## Possible Values

- `CPTemplateApplicationScene`

#### Discussion

CarPlay doesn’t support custom classes. Omit this key or specify [`CPTemplateApplicationInstrumentClusterScene`](../../../../../CarPlay/cptemplateapplicationinstrumentclusterscene.md) for scenes meant for a CarPlay Instrument Cluster.

## See Also

### Scene objects
- [UISceneDelegateClassName](./uiscenedelegateclassname.md)
  The name of the app-specific class you want UIKit to instantiate and use as the delegate for your app’s instrument cluster scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationinstrumentclusterscenesessionroleapplication/uisceneclassname)*