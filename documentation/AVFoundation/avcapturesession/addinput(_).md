# addInput(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addInput:(AVCaptureInput *) input;
```

## Discussion

It’s only valid to call this method if [`canAddInput(_:)`](./canaddinput%28_%29.md) returns [`true`](../../Swift/true.md).

You can invoke this method while the session is running.

## Parameters

- `input`: An input to add to the session.

## See Also

### Configuring inputs
- [var inputs: [AVCaptureInput]](./inputs.md)
  The inputs that provide media data to a capture session.
- [func canAddInput(AVCaptureInput) -> Bool](./canaddinput%28_%29.md)
  Determines whether you can add an input to a session.
- [func removeInput(AVCaptureInput)](./removeinput%28_%29.md)
  Removes an input from the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/addinput(_:))*