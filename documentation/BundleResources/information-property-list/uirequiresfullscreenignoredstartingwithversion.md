# UIRequiresFullScreenIgnoredStartingWithVersion

**Framework**: Bundle Resources  
**Kind**: typealias

A string value that specifies a system version after which the system ignores the requires full screen key.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

#### Discussion

Use this key only if you’ve already updated your app so that it no longer uses [`UIRequiresFullScreen`](information-property-list/uirequiresfullscreen.md) in later versions of iOS. Add the key, then specify in which version of iOS you want the system to begin ignoring the [`UIRequiresFullScreen`](information-property-list/uirequiresfullscreen.md) key. The system ignores the key starting in the version you specify and in later versions of iOS.

The system only uses this key when your information property list also contains [`UIRequiresFullScreen`](information-property-list/uirequiresfullscreen.md) with a value of `true`.

## See Also

- [UIDesignRequiresCompatibility](information-property-list/uidesignrequirescompatibility.md)
  A Boolean value that indicates whether the system runs the app using a compatibility mode for UI.
- [UIUserInterfaceStyle](information-property-list/uiuserinterfacestyle.md)
  The user interface style for the app.
- [UIViewEdgeAntialiasing](information-property-list/uiviewedgeantialiasing.md)
  A Boolean value that indicates whether Core Animation layers use antialiasing when drawing a layer that isn’t aligned to pixel boundaries.
- [UIWhitePointAdaptivityStyle](information-property-list/uiwhitepointadaptivitystyle.md)
  The app’s white-point adaptivity style, enabled on devices with True Tone displays.
- [UIViewGroupOpacity](information-property-list/uiviewgroupopacity.md)
  A Boolean value that indicates whether Core Animation sublayers inherit the opacity of their superlayer.
- [UISupportsAssistiveAccess](information-property-list/uisupportsassistiveaccess.md)
  A Boolean value that indicates if an iOS or iPadOS app supports Assistive Access.
- [UISupportsFullScreenInAssistiveAccess](information-property-list/uisupportsfullscreeninassistiveaccess.md)
  A Boolean value that indicates if an iOS or iPadOS app appears as full screen in Assistive Access.
- [NSPrefersDisplaySafeAreaCompatibilityMode](information-property-list/nsprefersdisplaysafeareacompatibilitymode.md)
  A Boolean value that indicates whether the app prefers to run in compatibility mode when necessary.
- [NSAccentColorName](information-property-list/nsaccentcolorname.md)
  The name of a color in an asset catalog to use for a target’s global accent color.
- [NSWidgetBackgroundColorName](information-property-list/nswidgetbackgroundcolorname.md)
  The name of a color in an asset catalog to use for a widget’s configuration interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uirequiresfullscreenignoredstartingwithversion)*