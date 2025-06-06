# outputs

**Framework**: AVFoundation  
**Kind**: property

The output destinations to which a captures session sends its data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var outputs: [AVCaptureOutput] { get }
```

#### Discussion

You add new outputs to a capture session by calling its [`addOutput(_:)`](avcapturesession/addoutput(_:).md) method.

## See Also

- [func canAddOutput(AVCaptureOutput) -> Bool](avcapturesession/canaddoutput(_:).md)
  Determines whether you can add an output to a session.
- [func addOutput(AVCaptureOutput)](avcapturesession/addoutput(_:).md)
  Adds an output to the capture session.
- [func removeOutput(AVCaptureOutput)](avcapturesession/removeoutput(_:).md)
  Removes an output from a capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/outputs)*