# inputs

**Framework**: AVFoundation  
**Kind**: property

The inputs that provide media data to a capture session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var inputs: [AVCaptureInput] { get }
```

#### Discussion

You add new inputs to a capture session by callings its [`addInput(_:)`](avcapturesession/addinput(_:).md) method.

## See Also

- [func canAddInput(AVCaptureInput) -> Bool](avcapturesession/canaddinput(_:).md)
  Determines whether you can add an input to a session.
- [func addInput(AVCaptureInput)](avcapturesession/addinput(_:).md)
  Adds a capture input to the session.
- [func removeInput(AVCaptureInput)](avcapturesession/removeinput(_:).md)
  Removes an input from the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/inputs)*