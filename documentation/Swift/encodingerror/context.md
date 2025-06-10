# EncodingError.Context

**Framework**: Swift  
**Kind**: struct

The context in which the error occurred.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct Context
```

## Topics

### Initializers
- [init(codingPath: [any CodingKey], debugDescription: String, underlyingError: (any Error)?)](encodingerror/context/init(codingpath:debugdescription:underlyingerror:).md)
  Creates a new context with the given path of coding keys and a description of what went wrong.
### Instance Properties
- [let codingPath: [any CodingKey]](encodingerror/context/codingpath.md)
  The path of coding keys taken to get to the point of the failing encode call.
- [let debugDescription: String](encodingerror/context/debugdescription.md)
  A description of what went wrong, for debugging purposes.
- [let underlyingError: (any Error)?](encodingerror/context/underlyingerror.md)
  The underlying error which caused this error, if any.

## Relationships

### Conforms To
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/encodingerror/context)*