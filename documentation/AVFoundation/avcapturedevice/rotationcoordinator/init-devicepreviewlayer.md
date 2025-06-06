# init(device:previewLayer:)

**Framework**: AVFoundation  
**Kind**: init

Creates a coordinator that provides separate compensation angles for content your app takes with a capture device, and for your app’s camera preview.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
init(device: AVCaptureDevice, previewLayer: CALayer?)
```

## Parameters

- `device`: A capture device the new coordinator monitors to track its physical rotation to calculate its   property.
- `previewLayer`: A layer that displays a camera preview the new coordinator monitors to calculate its   property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator/init(device:previewlayer:))*