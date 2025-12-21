# UIApplicationSupportsTabbedSceneCollection

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether an app built with Mac Catalyst supports automatic tabbing mode.

**Availability**:
- Mac Catalyst 15.0+

#### Discussion

By default, the tabbing mode for an app built with Mac Catalyst that support multiple scenes is [`NSWindow.TabbingMode.automatic`](https://developer.apple.com/documentation/AppKit/NSWindow/TabbingMode-swift.enum/automatic). Starting with macOS 12, you can disable this behavior by adding the [`UIApplicationSupportsTabbedSceneCollection`](information-property-list/uiapplicationscenemanifest/uiapplicationsupportstabbedscenecollection.md) key with a value of [`false`](https://developer.apple.com/documentation/Swift/false) to the [`UIApplicationSceneManifest`](information-property-list/uiapplicationscenemanifest.md) key in your app’s `Info.plist` file.

## See Also

- [UIApplicationSupportsMultipleScenes](information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes.md)
  A Boolean value indicating whether the app supports two or more scenes simultaneously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportstabbedscenecollection)*