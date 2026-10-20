# CPSupportsInstrumentClusterNavigationScene

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Instrument Cluster.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+

## Details

- **Name**: `CPSupportsInstrumentClusterNavigationScene`
- **Type**: boolean

#### Discussion

To declare support for displaying navigation content in the CarPlay Instruments Cluster, add this key and set its value to YES. You specify the scene configurations using the [`CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication`](./uisceneconfigurations/cptemplateapplicationinstrumentclusterscenesessionroleapplication.md) key.

For more information, see [Displaying Content in CarPlay](../../../CarPlay/displaying-content-in-carplay.md).

## See Also

### CarPlay
- [CPSupportsDashboardNavigationScene](./cpsupportsdashboardnavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Dashboard.
- [CPInstrumentClusterNavigationSceneOptions](./cpinstrumentclusternavigationsceneoptions.md)
  A dictionary of options that indicates your app’s level of support for the CarPlay instrument cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/cpsupportsinstrumentclusternavigationscene)*