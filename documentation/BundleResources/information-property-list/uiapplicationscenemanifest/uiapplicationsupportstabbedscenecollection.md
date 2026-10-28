# UIApplicationSupportsTabbedSceneCollection

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value indicating whether an app built with Mac Catalyst supports automatic tabbing mode.

**Availability**:
- Mac Catalyst 15.0+

## Details

- **Name**: `UIApplicationSupportsTabbedSceneCollection` (Supports Tabbed Scene Collection)
- **Type**: boolean



**Default**: `YES`

## Discussion

By default, the tabbing mode for an app built with Mac Catalyst that support multiple scenes is [`NSWindow.TabbingMode.automatic`](../../../AppKit/nswindow/tabbingmode-swift.enum/automatic.md). Starting with macOS 12, you can disable this behavior by adding the [`UIApplicationSupportsTabbedSceneCollection`](./uiapplicationsupportstabbedscenecollection.md) key with a value of [`false`](../../../Swift/false.md) to the [`UIApplicationSceneManifest`](../uiapplicationscenemanifest.md) key in your app’s `Info.plist` file.

## See Also

### Multiple windows
- [UIApplicationSupportsMultipleScenes](./uiapplicationsupportsmultiplescenes.md)
  A Boolean value indicating whether the app supports two or more scenes simultaneously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportstabbedscenecollection)*