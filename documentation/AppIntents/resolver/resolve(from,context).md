# resolve(from:context:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Converts the specified value into the expected data type.

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
func resolve(from input: Self.Input, context: IntentParameterContext<Self.Output>) async throws -> Self.Output?
```

#### Return Value

The converted value, or `nil` if conversion fails.

## Parameters

- `input`: The value to convert.
- `context`: Contextual resolution information, including resolution source and information about the associated parameter if applicable.

## See Also

### Resolving the type
- [associatedtype Input : _IntentValue](./input.md)
- [associatedtype Output : _IntentValue](./output.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/resolver/resolve(from:context:))*