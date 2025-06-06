# removeOutput(_:)

**Framework**: AVFoundation  
**Kind**: method

Removes an output from a capture session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func removeOutput(_ output: AVCaptureOutput)
```

#### Discussion

You can call this method while the session is running.

## Parameters

- `output`: An output to remove from the capture session.

## See Also

- [var outputs: [AVCaptureOutput]](avcapturesession/outputs.md)
  The output destinations to which a captures session sends its data.
- [func canAddOutput(AVCaptureOutput) -> Bool](avcapturesession/canaddoutput(_:).md)
  Determines whether you can add an output to a session.
- [func addOutput(AVCaptureOutput)](avcapturesession/addoutput(_:).md)
  Adds an output to the capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/removeoutput(_:))*