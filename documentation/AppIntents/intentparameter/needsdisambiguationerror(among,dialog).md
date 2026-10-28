# needsDisambiguationError(among:dialog:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method

Returns a `restartPerform` error with context for the user to disambiguate amongst an array of values from for this parameter and re-perform the intent with the new value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
final func needsDisambiguationError(among itemsToDisambiguate: [Value.ValueType], dialog: IntentDialog? = nil) -> AppIntentError
```

Available when `Value` conforms to `_IntentValue` and `Sendable`.

## Return Value

An error that should be thrown within the intent `perform()` method.

## Parameters

- `itemsToDisambiguate`: The list of items to be presented to the user for disambiguation
- `dialog`: A custom dialog that may be used when prompting the user for the value

## See Also

### Requesting disambiguation
- [func requestDisambiguation(among: [Value.ValueType], dialog: IntentDialog?) async throws -> Value.ValueType](./requestdisambiguation%28among,dialog%29.md)
  Request that the user disambiguate amongst an array of values for this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/needsdisambiguationerror(among:dialog:))*