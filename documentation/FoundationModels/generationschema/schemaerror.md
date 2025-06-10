# GenerationSchema.SchemaError

**Framework**: Foundation Models  
**Kind**: enum

A error that occurs when there is a problem creating a generation schema.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum SchemaError
```

## Topics

### Getting schema errors
- [case duplicateProperty(schema: String, property: String, context: GenerationSchema.SchemaError.Context)](generationschema/schemaerror/duplicateproperty(schema:property:context:).md)
  An error that represents an attempt to construct a dynamic schema with properties that have conflicting names.
- [case duplicateType(schema: String?, type: String, context: GenerationSchema.SchemaError.Context)](generationschema/schemaerror/duplicatetype(schema:type:context:).md)
  An error that represents an attempt to construct a schema from dynamic schemas, and two or more of the subschemas have the same type name.
- [case emptyTypeChoices(schema: String, context: GenerationSchema.SchemaError.Context)](generationschema/schemaerror/emptytypechoices(schema:context:).md)
  An error that represents an attempt to construct an anyOf schema with an empty array of type choices.
- [case undefinedReferences(schema: String?, references: [String], context: GenerationSchema.SchemaError.Context)](generationschema/schemaerror/undefinedreferences(schema:references:context:).md)
  An error that represents an attempt to construct a schema from dynamic schemas, and one of those schemas references an undefined schema.
- [GenerationSchema.SchemaError.Context](generationschema/schemaerror/context.md)
  The context in which the error occurred.
### Getting the error description
- [var errorDescription: String](generationschema/schemaerror/errordescription.md)
  A string representation of the error description.
### Getting the recovery suggestion
- [var recoverySuggestion: String?](generationschema/schemaerror/recoverysuggestion.md)
  A suggestion that indicates how to handle the error.
### Default Implementations
- [Error Implementations](generationschema/schemaerror/error-implementations.md)
- [LocalizedError Implementations](generationschema/schemaerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/schemaerror)*