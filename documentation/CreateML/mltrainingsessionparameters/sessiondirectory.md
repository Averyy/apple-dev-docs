# sessionDirectory

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The location in the file system where the session stores its progress.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
let sessionDirectory: URL?
```

## See Also

### Configuring the session’s parameters
- [var reportInterval: Int](./reportinterval.md)
  The number of iterations the session completes before it reports its progress.
- [var checkpointInterval: Int](./checkpointinterval.md)
  The number of iterations the session completes before it saves a checkpoint.
- [var iterations: Int](./iterations.md)
  The maximum number of iterations for the training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/sessiondirectory)*