# currentFrame

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The most recent still frame captured by the active camera feed, including ARKit’s interpretation of it.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
@NSCopying
var currentFrame: ARFrame? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) ARFrame * currentFrame;
```

## Mentions

- [Displaying an AR Experience with Metal](../displaying-an-ar-experience-with-metal.md)

## See Also

### Accessing the camera frame
- [class ARFrame](../arframe.md)
  A video image captured as part of a session with position-tracking information.
- [func captureHighResolutionFrame(completion: (ARFrame?, (any Error)?) -> Void)](./capturehighresolutionframe%28completion%29.md)
  Requests a frame outside of the normal frequency that contains a high-resolution captured image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/currentframe)*