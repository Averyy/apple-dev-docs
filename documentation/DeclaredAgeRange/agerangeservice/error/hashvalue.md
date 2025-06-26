# hashValue

**Framework**: Declared Age Range  
**Kind**: property

The hash value.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
var hashValue: Int { get }
```

#### Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

## See Also

- [static func == (AgeRangeService.Error, AgeRangeService.Error) -> Bool](agerangeservice/error/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [func hash(into: inout Hasher)](agerangeservice/error/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/declaredagerange/agerangeservice/error/hashvalue)*