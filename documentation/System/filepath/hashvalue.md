# hashValue

**Framework**: System  
**Kind**: property

The hash value.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var hashValue: Int { get }
```

#### Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

## See Also

- [static func == (FilePath, FilePath) -> Bool](filepath/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](filepath/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into: inout Hasher)](filepath/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/hashvalue)*