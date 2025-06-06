# hashValue

**Framework**: RealityKit  
**Kind**: property

The hash value.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- visionOS ?+

## Declaration

```swift
var hashValue: Int { get }
```

#### Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

`hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

## See Also

- [func hash(into: inout Hasher)](networkcompatibilitytoken/compatibility/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [static func != (Self, Self) -> Bool](networkcompatibilitytoken/compatibility/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (NetworkCompatibilityToken.Compatibility, NetworkCompatibilityToken.Compatibility) -> Bool](networkcompatibilitytoken/compatibility/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/networkcompatibilitytoken/compatibility/hashvalue)*