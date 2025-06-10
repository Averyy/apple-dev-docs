# hashValue

**Framework**: Create ML  
**Kind**: property

The hash value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var hashValue: Int { get }
```

#### Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

## See Also

- [static func != (Self, Self) -> Bool](mldatavalue/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (MLDataValue, MLDataValue) -> Bool](mldatavalue/==(_:_:).md)
  Returns a Boolean value indicating whether two data values wrap the same underlying value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/hashvalue)*