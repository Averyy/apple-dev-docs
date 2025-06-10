# AskError

**Framework**: PermissionKit  
**Kind**: enum

An error that can occur when asking someone to send a communication permission question.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum AskError
```

## Topics

### Getting the error response
- [AskError.unknown](askerror/unknown.md)
  An unknown error response.
### Operators
- [static func == (AskError, AskError) -> Bool](askerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](askerror/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](askerror/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](askerror/equatable-implementations.md)
- [Error Implementations](askerror/error-implementations.md)
- [LocalizedError Implementations](askerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/askerror)*