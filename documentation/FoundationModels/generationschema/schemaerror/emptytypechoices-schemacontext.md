# GenerationSchema.SchemaError.emptyTypeChoices(schema:context:)

**Framework**: Foundation Models  
**Kind**: case

An error that represents an attempt to construct an anyOf schema with an empty array of type choices.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case emptyTypeChoices(schema: String, context: GenerationSchema.SchemaError.Context)
```

## See Also

- [case duplicateProperty(schema: String, property: String, context: GenerationSchema.SchemaError.Context)](generationschema/schemaerror/duplicateproperty(schema:property:context:).md)
  An error that represents an attempt to construct a dynamic schema with properties that have conflicting names.
- [case duplicateType(schema: String?, type: String, context: GenerationSchema.SchemaError.Context)](generationschema/schemaerror/duplicatetype(schema:type:context:).md)
  An error that represents an attempt to construct a schema from dynamic schemas, and two or more of the subschemas have the same type name.
- [case undefinedReferences(schema: String?, references: [String], context: GenerationSchema.SchemaError.Context)](generationschema/schemaerror/undefinedreferences(schema:references:context:).md)
  An error that represents an attempt to construct a schema from dynamic schemas, and one of those schemas references an undefined schema.
- [GenerationSchema.SchemaError.Context](generationschema/schemaerror/context.md)
  The context in which the error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/schemaerror/emptytypechoices(schema:context:))*