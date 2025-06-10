# PhotogrammetrySession.Output.invalidSample(id:reason:)

**Framework**: RealityKit  
**Kind**: case

A provided sample was invalid.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
case invalidSample(id: Int, reason: String)
```

## Parameters

- `id`: The sample ID.
- `reason`: The reason the sample is invalid.

## See Also

- [PhotogrammetrySession.Output.automaticDownsampling](photogrammetrysession/output/automaticdownsampling.md)
  The session reduced the image size because of memory constraints.
- [PhotogrammetrySession.Output.skippedSample(id:)](photogrammetrysession/output/skippedsample(id:).md)
  The type of element used for Object Capture updates. The [`PhotogrammetrySample`](photogrammetrysample.md) with the [`id`](photogrammetrysample/id.md) indicated was not able to be used for reconstruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/output/invalidsample(id:reason:))*