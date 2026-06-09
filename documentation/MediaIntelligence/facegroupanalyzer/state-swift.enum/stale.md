# FaceGroupAnalyzer.State.stale

**Framework**: Media Intelligence  
**Kind**: case

A state that indicates new faces need cluster assignments.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
case stale
```

## Mentions

- [Detecting and grouping faces in images](detecting-and-grouping-faces-in-images.md)

#### Discussion

Call [`update(subprogress:)`](facegroupanalyzer/update(subprogress:).md) to assign them to entities.

## See Also

- [FaceGroupAnalyzer.State.ready](facegroupanalyzer/state-swift.enum/ready.md)
  A state that indicates all faces have up-to-date cluster assignments.
- [FaceGroupAnalyzer.State.updating](facegroupanalyzer/state-swift.enum/updating.md)
  A state that indicates the clustering algorithm is running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/state-swift.enum/stale)*