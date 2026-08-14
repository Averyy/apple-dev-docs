# FaceGroupAnalyzer.Face.ID

**Framework**: Media Intelligence  
**Kind**: struct

A unique identifier for a detected face.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ID
```

## Topics

### Creating an ID
- [init(String)](facegroupanalyzer/face/id-swift.struct/init(_:).md)
  Creates an identifier from a string value.
### Initializers
- [init(rawValue: String)](facegroupanalyzer/face/id-swift.struct/init(rawvalue:).md)
  Creates an identifier from a raw string value.
### Instance Properties
- [let rawValue: String](facegroupanalyzer/face/id-swift.struct/rawvalue.md)
  The raw string value of the identifier.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let id: FaceGroupAnalyzer.Face.ID](facegroupanalyzer/face/id-swift.property.md)
  A unique identifier for the face.
- [let entityID: FaceGroupAnalyzer.Entity.ID?](facegroupanalyzer/face/entityid.md)
  An identifier for the entity this face belongs to.
- [let assetID: MediaIntelligenceImageAsset.ID](facegroupanalyzer/face/assetid.md)
  An identifier for the image asset that contains this face.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/facegroupanalyzer/face/id-swift.struct)*