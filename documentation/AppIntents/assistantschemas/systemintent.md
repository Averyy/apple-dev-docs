# AssistantSchemas.SystemIntent

**Framework**: App Intents  
**Kind**: protocol

Assistant schema conformance for app intents that match system-provided intents.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol SystemIntent : AssistantSchemas.Model
```

## Topics

### Instance Properties
- [var search: some AssistantSchemas.Intent](assistantschemas/systemintent/search.md)
  The app intent conforms to the schema for search functionality.

## Relationships

### Inherits From
- [AssistantSchemas.Model](assistantschemas/model.md)
### Conforming Types
- [AssistantSchema.IntentSchema](assistantschema/intentschema.md)
- [AssistantSchemas.IntentSchema](assistantschemas/intentschema.md)

## See Also

- [Making in-app search actions available to Siri and Apple Intelligence](making-in-app-search-actions-available-to-siri-and-apple-intelligence.md)
  Create app intents and entities to integrate your app’s search functionality with Siri and Apple Intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/systemintent)*