# AppSchema.PhotosEntity

**Framework**: App Intents  
**Kind**: protocol  
**Role**: Protocol

Identifies entity schemas in the photos domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol PhotosEntity : AppSchema.Kind
```

## Topics

### Instance Properties
- [var album: some AppSchemaEntity](./photosentity/album.md)
  An entity schema for an album.
- [var asset: some AppSchemaEntity](./photosentity/asset.md)
  An entity schema for an asset.
- [var recognizedPerson: some AppSchemaEntity](./photosentity/recognizedperson.md)
  An entity schema for a recognized person.

## Relationships

### Inherits From
- [AppSchema.Kind](./kind.md)
### Conforming Types
- [AppSchema.Entity](./entity.md)

## See Also

### Content and parameter types
- [var album: some AppSchemaEntity](./photosentity/album.md)
  An entity schema for an album.
- [var asset: some AppSchemaEntity](./photosentity/asset.md)
  An entity schema for an asset.
- [var recognizedPerson: some AppSchemaEntity](./photosentity/recognizedperson.md)
  An entity schema for a recognized person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/photosentity)*