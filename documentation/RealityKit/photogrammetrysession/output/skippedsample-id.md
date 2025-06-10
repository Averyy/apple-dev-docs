# PhotogrammetrySession.Output.skippedSample(id:)

**Framework**: RealityKit  
**Kind**: case

The type of element used for Object Capture updates. The [`PhotogrammetrySample`](photogrammetrysample.md) with the [`id`](photogrammetrysample/id.md) indicated was not able to be used for reconstruction.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
case skippedSample(id: Int)
```

## See Also

- [PhotogrammetrySession.Output.invalidSample(id:reason:)](photogrammetrysession/output/invalidsample(id:reason:).md)
  A provided sample was invalid.
- [PhotogrammetrySession.Output.automaticDownsampling](photogrammetrysession/output/automaticdownsampling.md)
  The session reduced the image size because of memory constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/output/skippedsample(id:))*