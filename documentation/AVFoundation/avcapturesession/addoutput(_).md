# addOutput(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Adds an output to the capture session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func addOutput(_ output: AVCaptureOutput)
```

```objc
- (void) addOutput:(AVCaptureOutput *) output;
```

## Discussion

You can only add an output to a session using this method if [`canAddOutput(_:)`](./canaddoutput%28_%29.md) returns [`true`](../../Swift/true.md).

You can invoke this method while the session is running.

## Parameters

- `output`: An output to add to the session.

## See Also

### Configuring outputs
- [var outputs: [AVCaptureOutput]](./outputs.md)
  The output destinations to which a captures session sends its data.
- [func canAddOutput(AVCaptureOutput) -> Bool](./canaddoutput%28_%29.md)
  Determines whether you can add an output to a session.
- [func removeOutput(AVCaptureOutput)](./removeoutput%28_%29.md)
  Removes an output from a capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/addoutput(_:))*