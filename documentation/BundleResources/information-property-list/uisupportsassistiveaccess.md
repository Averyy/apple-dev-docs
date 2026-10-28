# UISupportsAssistiveAccess

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates if an iOS or iPadOS app supports Assistive Access.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Details

- **Name**: `UISupportsAssistiveAccess` (Supports Assistive Access)
- **Type**: boolean



**Default**: `YES`

## Discussion

Adding this key to your project’s Info pane with a value of `YES` indicates your app supports a streamlined experience designed for Assistive Access. It allows your app’s UI to match the prominent style of Assistive Access controls. It also lists your app as Optimized for Assistive Access in Settings, so that a trusted supporter configuring Assistive Access on someone’s behalf knows that your app is optimized for this feature.

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
- [UISupportsFullScreenInAssistiveAccess](./uisupportsfullscreeninassistiveaccess.md)
  A Boolean value that indicates if an iOS or iPadOS app appears as full screen in Assistive Access.
- [NSPrefersDisplaySafeAreaCompatibilityMode](./nsprefersdisplaysafeareacompatibilitymode.md)
  A Boolean value that indicates whether the app prefers to run in compatibility mode when necessary.
- [NSAccentColorName](./nsaccentcolorname.md)
  The name of a color in an asset catalog to use for a target’s global accent color.
- [NSWidgetBackgroundColorName](./nswidgetbackgroundcolorname.md)
  The name of a color in an asset catalog to use for a widget’s configuration interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uisupportsassistiveaccess)*