# NSWidgetBackgroundColorName

**Framework**: Bundle Resources  
**Kind**: typealias

The name of a color in an asset catalog to use for a widget’s configuration interface.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+

#### Discussion

This `Info.plist` value controls the background color shown in the widget configuration interface while editing a widget.

While you can set this directly in your Info.plist, the recommended approach is to use the `Widget Background Color Name` build setting (in the `Asset Catalog Compiler - Options` section) of the widget extension target.  Set the value of the build setting to the name of the Color Set in the asset catalog. Xcode automatically sets `NSWidgetBackgroundColorName` to the appropriate value in the `Info.plist` file when building your project.

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
- [UIRequiresFullScreen](information-property-list/uirequiresfullscreen.md)
  A Boolean value that indicates whether an iPad app is capable of sharing the screen with other apps.
- [UISupportsFullScreenInAssistiveAccess](information-property-list/uisupportsfullscreeninassistiveaccess.md)
  A Boolean value that indicates if an iOS or iPadOS app appears as full screen in Assistive Access.
- [NSPrefersDisplaySafeAreaCompatibilityMode](information-property-list/nsprefersdisplaysafeareacompatibilitymode.md)
  A Boolean value that indicates whether the app prefers to run in compatibility mode when necessary.
- [NSAccentColorName](information-property-list/nsaccentcolorname.md)
  The name of a color in an asset catalog to use for a target’s global accent color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nswidgetbackgroundcolorname)*