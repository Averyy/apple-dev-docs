# NSPrefersDisplaySafeAreaCompatibilityMode

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the app prefers to run in compatibility mode when necessary.

**Availability**:
- macOS 12.0+

## Details

- **Name**: `NSPrefersDisplaySafeAreaCompatibilityMode`
- **Type**: boolean

#### Discussion

On Mac computers that include a camera housing in the screen bezel, the system provides a compatibility mode to prevent apps from unintentionally putting content in the region the housing occupies. When this mode is active, the system changes the active area of the display to avoid the camera housing. The new active area ensures your app’s contents are always visible and not obscured by the camera housing. The system activates this compatibility mode when an app that requires it places a window behind the camera housing in the current desktop or full-screen space.

On Mac computers that include a camera housing, the Finder adds a checkbox to your app’s Get Info panel to enable or disable compatibility mode. If your app’s `Info.plist` file includes the [`NSPrefersDisplaySafeAreaCompatibilityMode`](./nsprefersdisplaysafeareacompatibilitymode.md) key, the Finder doesn’t add that checkbox; instead, it uses the value of the key to determine whether to run your app in compatibility mode. Set the value of the key to [`true`](../../Swift/true.md) to always run your app in compatibility mode, and set it to [`false`](../../Swift/false.md) to never run your app in compatibility mode.

After you audit your app and verify that it runs correctly on Mac computers that include a camera housing, add this key to your `Info.plist` file and set its value to [`false`](../../Swift/false.md). If you discover issues during your audit, add the key and set its value to [`true`](../../Swift/true.md) until you’re able to fix those issues.

> **Note**:  On Mac computers that include a camera housing in the bezel, the [`auxiliaryTopLeftArea`](../../AppKit/nsscreen/auxiliarytopleftarea-uglc.md) and [`auxiliaryTopRightArea`](../../AppKit/nsscreen/auxiliarytoprightarea-gr2n.md) properties of [`NSScreen`](../../AppKit/nsscreen.md) contain the regions to the left and right of the camera housing. Use those properties and the [`visibleFrame`](../../AppKit/nsscreen/visibleframe.md) property to determine where to display your content.

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
- [NSAccentColorName](./nsaccentcolorname.md)
  The name of a color in an asset catalog to use for a target’s global accent color.
- [NSWidgetBackgroundColorName](./nswidgetbackgroundcolorname.md)
  The name of a color in an asset catalog to use for a widget’s configuration interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsprefersdisplaysafeareacompatibilitymode)*