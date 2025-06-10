# checkpointDirectory

**Framework**: RealityKit  
**Kind**: property

An optional directory to store data about session progress which may be used to speed up on-device reconstruction by passing into the `PhotogrammetrySession.Configuration`. If you provide a value for `checkpointDirectory`, it also needs to point to an empty, writable directory. If the directory is not writable or already contains data, the session moves to the `.failed(Error)` state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
var checkpointDirectory: URL?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/configuration-swift.struct/checkpointdirectory)*