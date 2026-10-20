# UIUserInterfaceStyle

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The user interface style for the app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- tvOS 10.0+

## Details

- **Name**: `UIUserInterfaceStyle` (Appearance)
- **Type**: string

## Possible Values

- `Automatic`: Set this value to adopt the systemwide user interface style, and observe any changes to that style. This is the default value, and provides the same functionality as if the key weren’t explicitly set.
- `Light`: Set this value to force the light user interface style, even when the systemwide style is set to dark. Your app will ignore any changes to the systemwide style.
- `Dark`: Set this value to force the dark user interface style, even when the systemwide style is set to light. Your app will ignore any changes to the systemwide style.



**Default**: `Automatic`

## See Also

### Styling
- [UIDesignRequiresCompatibility](./uidesignrequirescompatibility.md)
  A Boolean value that indicates whether the system runs the app using a compatibility mode for UI.
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
- [NSAccentColorName](./nsaccentcolorname.md)
  The name of a color in an asset catalog to use for a target’s global accent color.
- [NSWidgetBackgroundColorName](./nswidgetbackgroundcolorname.md)
  The name of a color in an asset catalog to use for a widget’s configuration interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiuserinterfacestyle)*