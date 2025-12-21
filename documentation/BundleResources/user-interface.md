# User interface

**Framework**: Bundle Resources

Configure an app’s scenes, storyboards, icons, fonts, and other user interface elements.

#### Overview

You define the user interface that your app presents during normal operation with a combination of code and storyboards. However, the system needs to know a few things about your app’s user interface before execution begins. For example, on some platforms, you have to specify what device orientations your app supports and what the system should display while your app launches. You add keys to your app’s [`Information Property List`](information-property-list.md) file to control certain aspects of its user interface.

## Topics

### Main user interface
- [UIApplicationSceneManifest](information-property-list/uiapplicationscenemanifest.md)
  The information about the app’s scene-based life-cycle support.
- [UIApplicationPreferredDefaultSceneSessionRole](information-property-list/uiapplicationpreferreddefaultscenesessionrole.md)
  The preferred initial scene session role for your app.
- [NSMainStoryboardFile](information-property-list/nsmainstoryboardfile.md)
  The name of an app’s storyboard resource file.
- [UIMainStoryboardFile](information-property-list/uimainstoryboardfile.md)
  The name of the app’s main storyboard file.
- [NSMainNibFile](information-property-list/nsmainnibfile.md)
  The name of an app’s main user interface file.
- [LSUIElement](information-property-list/lsuielement.md)
  A Boolean value indicating whether the app is an agent app that runs in the background and doesn’t appear in the Dock.
- [UISupportsTrueScreenSizeOnMac](information-property-list/uisupportstruescreensizeonmac.md)
  A Boolean value that indicates whether your iPad app supports arbitrary screen sizes and resolutions when running on a Mac.
### Launch interface
- [UILaunchScreen](information-property-list/uilaunchscreen.md)
  The user interface to show while an app launches.
- [UILaunchScreens](information-property-list/uilaunchscreens.md)
  The user interfaces to show while an app launches in response to different URL schemes.
- [UILaunchStoryboardName](information-property-list/uilaunchstoryboardname.md)
  The filename of the storyboard from which to generate the app’s launch image.
- [UILaunchStoryboards](information-property-list/uilaunchstoryboards.md)
  The launch storyboard to use to generate a launch image when your app opens from a supported scheme.
- [LSUIPresentationMode](information-property-list/lsuipresentationmode.md)
  The initial user-interface mode for the app.
- [UILaunchToFullScreenByDefaultOnMac](information-property-list/uilaunchtofullscreenbydefaultonmac.md)
  A Boolean value that indicates whether to launch your iPad app in full-screen mode when running on a Mac.
### Icons
- [CFBundleIcons](information-property-list/cfbundleicons.md)
  Information about all of the icons used by the app.
- [CFBundleIconFiles](information-property-list/cfbundleiconfiles.md)
  The names of the bundle’s icon image files.
- [CFBundleIconFile](information-property-list/cfbundleiconfile.md)
  The file containing the bundle’s icon.
- [CFBundleIconName](information-property-list/cfbundleiconname.md)
  The name of the asset that represents the app icon.
- [UIPrerenderedIcon](information-property-list/uiprerenderedicon.md)
  A Boolean value that indicates whether the app’s icon contains a shine effect.
### Orientation
- [UIInterfaceOrientation](information-property-list/uiinterfaceorientation.md)
  The initial orientation of the app’s user interface.
- [UISupportedInterfaceOrientations](information-property-list/uisupportedinterfaceorientations.md)
  The interface orientations supported by your app.
- [UIPreferredDefaultInterfaceOrientation](information-property-list/uipreferreddefaultinterfaceorientation.md)
  A string that indicates the preferred initial interface orientation for iPad and iPhone apps running on visionOS.
### Styling
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
- [UISupportsFullScreenInAssistiveAccess](information-property-list/uisupportsfullscreeninassistiveaccess.md)
  A Boolean value that indicates if an iOS or iPadOS app appears as full screen in Assistive Access.
- [NSPrefersDisplaySafeAreaCompatibilityMode](information-property-list/nsprefersdisplaysafeareacompatibilitymode.md)
  A Boolean value that indicates whether the app prefers to run in compatibility mode when necessary.
- [NSAccentColorName](information-property-list/nsaccentcolorname.md)
  The name of a color in an asset catalog to use for a target’s global accent color.
- [NSWidgetBackgroundColorName](information-property-list/nswidgetbackgroundcolorname.md)
  The name of a color in an asset catalog to use for a widget’s configuration interface.
