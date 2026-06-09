# entityID

**Framework**: Media Intelligence  
**Kind**: property

An identifier for the entity this face belongs to.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let entityID: FaceGroupAnalyzer.Entity.ID?
```

## Mentions

- [Detecting and grouping faces in images](detecting-and-grouping-faces-in-images.md)

#### Discussion

This value is `nil` until you call [`update(subprogress:)`](facegroupanalyzer/update(subprogress:).md). After clustering runs, every face receives an entity identifier that groups it with other faces of the same person.

## See Also

- [let id: FaceGroupAnalyzer.Face.ID](facegroupanalyzer/face/id-swift.property.md)
  A unique identifier for the face.
- [let assetID: MediaIntelligenceImageAsset.ID](facegroupanalyzer/face/assetid.md)
  An identifier for the image asset that contains this face.
- [FaceGroupAnalyzer.Face.ID](facegroupanalyzer/face/id-swift.struct.md)
  A unique identifier for a detected face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/face/entityid)*