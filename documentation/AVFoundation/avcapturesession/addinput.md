# addInput(_:)

**Framework**: AVFoundation  
**Kind**: method

Adds a capture input to the session.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func addInput(_ input: AVCaptureInput)
```

#### Discussion

It’s only valid to call this method if [`canAddInput(_:)`](avcapturesession/canaddinput(_:).md) returns [`true`](https://developer.apple.com/documentation/Swift/true).

You can invoke this method while the session is running.

## Parameters

- `input`: An input to add to the session.

## See Also

- [var inputs: [AVCaptureInput]](avcapturesession/inputs.md)
  The inputs that provide media data to a capture session.
- [func canAddInput(AVCaptureInput) -> Bool](avcapturesession/canaddinput(_:).md)
  Determines whether you can add an input to a session.
- [func removeInput(AVCaptureInput)](avcapturesession/removeinput(_:).md)
  Removes an input from the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/addinput(_:))*