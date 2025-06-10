# GenerationSchema.SchemaError.duplicateProperty(schema:property:context:)

**Framework**: Foundation Models  
**Kind**: case

An error that represents an attempt to construct a dynamic schema with properties that have conflicting names.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
case duplicateProperty(schema: String, property: String, context: GenerationSchema.SchemaError.Context)
```

## See Also

- [case duplicateType(schema: String?, type: String, context: GenerationSchema.SchemaError.Context)](generationschema/schemaerror/duplicatetype(schema:type:context:).md)
  An error that represents an attempt to construct a schema from dynamic schemas, and two or more of the subschemas have the same type name.
- [case emptyTypeChoices(schema: String, context: GenerationSchema.SchemaError.Context)](generationschema/schemaerror/emptytypechoices(schema:context:).md)
  An error that represents an attempt to construct an anyOf schema with an empty array of type choices.
- [case undefinedReferences(schema: String?, references: [String], context: GenerationSchema.SchemaError.Context)](generationschema/schemaerror/undefinedreferences(schema:references:context:).md)
  An error that represents an attempt to construct a schema from dynamic schemas, and one of those schemas references an undefined schema.
- [GenerationSchema.SchemaError.Context](generationschema/schemaerror/context.md)
  The context in which the error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationschema/schemaerror/duplicateproperty(schema:property:context:))*