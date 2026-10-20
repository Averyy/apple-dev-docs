# GenerationSchema.SchemaError.duplicateType(schema:type:context:)

**Framework**: Foundation Models  
**Kind**: case  
**Role**: Case

An error that represents an attempt to construct a schema from dynamic schemas in which two or more of the subschemas have the same type name.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
case duplicateType(schema: String?, type: String, context: GenerationSchema.SchemaError.Context)
```

## See Also

### Getting schema errors
- [case duplicateProperty(schema: String, property: String, context: GenerationSchema.SchemaError.Context)](./duplicateproperty%28schema,property,context%29.md)
  An error that represents an attempt to construct a dynamic schema with properties that have conflicting names.
- [case emptyTypeChoices(schema: String, context: GenerationSchema.SchemaError.Context)](./emptytypechoices%28schema,context%29.md)
  An error that represents an attempt to construct an anyOf schema with an empty array of type choices.
- [case undefinedReferences(schema: String?, references: [String], context: GenerationSchema.SchemaError.Context)](./undefinedreferences%28schema,references,context%29.md)
  An error that represents an attempt to construct a schema from dynamic schemas in which one of those schemas references an undefined schema.
- [GenerationSchema.SchemaError.Context](./context.md)
  The context in which the error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/schemaerror/duplicatetype(schema:type:context:))*