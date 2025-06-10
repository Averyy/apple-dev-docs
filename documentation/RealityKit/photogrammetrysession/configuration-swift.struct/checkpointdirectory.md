# checkpointDirectory

**Framework**: RealityKit  
**Kind**: property

The directory that a the photogrammetry session uses for checkpoints during reconstruction.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
var checkpointDirectory: URL?
```

#### Discussion

For macOS reconstruction, the `checkpointDirectory` serves as a temporary reconstruction space if it is not `nil`. Reconstruction starts from scratch, and does not resume from previous checkpoints.

For iOS reconstruction, if you pass the same `checkpointDirectory` used by an [`ObjectCaptureSession`](objectcapturesession.md) or an earlier interrupted [`PhotogrammetrySession`](photogrammetrysession.md), the [`PhotogrammetrySession`](photogrammetrysession.md) tries to use the saved checkpoint instead of starting from scratch. Ensure that each `checkpointDirectory` is unique for each images folder.

If set to an empty folder, the `checkpointDirectory` saves checkpoints during processing for reuse in a subsequent restart. If it is `nil`, the session does not use or save checkpoints, and every reconstruction starts from scratch.

If a `checkpointDirectory` is has a non-nil value, but the latest checkpoint is not compatible with the images folder or other configuration settings, the session starts from scratch and writes new checkpoints to this folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/configuration-swift.struct/checkpointdirectory)*