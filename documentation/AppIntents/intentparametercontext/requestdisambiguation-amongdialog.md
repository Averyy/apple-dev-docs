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
func requestDisambiguation(among itemsToDisambiguate: [Value.ValueType], dialog: IntentDialog? = nil) async throws -> Value.ValueType
```

#### Return Value

The value supplied by the user

## Parameters

- `itemsToDisambiguate`: The list of items to be presented to the user for disambiguation
- `dialog`: A custom dialog that may be used when prompting the user for the value


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparametercontext/requestdisambiguation(among:dialog:))*