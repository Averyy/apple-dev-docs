# resolve(from:context:)

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Converts the specified value into the expected data type.

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
func resolve(from input: Self.Input, context: IntentParameterContext<Self.Output>) async throws -> Self.Output?
```

#### Return Value

The converted value, or `nil` if conversion fails.

## Parameters

- `input`: The value to convert.
- `context`: Contextual resolution information, including resolution source and information   about the associated parameter if applicable.

## See Also

- [associatedtype Input : _IntentValue](resolver/input.md)
- [associatedtype Output : _IntentValue](resolver/output.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/resolver/resolve(from:context:))*