# VersionedSchema

**Framework**: SwiftData  
**Kind**: protocol

An interface for describing a specific version of a schema, including the models it contains.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
protocol VersionedSchema : SendableMetatype
```

## Topics

### Describing the version
- [static var versionIdentifier: Schema.Version](versionedschema/versionidentifier.md)
  The textual description of the migration’s version or purpose.
### Specifying the included models
- [static var models: [any PersistentModel.Type]](versionedschema/models.md)
  The models to include in this version of the schema.

## Relationships

### Inherits From
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(Schema.Entity..., version: Schema.Version)](schema/init(_:version:)-8el78.md)
- [init([any PersistentModel.Type], version: Schema.Version)](schema/init(_:version:)-8jo9o.md)
- [convenience init(versionedSchema: any VersionedSchema.Type)](schema/init(versionedschema:).md)
- [init()](schema/init.md)
- [Schema components](schemacomponents.md)
  Specify the constituent parts of your schema, including entities, attributes, and relationships.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/versionedschema)*