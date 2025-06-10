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
func requestValue(_ dialog: IntentDialog? = nil) async throws -> Value.ValueType
```

#### Return Value

The value supplied by the user

## Parameters

- `dialog`: A custom dialog that may be used when prompting the user for the value


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparametercontext/requestvalue(_:))*