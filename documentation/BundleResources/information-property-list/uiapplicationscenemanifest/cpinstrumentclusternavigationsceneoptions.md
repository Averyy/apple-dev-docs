# CPInstrumentClusterNavigationSceneOptions

**Framework**: Bundle Resources  
**Kind**: dictionary

A dictionary of options that indicates your app’s level of support for the CarPlay instrument cluster.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+



**Type**: dictionary

#### Discussion

When this key is present at the top level of the app’s scene manifest, CarPlay creates your app’s instrument cluster scene only if the app is running in iOS 26.2 or later. The value of this key is an empty dictionary.

## See Also

- [CPSupportsDashboardNavigationScene](information-property-list/uiapplicationscenemanifest/cpsupportsdashboardnavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Dashboard.
- [CPSupportsInstrumentClusterNavigationScene](information-property-list/uiapplicationscenemanifest/cpsupportsinstrumentclusternavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Instrument Cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/cpinstrumentclusternavigationsceneoptions)*