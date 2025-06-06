# Schema components

**Framework**: SwiftData

Specify the constituent parts of your schema, including entities, attributes, and relationships.

## Topics

### Entities
- [Schema.Entity](schema/entity.md)
  An object that provides a blueprint for the associated model class.
### Attributes
- [Schema.Attribute](schema/attribute.md)
  An object that describes the configuration and behavior of a specific property of a model class.
- [Schema.CompositeAttribute](schema/compositeattribute.md)
  An object that describes an attribute that derives its value by composing other attributes.
### Relationships
- [Schema.Relationship](schema/relationship.md)
  An object that describes the configuration and behavior of a relationship between two model classes.
### Internal
- [Internal symbols](schemacomponentsinternal.md)
  Restricted-use symbols that the framework requires for macro expansion and other internal tasks.

## See Also

- [init(Schema.Entity..., version: Schema.Version)](schema/init(_:version:)-8el78.md)
- [init([any PersistentModel.Type], version: Schema.Version)](schema/init(_:version:)-8jo9o.md)
- [convenience init(versionedSchema: any VersionedSchema.Type)](schema/init(versionedschema:).md)
- [protocol VersionedSchema](versionedschema.md)
  An interface for describing a specific version of a schema, including the models it contains.
- [init()](schema/init.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schemacomponents)*