# GenerationSchema.SchemaError

**Framework**: Foundation Models  
**Kind**: enum  
**Role**: Enumeration

An error that occurs when there is a problem creating a generation schema.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
@nonexhaustive enum SchemaError
```

## Topics

### Getting schema errors
- [case duplicateProperty(schema: String, property: String, context: GenerationSchema.SchemaError.Context)](./schemaerror/duplicateproperty%28schema,property,context%29.md)
  An error that represents an attempt to construct a dynamic schema with properties that have conflicting names.
- [case duplicateType(schema: String?, type: String, context: GenerationSchema.SchemaError.Context)](./schemaerror/duplicatetype%28schema,type,context%29.md)
  An error that represents an attempt to construct a schema from dynamic schemas in which two or more of the subschemas have the same type name.
- [case emptyTypeChoices(schema: String, context: GenerationSchema.SchemaError.Context)](./schemaerror/emptytypechoices%28schema,context%29.md)
  An error that represents an attempt to construct an anyOf schema with an empty array of type choices.
- [case undefinedReferences(schema: String?, references: [String], context: GenerationSchema.SchemaError.Context)](./schemaerror/undefinedreferences%28schema,references,context%29.md)
  An error that represents an attempt to construct a schema from dynamic schemas in which one of those schemas references an undefined schema.
- [GenerationSchema.SchemaError.Context](./schemaerror/context.md)
  The context in which the error occurred.
### Getting the error description
- [var errorDescription: String?](./schemaerror/errordescription.md)
  A string representation of the error description.
### Getting the recovery suggestion
- [var recoverySuggestion: String?](./schemaerror/recoverysuggestion.md)
  A suggestion that indicates how to handle the error.
### Default Implementations
- [LocalizedError Implementations](./schemaerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Error](../../Swift/error.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/schemaerror)*