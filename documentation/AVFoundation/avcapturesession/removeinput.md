# removeInput(_:)

**Framework**: AVFoundation  
**Kind**: method

Removes an input from the session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func removeInput(_ input: AVCaptureInput)
```

#### Discussion

You can invoke this method while the session is running.

## Parameters

- `input`: An input to remove from the capture session.

## See Also

- [var inputs: [AVCaptureInput]](avcapturesession/inputs.md)
  The inputs that provide media data to a capture session.
- [func canAddInput(AVCaptureInput) -> Bool](avcapturesession/canaddinput(_:).md)
  Determines whether you can add an input to a session.
- [func addInput(AVCaptureInput)](avcapturesession/addinput(_:).md)
  Adds a capture input to the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/removeinput(_:))*