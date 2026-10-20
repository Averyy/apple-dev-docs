# StringFromIntResolver

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

A resolver that converts one or more integers into one or more strings.

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
struct StringFromIntResolver<Input, Output> where Input : _IntentValue, Output : _IntentValue, Output.ValueType == String
```

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Resolver](./resolver.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### String resolution
- [struct AttributedStringFromStringResolver](./attributedstringfromstringresolver.md)
  A resolver that converts a string into an attributed string.
- [struct StringFromDoubleResolver](./stringfromdoubleresolver.md)
  A resolver that converts a double into a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/stringfromintresolver)*