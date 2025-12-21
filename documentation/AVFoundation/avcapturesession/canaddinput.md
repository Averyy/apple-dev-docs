# canAddInput(_:)

**Framework**: AVFoundation  
**Kind**: method

Determines whether you can add an input to a session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func canAddInput(_ input: AVCaptureInput) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if you can add the input to the session; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method returns [`false`](https://developer.apple.com/documentation/Swift/false) if you can’t add an input to a capture session. This occurs, for example, if you attempt to add the input to a session twice, or if the input already belongs to another capture session.

## Parameters

- `input`: An input to add to the session.

## See Also

- [var inputs: [AVCaptureInput]](avcapturesession/inputs.md)
  The inputs that provide media data to a capture session.
- [func addInput(AVCaptureInput)](avcapturesession/addinput(_:).md)
  Adds a capture input to the session.
- [func removeInput(AVCaptureInput)](avcapturesession/removeinput(_:).md)
  Removes an input from the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/canaddinput(_:))*