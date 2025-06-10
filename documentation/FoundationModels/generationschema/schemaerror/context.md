# GenerationSchema.SchemaError.Context

**Framework**: Foundation Models  
**Kind**: struct

The context in which the error occurred.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Context
```

## Topics

### Getting the context
- [init(debugDescription: String, underlyingErrors: [any Error])](generationschema/schemaerror/context/init(debugdescription:underlyingerrors:).md)
### Getting the debug description
- [let debugDescription: String](generationschema/schemaerror/context/debugdescription.md)
  A string representation of the debug description.
### Getting the underlying errors
- [let underlyingErrors: [any Error]](generationschema/schemaerror/context/underlyingerrors.md)
  The underlying errors that caused this error.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case duplicateProperty(schema: String, property: String, context: GenerationSchema.SchemaError.Context)](generationschema/schemaerror/duplicateproperty(schema:property:context:).md)
  An error that represents an attempt to construct a dynamic schema with properties that have conflicting names.
- [case duplicateType(schema: String?, type: String, context: GenerationSchema.SchemaError.Context)](generationschema/schemaerror/duplicatetype(schema:type:context:).md)
  An error that represents an attempt to construct a schema from dynamic schemas, and two or more of the subschemas have the same type name.
- [case emptyTypeChoices(schema: String, context: GenerationSchema.SchemaError.Context)](generationschema/schemaerror/emptytypechoices(schema:context:).md)
  An error that represents an attempt to construct an anyOf schema with an empty array of type choices.
- [case undefinedReferences(schema: String?, references: [String], context: GenerationSchema.SchemaError.Context)](generationschema/schemaerror/undefinedreferences(schema:references:context:).md)
  An error that represents an attempt to construct a schema from dynamic schemas, and one of those schemas references an undefined schema.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/schemaerror/context)*