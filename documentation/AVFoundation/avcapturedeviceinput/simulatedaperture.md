# simulatedAperture

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
var simulatedAperture: Float { get set }
```

#### Discussion

Shallow depth of field simulated aperture.

When capturing a Cinematic Video, use this property to control the amount of blur in the simulated depth of field effect.

This property only takes effect when cinematicVideoCaptureEnabled is set to YES.

Setting this property throws an NSRangeException if simulatedAperture is set to a value less than the AVCaptureDevice’s activeFormat.minSimulatedAperture or greater than the AVCaptureDevice’s activeFormat.maxSimulatedAperture. This property may only be set if AVCaptureDevice’s activeFormat.minSimulatedAperture returns a non-zero value, otherwise an NSInvalidArgumentException is thrown. This property can only be set before a Cinematic Video capture starts. An NSInvalidArgumentException is thrown if simulatedAperture is set when a Cinematic Video is being captured.

This property is initialized to the device.activeFormat’s defaultSimulatedAperture.

This property is key-value observable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/simulatedaperture)*