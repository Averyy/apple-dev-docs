# Camera Region access

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating whether your app may access the camera region.

**Availability**:
- visionOS 26.0+ (Beta)

#### Discussion

Camera Region allows developers create a new SwiftUI element that acts as a frame that the user can place anywhere within their view, and then passes camera frames from that specified region back to the app for processing or display.  The region in space is fixed and stabilized, so if a user moves their head or looks around, they continue to get frames from the space they defined, as long as it is in their field of view.  Additionally, there is an optional configurable argument that enables image enhancement, providing a clearer and sharper version of the camera frames than the default camera frame provides.

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
- [Shared Coordinate Space access](entitlements/com.apple.developer.arkit.shared-coordinate-space.allow.md)
  A Boolean value indicating whether your app may use a shared coordinate space.
- [App-Protected Content](entitlements/com.apple.developer.protected-content.md)
  A Boolean value indicating whether the system prohibits capturing your app’s content.
- [Follow Mode for Windows](entitlements/com.apple.developer.window-body-follow.md)
  A Boolean value indicating whether your app’s windows will follow the user.
- [Apple Neural Engine access](entitlements/com.apple.developer.coreml.neural-engine-access.md)
  A Boolean value that indicates whether an app can use the Apple Neural Engine to speed up CoreML.
- [UVC Device Access on visionOS](entitlements/com.apple.developer.avfoundation.uvc-device-access.md)
  A Boolean value that indicates whether the app can stream USB UVC devices connected to the Developer strap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.arkit.camera-region.allow)*