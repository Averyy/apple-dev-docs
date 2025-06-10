# needsValueError(_:)

**Framework**: App Intents  
**Kind**: method

Returns a `restartPerform` error with context to request a value from the user for this parameter and re-perform the intent with the new value.

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
func needsValueError(_ dialog: IntentDialog? = nil) -> AppIntentError
```

#### Return Value

An error that should be thrown within the intent `perform()` method.

## Parameters

- `dialog`: A custom dialog that may be used when prompting the user for the value


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparametercontext/needsvalueerror(_:))*