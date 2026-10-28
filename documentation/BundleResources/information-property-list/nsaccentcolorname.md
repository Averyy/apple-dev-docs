# NSAccentColorName

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The name of a color in an asset catalog to use for a target’s global accent color.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Details

- **Name**: `NSAccentColorName`
- **Type**: string

## Discussion

This `Info.plist` value controls the global tint color (iOS and watchOS) or accent color (macOS) for the target.  When set in a widget extension, the widget configuration user interface uses this color as the tint color while editing a widget.

While you can set this directly in your `Info.plist`, the recommended approach is to use the `Global Accent Color Name` build setting (in the `Asset Catalog Compiler - Options` section) of the target.  Set the value of the build setting to the name of the Color Set in the asset catalog. Xcode automatically sets `NSAccentColorName` to the appropriate value in the `Info.plist` file when building your project.

## See Also

### Styling
- [UIDesignRequiresCompatibility](./uidesignrequirescompatibility.md)
  A Boolean value that indicates whether the system runs the app using a compatibility mode for UI.
- [UIUserInterfaceStyle](./uiuserinterfacestyle.md)
  The user interface style for the app.
- [UIViewEdgeAntialiasing](./uiviewedgeantialiasing.md)
  A Boolean value that indicates whether Core Animation layers use antialiasing when drawing a layer that isn’t aligned to pixel boundaries.
- [UIWhitePointAdaptivityStyle](./uiwhitepointadaptivitystyle.md)
  The app’s white-point adaptivity style, enabled on devices with True Tone displays.
- [UIViewGroupOpacity](./uiviewgroupopacity.md)
  A Boolean value that indicates whether Core Animation sublayers inherit the opacity of their superlayer.
- [UIRequiresFullScreenIgnoredStartingWithVersion](./uirequiresfullscreenignoredstartingwithversion.md)
  A string value that specifies a system version after which the system ignores the requires full screen key.
- [UISupportsAssistiveAccess](./uisupportsassistiveaccess.md)
  A Boolean value that indicates if an iOS or iPadOS app supports Assistive Access.
- [UISupportsFullScreenInAssistiveAccess](./uisupportsfullscreeninassistiveaccess.md)
  A Boolean value that indicates if an iOS or iPadOS app appears as full screen in Assistive Access.
- [NSPrefersDisplaySafeAreaCompatibilityMode](./nsprefersdisplaysafeareacompatibilitymode.md)
  A Boolean value that indicates whether the app prefers to run in compatibility mode when necessary.
- [NSWidgetBackgroundColorName](./nswidgetbackgroundcolorname.md)
  The name of a color in an asset catalog to use for a widget’s configuration interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsaccentcolorname)*