# currentFrame

**Framework**: ARKit  
**Kind**: property

The most recent still frame captured by the active camera feed, including ARKit’s interpretation of it.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@NSCopying
var currentFrame: ARFrame? { get }
```

## Mentions

- [Displaying an AR Experience with Metal](displaying-an-ar-experience-with-metal.md)

## See Also

- [class ARFrame](arframe.md)
  A video image captured as part of a session with position-tracking information.
- [func captureHighResolutionFrame(completion: (ARFrame?, (any Error)?) -> Void)](arsession/capturehighresolutionframe(completion:).md)
  Requests a frame outside of the normal frequency that contains a high-resolution captured image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/currentframe)*