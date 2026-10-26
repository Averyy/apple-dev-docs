# init(device:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates an input for the specified capture device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(device: AVCaptureDevice) throws
```

```objc
- (instancetype) initWithDevice:(AVCaptureDevice *) device error:(NSError **) outError;
```

## Parameters

- `device`: A device from which to capture media.

## See Also

### Creating an input
- [+ deviceInputWithDevice:error:](./deviceinputwithdevice_error_.md)
  Returns a new input for the specified capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/init(device:))*