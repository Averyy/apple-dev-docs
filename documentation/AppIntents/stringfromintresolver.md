# StringFromIntResolver

**Framework**: App Intents  
**Kind**: struct

A resolver that converts one or more integers into one or more strings.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct StringFromIntResolver<Input, Output> where Input : _IntentValue, Output : _IntentValue, Output.ValueType == String
```

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Resolver](resolver.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct AttributedStringFromStringResolver](attributedstringfromstringresolver.md)
  A resolver that converts a string into an attributed string.
- [struct StringFromDoubleResolver](stringfromdoubleresolver.md)
  A resolver that converts a double into a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/stringfromintresolver)*