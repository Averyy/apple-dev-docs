# CPSupportsDashboardNavigationScene

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Dashboard.

**Availability**:
- iOS 13.1+
- iPadOS 13.1+

## Details

- **Name**: `CPSupportsDashboardNavigationScene`
- **Type**: boolean

## Discussion

To declare support for displaying navigation content in the CarPlay Dashboard, add this key and set its value to YES. You specify the scene configurations using the [`CPTemplateApplicationDashboardSceneSessionRoleApplication`](./uisceneconfigurations/cptemplateapplicationdashboardscenesessionroleapplication.md) key.

For more information, see [Displaying Content in CarPlay](../../../CarPlay/displaying-content-in-carplay.md).

## See Also

### CarPlay
- [CPSupportsInstrumentClusterNavigationScene](./cpsupportsinstrumentclusternavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Instrument Cluster.
- [CPInstrumentClusterNavigationSceneOptions](./cpinstrumentclusternavigationsceneoptions.md)
  A dictionary of options that indicates your app’s level of support for the CarPlay instrument cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/cpsupportsdashboardnavigationscene)*