### Fonts
- [ATSApplicationFontsPath](information-property-list/atsapplicationfontspath.md)
  The location of a font file or folder of fonts in the bundle’s Resources folder.
- [UIAppFonts](information-property-list/uiappfonts.md)
  App-specific font files located in the bundle and that the system loads at runtime.
### Status bar
- [UIStatusBarHidden](information-property-list/uistatusbarhidden.md)
  A Boolean value that indicates whether the system initially hides the status bar when the app launches.
- [UIStatusBarStyle](information-property-list/uistatusbarstyle.md)
  The style of the status bar as the app launches.
- [UIStatusBarTintParameters](information-property-list/uistatusbartintparameters.md)
  The status bar tint.
- [UIViewControllerBasedStatusBarAppearance](information-property-list/uiviewcontrollerbasedstatusbarappearance.md)
  A Boolean value that indicates whether the system bases the appearance of the status bar on the style preferred by the current view controller.
### Text fields
- [NSAutoFillRequiresTextContentTypeForOneTimeCodeOnMac](information-property-list/nsautofillrequirestextcontenttypeforonetimecodeonmac.md)
  A Boolean value that indicates whether text fields receive AutoFill of one-time codes only if they adopt the suitable content type.
### Pointer interactions
- [UIApplicationSupportsIndirectInputEvents](information-property-list/uiapplicationsupportsindirectinputevents.md)
  A Boolean value indicating that the app generally supports indirect input mechanisms.
### Preferences
- [NSPrefPaneIconFile](information-property-list/nsprefpaneiconfile.md)
  The name of an image file used to represent a preference pane in the System Preferences app.
- [NSPrefPaneIconLabel](information-property-list/nsprefpaneiconlabel.md)
  The name of a preference pane displayed beneath the preference pane icon in the System Preferences app.
### Graphics
- [UIAppSupportsHDR](information-property-list/uiappsupportshdr.md)
  A Boolean value that indicates whether the app supports HDR mode on Apple TV 4K.
- [NSHighResolutionCapable](information-property-list/nshighresolutioncapable.md)
  A Boolean value indicating whether the Cocoa app supports high-resolution displays.
- [NSSupportsAutomaticGraphicsSwitching](information-property-list/nssupportsautomaticgraphicsswitching.md)
  A Boolean value indicating whether an OpenGL app may utilize the integrated GPU.
- [GPUEjectPolicy](information-property-list/gpuejectpolicy.md)
  The preferred system action when an external GPU is connected from the system.
- [GPUSelectionPolicy](information-property-list/gpuselectionpolicy.md)
  The app’s preference for whether it wants to use external graphics processors.
### QuickLook
- [QLNeedsToBeRunInMainThread](information-property-list/qlneedstoberuninmainthread.md)
  A Boolean value indicating whether a Quick Look app’s generator can be run in threads other than the main thread.
- [QLPreviewHeight](information-property-list/qlpreviewheight.md)
  A hint at the height, in points, of a Quick Look app’s previews.
- [QLPreviewWidth](information-property-list/qlpreviewwidth.md)
  A hint at the width, in points, of a Quick Look app’s previews.
- [QLSupportsConcurrentRequests](information-property-list/qlsupportsconcurrentrequests.md)
  A Boolean value indicating whether a Quick Look app’s  generator can handle concurrent thumbnail and preview requests.
- [QLThumbnailMinimumSize](information-property-list/qlthumbnailminimumsize.md)
  The minimum size, in points, along one dimension of thumbnails for a Quick Look app’s generator.
### Automatic observation tracking
- [NSObservationTrackingEnabled](information-property-list/nsobservationtrackingenabled.md)
  A Boolean value that indicates whether the system automatically tracks changes to observable objects in macOS 15.
- [UIObservationTrackingEnabled](information-property-list/uiobservationtrackingenabled.md)
  A Boolean value that indicates whether the system automatically tracks changes to observable objects in iOS 18.
### Deprecated keys
- [UILaunchImages](information-property-list/uilaunchimages.md)
  A dictionary containing information about launch images.
- [UIRequiresFullScreen](information-property-list/uirequiresfullscreen.md)
  A Boolean value that indicates whether the system puts an iPad app into a compatibility mode that opts the app out of multitasking and dynamic resizing.

## See Also

- [Bundle configuration](bundle-configuration.md)
  Define basic characteristics of a bundle, like its name, type, and version.
- [App execution](app-execution.md)
  Control app launch, execution, and termination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/user-interface)*