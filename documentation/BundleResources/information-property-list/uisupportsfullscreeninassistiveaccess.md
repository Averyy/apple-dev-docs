# UISupportsFullScreenInAssistiveAccess

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates if an iOS or iPadOS app appears as full screen in Assistive Access.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

#### Discussion

Adding this key to your app’s `Info.plist` file with a value of `YES` allows your app’s UI to expand into all the available space above the Back button in Assistive Access. It also lists your app as Optimized for Assistive Access in Settings, so that a trusted supporter configuring Assistive Access on someone’s behalf knows that your app’s UI is optimized for this feature.

![An image of iPad and iPhone devices that show the Home Screen in Assistive Access with five apps: Music, Calls, Messages, Photos, and Camera. The iPad shows the apps in a grid layout, and the iPhone shows the apps in a list layout.](https://docs-assets.developer.apple.com/published/16c0a6aec93431d594e59a2b6de74896/media-4403388%402x.png)

For more information, read [`Optimizing your app for Assistive Access`](https://developer.apple.com/documentation/Accessibility/optimizing-your-app-for-assistive-access).

## See Also

- [Assistive Access](../Accessibility/assistive-access.md)
  A mode that tailors the iOS and iPadOS experience for people with cognitive disabilities.
- [Optimizing your app for Assistive Access](../Accessibility/optimizing-your-app-for-assistive-access.md)
  Adjust your app’s UI to make sure it works well for people who use Assistive Access.
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
- [UIRequiresFullScreenIgnoredStartingWithVersion](information-property-list/uirequiresfullscreenignoredstartingwithversion.md)
  A string value that specifies a system version after which the system ignores the requires full screen key.
- [UISupportsAssistiveAccess](information-property-list/uisupportsassistiveaccess.md)
  A Boolean value that indicates if an iOS or iPadOS app supports Assistive Access.
- [NSPrefersDisplaySafeAreaCompatibilityMode](information-property-list/nsprefersdisplaysafeareacompatibilitymode.md)
  A Boolean value that indicates whether the app prefers to run in compatibility mode when necessary.
- [NSAccentColorName](information-property-list/nsaccentcolorname.md)
  The name of a color in an asset catalog to use for a target’s global accent color.
- [NSWidgetBackgroundColorName](information-property-list/nswidgetbackgroundcolorname.md)
  The name of a color in an asset catalog to use for a widget’s configuration interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uisupportsfullscreeninassistiveaccess)*