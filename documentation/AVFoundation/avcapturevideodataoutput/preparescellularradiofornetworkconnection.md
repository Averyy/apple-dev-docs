# preparesCellularRadioForNetworkConnection

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
var preparesCellularRadioForNetworkConnection: Bool { get set }
```

#### Discussion

Indicates whether the receiver should prepare the cellular radio for imminent network activity.

Apps that scan video data output buffers for information that will result in network activity (such as detecting a QRCode containing a URL) should set this property true to allow the cellular radio to prepare for an imminent network request. Enabling this property requires a lengthy reconfiguration of the capture render pipeline, so you should set this property to YES before calling -[AVCaptureSession startRunning].

Using this API requires your app to adopt the entitlement `com.apple.developer.avfoundation.video-data-output-prepares-cellular-radio-for-machine-readable-code-scanning`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput/preparescellularradiofornetworkconnection)*