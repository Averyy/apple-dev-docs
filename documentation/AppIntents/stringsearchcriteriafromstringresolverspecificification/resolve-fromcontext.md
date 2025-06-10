# resolve(from:context:)

**Framework**: App Intents  
**Kind**: method

Converts the specified value into the expected data type.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst ?+
- macOS 14.2+
- tvOS 17.2+
- visionOS ?+
- watchOS 10.2+

## Declaration

```swift
func resolve(from input: String, context: IntentParameterContext<StringSearchCriteria>) async throws -> StringSearchCriteria?
```

#### Return Value

The converted value, or `nil` if conversion fails.

## Parameters

- `input`: The value to convert.
- `context`: Contextual resolution information, including resolution source and information   about the associated parameter if applicable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/stringsearchcriteriafromstringresolverspecificification/resolve(from:context:))*