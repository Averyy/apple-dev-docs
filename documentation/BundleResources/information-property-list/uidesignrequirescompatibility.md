# UIDesignRequiresCompatibility

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the system runs the app using a compatibility mode for UI.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

#### Discussion

> ⚠️ **Warning**: Temporarily use this key while reviewing and refining your app’s UI for the design in the latest SDKs.

If `YES`, the system runs the app using a compatibility mode for UI elements. The compatibility mode displays the app as it looks when built against previous versions of the SDKs.

If `NO`, the system uses the UI design of the running OS, with no compatibility mode. Absence of the key, or `NO`, is the default value for apps linking against the latest SDKs.

## See Also

- [UIUserInterfaceStyle](information-property-list/uiuserinterfacestyle.md)
  The user interface style for the app.
- [UIViewEdgeAntialiasing](information-property-list/uiviewedgeantialiasing.md)
  A Boolean value that indicates whether Core Animation layers use antialiasing when drawing a layer that isn’t aligned to pixel boundaries.
- [UIWhitePointAdaptivityStyle](information-property-list/uiwhitepointadaptivitystyle.md)
  The app’s white-point adaptivity style, enabled on devices with True Tone displays.
- [UIViewGroupOpacity](information-property-list/uiviewgroupopacity.md)
  A Boolean value that indicates whether Core Animation sublayers inherit the opacity of their superlayer.
- [UIRequiresFullScreen](information-property-list/uirequiresfullscreen.md)
  A Boolean value that indicates whether an iPad app is capable of sharing the screen with other apps.
- [UISupportsFullScreenInAssistiveAccess](information-property-list/uisupportsfullscreeninassistiveaccess.md)
  A Boolean value that indicates if an iOS or iPadOS app appears as full screen in Assistive Access.
- [NSPrefersDisplaySafeAreaCompatibilityMode](information-property-list/nsprefersdisplaysafeareacompatibilitymode.md)
  A Boolean value that indicates whether the app prefers to run in compatibility mode when necessary.
- [NSAccentColorName](information-property-list/nsaccentcolorname.md)
  The name of a color in an asset catalog to use for a target’s global accent color.
- [NSWidgetBackgroundColorName](information-property-list/nswidgetbackgroundcolorname.md)
  The name of a color in an asset catalog to use for a widget’s configuration interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uidesignrequirescompatibility)*