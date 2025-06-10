# requestValue(_:)

**Framework**: App Intents  
**Kind**: method

Request a value from the user for this parameter.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
final func requestValue(_ dialog: IntentDialog? = nil) async throws -> Value.ValueType
```

## Mentions

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)

#### Return Value

The value supplied by the user

## Parameters

- `dialog`: A custom dialog that may be used when prompting the user for the value

## See Also

- [func needsValueError(IntentDialog?) -> AppIntentError](intentparameter/needsvalueerror(_:).md)
  Returns a `restartPerform` error with context to request a value from the user for this parameter and re-perform the intent with the new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/requestvalue(_:)-592nd)*