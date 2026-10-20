# FaceGroupAnalyzer.Face.ID

**Framework**: Media Intelligence  
**Kind**: struct  
**Role**: Structure

A unique identifier for a detected face.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct ID
```

## Topics

### Creating an ID
- [init(String)](./id-swift.struct/init%28_%29.md)
  Creates an identifier from a string value.
### Initializers
- [init(rawValue: String)](./id-swift.struct/init%28rawvalue%29.md)
  Creates an identifier from a raw string value.
### Instance Properties
- [let rawValue: String](./id-swift.struct/rawvalue.md)
  The raw string value of the identifier.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Identifying a face
- [let id: FaceGroupAnalyzer.Face.ID](./id-swift.property.md)
  A unique identifier for the face.
- [let entityID: FaceGroupAnalyzer.Entity.ID?](./entityid.md)
  An identifier for the entity this face belongs to.
- [let assetID: MediaIntelligenceImageAsset.ID](./assetid.md)
  An identifier for the image asset that contains this face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/face/id-swift.struct)*