# maximumNumberOfInputImages

**Framework**: RealityKit  
**Kind**: property

The maximum number of images that can be used for on-device reconstruction.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

## Declaration

```swift
@MainActor
var maximumNumberOfInputImages: Int { get }
```

#### Discussion

Note: the session will stop capturing images when this limit is reached unless [`isOverCaptureEnabled`](objectcapturesession/configuration-swift.struct/isovercaptureenabled.md) is true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/objectcapturesession/maximumnumberofinputimages)*