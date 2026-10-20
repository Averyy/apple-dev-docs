# removeOutput(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeOutput:(AVCaptureOutput *) output;
```

#### Discussion

You can call this method while the session is running.

## Parameters

- `output`: An output to remove from the capture session.

## See Also

### Configuring outputs
- [var outputs: [AVCaptureOutput]](./outputs.md)
  The output destinations to which a captures session sends its data.
- [func canAddOutput(AVCaptureOutput) -> Bool](./canaddoutput%28_%29.md)
  Determines whether you can add an output to a session.
- [func addOutput(AVCaptureOutput)](./addoutput%28_%29.md)
  Adds an output to the capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/removeoutput(_:))*