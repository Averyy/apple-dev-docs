# inputs

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSArray<__kindof AVCaptureInput *> * inputs;
```

## Discussion

You add new inputs to a capture session by callings its [`addInput(_:)`](./addinput%28_%29.md) method.

## See Also

### Configuring inputs
- [func canAddInput(AVCaptureInput) -> Bool](./canaddinput%28_%29.md)
  Determines whether you can add an input to a session.
- [func addInput(AVCaptureInput)](./addinput%28_%29.md)
  Adds a capture input to the session.
- [func removeInput(AVCaptureInput)](./removeinput%28_%29.md)
  Removes an input from the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesession/inputs)*