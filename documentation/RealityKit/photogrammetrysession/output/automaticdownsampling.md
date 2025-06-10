# PhotogrammetrySession.Output.automaticDownsampling

**Framework**: RealityKit  
**Kind**: case

The session reduced the image size because of memory constraints.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
case automaticDownsampling
```

#### Discussion

If [`PhotogrammetrySession`](photogrammetrysession.md) encounters serious resource constraints during the object-creation process, it attempts to reduce memory usage by creating scaled-down copies of the sample images, and publishes this message.

## See Also

- [PhotogrammetrySession.Output.invalidSample(id:reason:)](photogrammetrysession/output/invalidsample(id:reason:).md)
  A provided sample was invalid.
- [PhotogrammetrySession.Output.skippedSample(id:)](photogrammetrysession/output/skippedsample(id:).md)
  The type of element used for Object Capture updates. The [`PhotogrammetrySample`](photogrammetrysample.md) with the [`id`](photogrammetrysample/id.md) indicated was not able to be used for reconstruction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/output/automaticdownsampling)*