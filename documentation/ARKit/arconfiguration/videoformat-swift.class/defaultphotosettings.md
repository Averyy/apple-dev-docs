# defaultPhotoSettings

**Framework**: ARKit  
**Kind**: property

The default AVCapturePhotoSettings object that ARKit uses when capturing a high resolution frame using this video format.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
var defaultPhotoSettings: AVCapturePhotoSettings { get }
```

#### Return Value

An AVCapturePhotoSettings object.

#### Discussion

Calling this getter will return a new instance that may be mutated to customize settings. Pass that instance to `captureHighResolutionFrameUsingPhotoSettings:completion:` to capture a high resolution frame with custom settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/videoformat-swift.class/defaultphotosettings)*