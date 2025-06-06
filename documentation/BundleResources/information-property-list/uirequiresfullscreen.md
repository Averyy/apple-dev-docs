# UIRequiresFullScreen

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether an iPad app is capable of sharing the screen with other apps.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+

#### Discussion

iPad multitasking lets multiple apps appear on screen at the same time. Dragging the resize controls causes the system to change the size of each app’s window. Each app must then adjust its content to fit the newly available space.

If your app’s content requires a full-screen presentation, include this key in your `Info.plist` and set its value to [`true`](https://developer.apple.com/documentation/swift/true). When you do, the system prevents your app from sharing the screen with other apps. On an external screen, the window for an app with this setting maintains its canvas size.

Don’t include this key in your `Info.plist` file if your app supports iPad multitasking and is capable of running alongside other apps. To take advantage of the full size of an external screen consider adopting resizability and multitasking support. If this key is absent, or is present and set to [`false`](https://developer.apple.com/documentation/swift/false), the system lets your app share the screen with other apps.

## See Also

- [Multitasking on iPad](../UIKit/multitasking-on-ipad.md)
  Implement multitasking APIs to seamlessly integrate your app with iPadOS.
- [Presenting content on a connected display](../UIKit/presenting-content-on-a-connected-display.md)
  Fill connected displays with additional content from your app.
- [UIUserInterfaceStyle](information-property-list/uiuserinterfacestyle.md)
  The user interface style for the app.
- [UIViewEdgeAntialiasing](information-property-list/uiviewedgeantialiasing.md)
  A Boolean value that indicates whether Core Animation layers use antialiasing when drawing a layer that isn’t aligned to pixel boundaries.
- [UIWhitePointAdaptivityStyle](information-property-list/uiwhitepointadaptivitystyle.md)
  The app’s white-point adaptivity style, enabled on devices with True Tone displays.
- [UIViewGroupOpacity](information-property-list/uiviewgroupopacity.md)
  A Boolean value that indicates whether Core Animation sublayers inherit the opacity of their superlayer.
- [UISupportsFullScreenInAssistiveAccess](information-property-list/uisupportsfullscreeninassistiveaccess.md)
  A Boolean value that indicates if an iOS or iPadOS app appears as full screen in Assistive Access.
- [NSPrefersDisplaySafeAreaCompatibilityMode](information-property-list/nsprefersdisplaysafeareacompatibilitymode.md)
  A Boolean value that indicates whether the app prefers to run in compatibility mode when necessary.
- [NSAccentColorName](information-property-list/nsaccentcolorname.md)
  The name of a color in an asset catalog to use for a target’s global accent color.
- [NSWidgetBackgroundColorName](information-property-list/nswidgetbackgroundcolorname.md)
  The name of a color in an asset catalog to use for a widget’s configuration interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uirequiresfullscreen)*