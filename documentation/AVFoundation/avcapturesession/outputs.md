# outputs

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSArray<__kindof AVCaptureOutput *> * outputs;
```

## Discussion

You add new outputs to a capture session by calling its [`addOutput(_:)`](./addoutput%28_%29.md) method.

## See Also

### Configuring outputs
- [func canAddOutput(AVCaptureOutput) -> Bool](./canaddoutput%28_%29.md)
  Determines whether you can add an output to a session.
- [func addOutput(AVCaptureOutput)](./addoutput%28_%29.md)
  Adds an output to the capture session.
- [func removeOutput(AVCaptureOutput)](./removeoutput%28_%29.md)
  Removes an output from a capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/outputs)*