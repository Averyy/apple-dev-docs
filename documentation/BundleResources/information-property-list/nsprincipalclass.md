# NSPrincipalClass

**Framework**: Bundle Resources  
**Kind**: typealias

The name of the bundle’s main executable class.

**Availability**:
- macOS 10.0+

#### Discussion

The system uses the class identified by this key to set the [`principalClass`](https://developer.apple.com/documentation/Foundation/Bundle/principalClass) property of a bundle when it’s loaded.

Xcode sets the default value of this key to [`NSApplication`](https://developer.apple.com/documentation/AppKit/NSApplication) for macOS apps, and to [`UIApplication`](https://developer.apple.com/documentation/UIKit/UIApplication) for iOS and tvOS apps. For other types of bundles, you must set this key in [`The Info.plist File`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProvidingUserAssitAppleHelp/authoring_help/authoring_help_book.html#//apple_ref/doc/uid/TP30000903-CH206-SW22).

## See Also

- [CLKComplicationPrincipalClass](information-property-list/clkcomplicationprincipalclass.md)
  The name of the class that implements the complication data source protocol.
- [CFBundleExecutable](information-property-list/cfbundleexecutable.md)
  The name of the bundle’s executable file.
- [LSEnvironment](information-property-list/lsenvironment.md)
  Environment variables to set before launching the app.
- [UIApplicationShortcutItems](information-property-list/uiapplicationshortcutitems.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsprincipalclass)*