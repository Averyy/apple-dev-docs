# UIApplicationSceneManifest

**Framework**: Bundle Resources  
**Kind**: dictionary

The information about the app’s scene-based life-cycle support.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

#### Discussion

The presence of this key indicates that the app supports scenes and doesn’t use an app delegate object to manage transitions to and from the foreground or background.

## Topics

### Multiple windows
- [UIApplicationSupportsMultipleScenes](information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes.md)
  A Boolean value indicating whether the app supports two or more scenes simultaneously.
- [UIApplicationSupportsTabbedSceneCollection](information-property-list/uiapplicationscenemanifest/uiapplicationsupportstabbedscenecollection.md)
  A Boolean value indicating whether an app built with Mac Catalyst supports automatic tabbing mode.
### CarPlay
- [CPSupportsDashboardNavigationScene](information-property-list/uiapplicationscenemanifest/cpsupportsdashboardnavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Dashboard.
- [CPSupportsInstrumentClusterNavigationScene](information-property-list/uiapplicationscenemanifest/cpsupportsinstrumentclusternavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Instrument Cluster.
### Configuration
- [UISceneConfigurations](information-property-list/uiapplicationscenemanifest/uisceneconfigurations.md)
  The default configuration details the system uses to create new scenes.

## See Also

- [UIApplicationPreferredDefaultSceneSessionRole](information-property-list/uiapplicationpreferreddefaultscenesessionrole.md)
  The preferred initial scene session role for your app.
- [NSMainStoryboardFile](information-property-list/nsmainstoryboardfile.md)
  The name of an app’s storyboard resource file.
- [UIMainStoryboardFile](information-property-list/uimainstoryboardfile.md)
  The name of the app’s main storyboard file.
- [NSMainNibFile](information-property-list/nsmainnibfile.md)
  The name of an app’s main user interface file.
- [LSUIElement](information-property-list/lsuielement.md)
  A Boolean value indicating whether the app is an agent app that runs in the background and doesn’t appear in the Dock.
- [UISupportsTrueScreenSizeOnMac](information-property-list/uisupportstruescreensizeonmac.md)
  A Boolean value that indicates whether your iPad app supports arbitrary screen sizes and resolutions when running on a Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest)*