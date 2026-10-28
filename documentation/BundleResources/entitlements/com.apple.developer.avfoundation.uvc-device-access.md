# UVC Device Access on visionOS

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the app can stream USB UVC devices connected to the Developer strap.

**Availability**:
- visionOS 2.1+ - Deprecated in 26.0

## Details

- **Name**: `com.apple.developer.avfoundation.uvc-device-access`
- **Type**: boolean

## Discussion

On visionOS, your app must have the this entitlement to discover and use devices of type [`external`](../../AVFoundation/avcapturedevice/devicetype-swift.struct/external.md) using an [`AVCaptureDevice.DiscoverySession`](../../AVFoundation/avcapturedevice/discoverysession.md).

This feature only supports USB2 devices drawing a maximum 500mA and supports the use of up to 1 hub.

## See Also

### Enterprise
- [Increased performance headroom](./com.apple.developer.app-compute-category.md)
  An entitlement that allows an app to adjust thresholds that balance thermal dissipation and performance against fan noise and other factors.
- [Passthrough in screen capture](./com.apple.developer.screen-capture.include-passthrough.md)
  A Boolean value that indicates whether an app can include passthrough in screen capture.
- [Main camera access](./com.apple.developer.arkit.main-camera-access.allow.md)
  A Boolean value that indicates whether an app can use ARKit to access the main cameras on Apple Vision Pro.
- [Object-tracking parameter adjustment](./com.apple.developer.arkit.object-tracking-parameter-adjustment.allow.md)
  A Boolean value that allows an app to use ARKit to track more objects with a higher frequency.
- [Spatial barcode and QR code scanning](./com.apple.developer.arkit.barcode-detection.allow.md)
  A Boolean value that indicates whether an app can use ARKit to detect, position, and decode barcode and QR codes.
- [Camera Region access](./com.apple.developer.arkit.camera-region.allow.md)
  A Boolean value indicating whether your app may access the camera region.
- [Shared Coordinate Space access](./com.apple.developer.arkit.shared-coordinate-space.allow.md)
  A Boolean value indicating whether your app may use a shared coordinate space.
- [App-Protected Content](./com.apple.developer.protected-content.md)
  A Boolean value indicating whether the system prohibits capturing your app’s content.
- [Window Follow Mode](./com.apple.developer.window-body-follow.md)
  A Boolean value indicating whether your app’s windows will follow the person.
- [Apple Neural Engine access](./com.apple.developer.coreml.neural-engine-access.md)
  A Boolean value that indicates whether an app can use the Apple Neural Engine to speed up CoreML.
- [Visual Fidelity monitoring](./com.apple.developer.arkit.visual-fidelity.allow.md)
  A Boolean value that indicates whether your app can monitor visual fidelity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.avfoundation.uvc-device-access)*