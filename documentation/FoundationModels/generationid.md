# GenerationID

**Framework**: Foundation Models  
**Kind**: struct

A unique identifier that is stable for the duration of a response, but not across responses.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct GenerationID
```

#### Overview

The framework guarentees a `GenerationID` to be both present and stable when you receive it from a `LanguageModelSession`. When you create an instance of `GenerationID` there is no guarantee an identifier is present or stable.

## Topics

### Creating an identifier
- [init()](generationid/init.md)
  Create a new, unique `GenerationID`.
### Accessing the hash value
- [var hashValue: Int](generationid/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](generationid/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing generation identifiers
- [static func == (GenerationID, GenerationID) -> Bool](generationid/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](generationid/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationid)*