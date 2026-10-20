# canAddInput(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) canAddInput:(AVCaptureInput *) input;
```

#### Return Value

[`true`](../../Swift/true.md) if you can add the input to the session; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method returns [`false`](../../Swift/false.md) if you can’t add an input to a capture session. This occurs, for example, if you attempt to add the input to a session twice, or if the input already belongs to another capture session.

## Parameters

- `input`: An input to add to the session.

## See Also

### Configuring inputs
- [var inputs: [AVCaptureInput]](./inputs.md)
  The inputs that provide media data to a capture session.
- [func addInput(AVCaptureInput)](./addinput%28_%29.md)
  Adds a capture input to the session.
- [func removeInput(AVCaptureInput)](./removeinput%28_%29.md)
  Removes an input from the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/canaddinput(_:))*