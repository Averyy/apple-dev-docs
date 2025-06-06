# UVC Device Access on visionOS

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app can stream USB UVC devices connected to the Developer strap.

**Availability**:
- visionOS 2.1+

#### Discussion

On visionOS, your app must have the this entitlement to discover and use devices of type [`external`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/DeviceType-swift.struct/external) using an [`AVCaptureDevice.DiscoverySession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureDevice/DiscoverySession).

This feature only supports USB2 devices drawing a maximum 500mA and supports the use of up to 1 hub.

## See Also

- [Apple Neural Engine access](entitlements/com.apple.developer.coreml.neural-engine-access.md)
  A Boolean value that indicates whether an app can use the Apple Neural Engine to speed up CoreML.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.avfoundation.uvc-device-access)*