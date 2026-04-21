# CADisableMinimumFrameDurationOnPhone

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that allows your app to access frame rates higher than the system’s default.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+



**Type**: boolean

**Default**: `NO`

#### Discussion

Devices with ProMotion displays allow apps to dynamically request a frame rate they prefer. If you set this key to `YES`, your app can request any frame rate the display supports. If you set this key to `NO`, frame rates higher than the system default are unavailable.

For more information on refresh rates, see [`Optimizing iPhone and iPad apps to support ProMotion displays`](https://developer.apple.com/documentation/QuartzCore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/cadisableminimumframedurationonphone)*