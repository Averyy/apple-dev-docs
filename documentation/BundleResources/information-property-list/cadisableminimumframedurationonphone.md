# CADisableMinimumFrameDurationOnPhone

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that allows your app to access frame rates higher than the system’s default.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Details

- **Name**: `CADisableMinimumFrameDurationOnPhone` (Disable Minimum Frame Duration on Phone)
- **Type**: boolean



**Default**: `NO`

## Discussion

Devices with ProMotion displays allow apps to dynamically request a frame rate they prefer. If you set this key to `YES`, your app can request any frame rate the display supports. If you set this key to `NO`, frame rates higher than the system default are unavailable.

For more information on refresh rates, see [Optimizing iPhone and iPad apps to support ProMotion displays](../../QuartzCore/optimizing-iphone-and-ipad-apps-to-support-promotion-displays.md).

## See Also

### Graphics
- [UIAppSupportsHDR](./uiappsupportshdr.md)
  A Boolean value that indicates whether the app supports HDR mode on Apple TV 4K.
- [NSHighResolutionCapable](./nshighresolutioncapable.md)
  A Boolean value indicating whether the Cocoa app supports high-resolution displays.
- [NSSupportsAutomaticGraphicsSwitching](./nssupportsautomaticgraphicsswitching.md)
  A Boolean value indicating whether an OpenGL app may utilize the integrated GPU.
- [GPUEjectPolicy](./gpuejectpolicy.md)
  The preferred system action when an external GPU is connected from the system.
- [GPUSelectionPolicy](./gpuselectionpolicy.md)
  The app’s preference for whether it wants to use external graphics processors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/cadisableminimumframedurationonphone)*