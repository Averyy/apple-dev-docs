# MediaIntelligenceVideoAsset.ID

**Framework**: Media Intelligence  
**Kind**: struct

A unique identifier for a video asset.

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

#### Overview

This value is a string-backed identifier that you assign to each video asset. Choose a value that uniquely identifies the video in your app, such as a file name or a database key.

## Topics

### Creating an ID
- [init(String)](mediaintelligencevideoasset/id-swift.struct/init(_:).md)

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

- [init(id: MediaIntelligenceVideoAsset.ID, kind: MediaIntelligenceVideoAsset.Kind)](mediaintelligencevideoasset/init(id:kind:).md)
  Creates a video asset with the specified identifier and kind.
- [MediaIntelligenceVideoAsset.Kind](mediaintelligencevideoasset/kind-swift.enum.md)
  A value that describes the source of a video asset’s data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaintelligence/mediaintelligencevideoasset/id-swift.struct)*