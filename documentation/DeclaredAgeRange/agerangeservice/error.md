# AgeRangeService.Error

**Framework**: Declared Age Range  
**Kind**: enum

An error that occurs when an age range request fails.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
enum Error
```

## Topics

### Interpreting error responses
- [AgeRangeService.Error.notAvailable](agerangeservice/error/notavailable.md)
  The system was unable to share the person’s age.
- [AgeRangeService.Error.invalidRequest](agerangeservice/error/invalidrequest.md)
  The request is invalid.
### Comparing values
- [static func == (AgeRangeService.Error, AgeRangeService.Error) -> Bool](agerangeservice/error/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [var hashValue: Int](agerangeservice/error/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](agerangeservice/error/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](agerangeservice/error/equatable-implementations.md)
- [Error Implementations](agerangeservice/error/error-implementations.md)
- [LocalizedError Implementations](agerangeservice/error/localizederror-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/error)*