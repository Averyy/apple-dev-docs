# GPUSelectionPolicy

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The app’s preference for whether it wants to use external graphics processors.

**Availability**:
- macOS 10.14+

## Details

- **Name**: `GPUSelectionPolicy`
- **Type**: string

## Possible Values

- `avoidRemovable`: Metal tries to avoid creating contexts on external GPUs. For legacy OpenGL apps, OpenGL also avoids creating contexts using external GPUs. Set this option only if your app doesn’t support external GPU event handling.
- `preferRemovable`: If external GPUs are visible to the system, Metal prefers them over other GPUs. Similarly, for legacy OpenGL apps, OpenGL also prefers to create contexts on the external GPU.

## Discussion

This key is optional.

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
- [CADisableMinimumFrameDurationOnPhone](./cadisableminimumframedurationonphone.md)
  A Boolean value that allows your app to access frame rates higher than the system’s default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/gpuselectionpolicy)*