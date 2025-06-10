# Follow Mode for Windows

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether your app’s windows will follow the user.

**Availability**:
- visionOS 26.0+ (Beta)

#### Discussion

When the user installs an app that has the Follow Mode for Windows entitlement configured, all standard windows on Vision Pro (windows which include all standard chrome, such as the grabber bar and close ‘x’ button) across all apps on the system have the Follow Mode permission enabled on them.  When Follow Mode is enabled for a window, it locks itself in place relative to the user’s body.  When the user then moves to a new location, the window will follow along with them, and then “land” itself in the same place relative to their body as when they enabled Follow Mode for that window.

## See Also

- [Increased performance headroom](entitlements/com.apple.developer.app-compute-category.md)
  An entitlement that allows an app to adjust thresholds that balance thermal dissipation and performance against fan noise and other factors.
- [Passthrough in screen capture](entitlements/com.apple.developer.screen-capture.include-passthrough.md)
  A Boolean value that indicates whether an app can include passthrough in screen capture.
- [Main camera access](entitlements/com.apple.developer.arkit.main-camera-access.allow.md)
  A Boolean value that indicates whether an app can use ARKit to access the main cameras on Apple Vision Pro.
- [Object-tracking parameter adjustment](entitlements/com.apple.developer.arkit.object-tracking-parameter-adjustment.allow.md)
  A Boolean value that allows an app to use ARKit to track more objects with a higher frequency.
- [Spatial barcode and QR code scanning](entitlements/com.apple.developer.arkit.barcode-detection.allow.md)
  A Boolean value that indicates whether an app can use ARKit to detect, position, and decode barcode and QR codes.
- [Camera Region access](entitlements/com.apple.developer.arkit.camera-region.allow.md)
  A Boolean value indicating whether your app may access the camera region.
- [Shared Coordinate Space access](entitlements/com.apple.developer.arkit.shared-coordinate-space.allow.md)
  A Boolean value indicating whether your app may use a shared coordinate space.
- [App-Protected Content](entitlements/com.apple.developer.protected-content.md)
  A Boolean value indicating whether the system prohibits capturing your app’s content.
- [Apple Neural Engine access](entitlements/com.apple.developer.coreml.neural-engine-access.md)
  A Boolean value that indicates whether an app can use the Apple Neural Engine to speed up CoreML.
- [UVC Device Access on visionOS](entitlements/com.apple.developer.avfoundation.uvc-device-access.md)
  A Boolean value that indicates whether the app can stream USB UVC devices connected to the Developer strap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.window-body-follow)*