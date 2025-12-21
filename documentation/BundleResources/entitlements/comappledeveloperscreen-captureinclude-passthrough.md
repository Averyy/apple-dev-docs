# Passthrough in screen capture

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether an app can include passthrough in screen capture.

**Availability**:
- visionOS 2.0+

#### Discussion

To optimize the viewing of displayed content for passthrough, Apple Vision Pro adjusts its refresh rate to 90 Hz, 96 Hz, or 100 Hz to account for physical environment changes, such as lighting. A flicker sensor and visionOS algorithms work to reduce passthrough artifacts, especially those that can be seen on physical displays due to varying lighting conditions. Apps don’t affect passthrough latency.

## See Also

- [Increased performance headroom](entitlements/com.apple.developer.app-compute-category.md)
  An entitlement that allows an app to adjust thresholds that balance thermal dissipation and performance against fan noise and other factors.
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
- [Window Follow Mode](entitlements/com.apple.developer.window-body-follow.md)
  A Boolean value indicating whether your app’s windows will follow the person.
- [Apple Neural Engine access](entitlements/com.apple.developer.coreml.neural-engine-access.md)
  A Boolean value that indicates whether an app can use the Apple Neural Engine to speed up CoreML.
- [UVC Device Access on visionOS](entitlements/com.apple.developer.avfoundation.uvc-device-access.md)
  A Boolean value that indicates whether the app can stream USB UVC devices connected to the Developer strap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.screen-capture.include-passthrough)*