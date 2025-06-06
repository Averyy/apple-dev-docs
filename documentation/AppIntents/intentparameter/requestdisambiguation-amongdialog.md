# requestDisambiguation(among:dialog:)

**Framework**: App Intents  
**Kind**: method

Request that the user disambiguate amongst an array of values for this parameter.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
final func requestDisambiguation(among itemsToDisambiguate: [Value.ValueType], dialog: IntentDialog? = nil) async throws -> Value.ValueType
```

#### Return Value

The value supplied by the user

## Parameters

- `itemsToDisambiguate`: The list of items to be presented to the user for disambiguation
- `dialog`: A custom dialog that may be used when prompting the user for the value

## See Also

- [func needsDisambiguationError(among: [Value.ValueType], dialog: IntentDialog?) -> AppIntentError](intentparameter/needsdisambiguationerror(among:dialog:).md)
  Returns a `restartPerform` error with context for the user to disambiguate amongst an array of values from for this parameter and re-perform the intent with the new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/requestdisambiguation(among:dialog:))*