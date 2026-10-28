# NSPrincipalClass

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The name of the bundle’s main executable class.

**Availability**:
- macOS 10.0+

## Details

- **Name**: `NSPrincipalClass` (Principal class)
- **Type**: string

## Discussion

The system uses the class identified by this key to set the [`principalClass`](../../Foundation/bundle/principalclass.md) property of a bundle when it’s loaded.

Xcode sets the default value of this key to [`NSApplication`](../../AppKit/nsapplication.md) for macOS apps, and to [`UIApplication`](../../UIKit/uiapplication.md) for iOS and tvOS apps. For other types of bundles, you must set this key in [The Info.plist File](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProvidingUserAssitAppleHelp/authoring_help/authoring_help_book.html#//apple_ref/doc/uid/TP30000903-CH206-SW22).

## See Also

### Launch
- [CLKComplicationPrincipalClass](./clkcomplicationprincipalclass.md)
  The name of the class that implements the complication data source protocol.
- [CFBundleExecutable](./cfbundleexecutable.md)
  The name of the bundle’s executable file.
- [LSEnvironment](./lsenvironment.md)
  Environment variables to set before launching the app.
- [UIApplicationShortcutItems](./uiapplicationshortcutitems.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsprincipalclass)*