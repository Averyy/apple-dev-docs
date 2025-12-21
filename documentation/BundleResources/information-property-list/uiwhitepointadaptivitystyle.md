# UIWhitePointAdaptivityStyle

**Framework**: Bundle Resources  
**Kind**: typealias

The app’s white-point adaptivity style, enabled on devices with True Tone displays.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+

#### Discussion

In split view, the system applies the style on the entire screen from the app with the weaker adaptivity style setting. For example, if one app uses the `UIWhitePointAdaptivityStylePhoto` style and another uses the `UIWhitePointAdaptivityStyleReading` style, the system uses the weaker `UIWhitePointAdaptivityStyleReading` style for the entire screen.

## See Also

- [UIDesignRequiresCompatibility](information-property-list/uidesignrequirescompatibility.md)
  A Boolean value that indicates whether the system runs the app using a compatibility mode for UI.
- [UIUserInterfaceStyle](information-property-list/uiuserinterfacestyle.md)
  The user interface style for the app.
- [UIViewEdgeAntialiasing](information-property-list/uiviewedgeantialiasing.md)
  A Boolean value that indicates whether Core Animation layers use antialiasing when drawing a layer that isn’t aligned to pixel boundaries.
- [UIViewGroupOpacity](information-property-list/uiviewgroupopacity.md)
  A Boolean value that indicates whether Core Animation sublayers inherit the opacity of their superlayer.
- [UIRequiresFullScreenIgnoredStartingWithVersion](information-property-list/uirequiresfullscreenignoredstartingwithversion.md)
  A string value that specifies a system version after which the system ignores the requires full screen key.
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

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiwhitepointadaptivitystyle)*