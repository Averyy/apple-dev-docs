# Input

**Framework**: App Intents  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

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
associatedtype Input : _IntentValue
```

## See Also

### Resolving the type
- [func resolve(from: Self.Input, context: IntentParameterContext<Self.Output>) async throws -> Self.Output?](./resolve%28from,context%29.md)
  Converts the specified value into the expected data type.
- [associatedtype Output : _IntentValue](./output.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/resolver/input)*