# deviceInputWithDevice:error:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a new input for the specified capture device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+

## Declaration

```objc
+ (instancetype) deviceInputWithDevice:(AVCaptureDevice *) device error:(NSError **) outError;
```

#### Return Value

A new capture input.

## Parameters

- `device`: The device from which to capture input.
- `outError`: If an error occurs during initialization, upon return contains an `NSError` object describing the problem.

## See Also

### Creating an input
- [init(device: AVCaptureDevice) throws](./init%28device%29.md)
  Creates an input for the specified capture device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/deviceinputwithdevice:error:)*