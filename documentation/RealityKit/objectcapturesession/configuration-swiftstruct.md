# ObjectCaptureSession.Configuration

**Framework**: RealityKit  
**Kind**: struct

The configuration options for the session which are passed into the `start(imagesDirectory:configuration:)` call.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Initializers
- [init()](objectcapturesession/configuration-swift.struct/init.md)
### Instance Properties
- [var checkpointDirectory: URL?](objectcapturesession/configuration-swift.struct/checkpointdirectory.md)
  An optional directory to store data about session progress which may be used to speed up on-device reconstruction by passing into the `PhotogrammetrySession.Configuration`. If you provide a value for `checkpointDirectory`, it also needs to point to an empty, writable directory. If the directory is not writable or already contains data, the session moves to the `.failed(Error)` state.
- [var isOverCaptureEnabled: Bool](objectcapturesession/configuration-swift.struct/isovercaptureenabled.md)
  Enables the session to continue capturing even after the number of captured images exceeds `maximumNumberOfInputImages`.  This setting is meant for use when the images are intended to be transferred to macOS for model reconstruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/configuration-swift.struct)*