# defaultPhotoSettings

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The default AVCapturePhotoSettings object that ARKit uses when capturing a high resolution frame using this video format.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var defaultPhotoSettings: AVCapturePhotoSettings { get }
```

```objc
@property (nonatomic, readonly) AVCapturePhotoSettings * defaultPhotoSettings;
```

## Return Value

An `AVCapturePhotoSettings` object.

## Discussion

Calling this getter will return a new instance that may be mutated to customize settings. Pass that instance to `captureHighResolutionFrameUsingPhotoSettings:completion:` to capture a high resolution frame with custom settings.

> **See Also**: [`captureHighResolutionFrame(using:completion:)`](../../arsession/capturehighresolutionframe%28using,completion%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/videoformat-swift.class/defaultphotosettings)*