# UIApplicationSceneManifest

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

The information about the app’s scene-based life-cycle support.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Details

- **Name**: `UIApplicationSceneManifest` (Application Scene Manifest)
- **Type**: dictionary

## Discussion

The presence of this key indicates that the app supports scenes and doesn’t use an app delegate object to manage transitions to and from the foreground or background.

## Topics

### Multiple windows
- [UIApplicationSupportsMultipleScenes](./uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes.md)
  A Boolean value indicating whether the app supports two or more scenes simultaneously.
- [UIApplicationSupportsTabbedSceneCollection](./uiapplicationscenemanifest/uiapplicationsupportstabbedscenecollection.md)
  A Boolean value indicating whether an app built with Mac Catalyst supports automatic tabbing mode.
### CarPlay
- [CPSupportsDashboardNavigationScene](./uiapplicationscenemanifest/cpsupportsdashboardnavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Dashboard.
- [CPSupportsInstrumentClusterNavigationScene](./uiapplicationscenemanifest/cpsupportsinstrumentclusternavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Instrument Cluster.
- [CPInstrumentClusterNavigationSceneOptions](./uiapplicationscenemanifest/cpinstrumentclusternavigationsceneoptions.md)
  A dictionary of options that indicates your app’s level of support for the CarPlay instrument cluster.
### Configuration
- [UISceneConfigurations](./uiapplicationscenemanifest/uisceneconfigurations.md)
  The default configuration details the system uses to create new scenes.

## See Also

### Main user interface
- [UIApplicationPreferredDefaultSceneSessionRole](./uiapplicationpreferreddefaultscenesessionrole.md)
  The preferred initial scene session role for your app.
- [NSMainStoryboardFile](./nsmainstoryboardfile.md)
  The name of an app’s storyboard resource file.
- [UIMainStoryboardFile](./uimainstoryboardfile.md)
  The name of the app’s main storyboard file.
- [NSMainNibFile](./nsmainnibfile.md)
  The name of an app’s main user interface file.
- [LSUIElement](./lsuielement.md)
  A Boolean value indicating whether the app is an agent app that runs in the background and doesn’t appear in the Dock.
- [UISupportsTrueScreenSizeOnMac](./uisupportstruescreensizeonmac.md)
  A Boolean value that indicates whether your iPad app supports arbitrary screen sizes and resolutions when running on a Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest)*