# resolve(from:context:)

**Framework**: App Intents  
**Kind**: method

Converts the specified value into the expected data type.

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
func resolve(from input: Double, context: IntentParameterContext<String>) async throws -> String?
```

#### Return Value

The converted value, or `nil` if conversion fails.

## Parameters

- `input`: The value to convert.
- `context`: Contextual resolution information, including resolution source and information   about the associated parameter if applicable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/stringfromdoubleresolver/resolve(from:context:))*