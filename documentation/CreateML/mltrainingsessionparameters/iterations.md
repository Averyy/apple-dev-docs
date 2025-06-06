# iterations

**Framework**: Create ML  
**Kind**: property

The maximum number of iterations for the training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var iterations: Int
```

#### Discussion

Each iteration represents a full pass over the training data, also known as an epoch. Training may stop with fewer iterations if training converges. This limit also affects resumed training sessions. To extend training beyond the original limit, increase the limit before resuming.

## See Also

- [let sessionDirectory: URL?](mltrainingsessionparameters/sessiondirectory.md)
  The location in the file system where the session stores its progress.
- [var reportInterval: Int](mltrainingsessionparameters/reportinterval.md)
  The number of iterations the session completes before it reports its progress.
- [var checkpointInterval: Int](mltrainingsessionparameters/checkpointinterval.md)
  The number of iterations the session completes before it saves a checkpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltrainingsessionparameters/iterations)*