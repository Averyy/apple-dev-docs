# AppSchema.SystemIntent

**Framework**: App Intents  
**Kind**: protocol

Identifies intent schemas in the system domain.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
protocol SystemIntent : AppSchema.Kind
```

## Topics

### Instance Properties
- [var open: some AppSchemaIntent](appschema/systemintent/open.md)
  An intent schema that opens an item in the application.
- [var search: some AppSchemaIntent](appschema/systemintent/search.md)
  An intent schema that navigates to search results.
- [var searchInApp: some AppSchemaIntent](appschema/systemintent/searchinapp.md)
  An intent schema that navigates to search results.

## Relationships

### Inherits From
- [AppSchema.Kind](appschema/kind.md)
### Conforming Types
- [AppSchema.Intent](appschema/intent.md)

## See Also

- [var open: some AppSchemaIntent](appschema/systemintent/open.md)
  An intent schema that opens an item in the application.
- [var search: some AppSchemaIntent](appschema/systemintent/search.md)
  An intent schema that navigates to search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/systemintent)*