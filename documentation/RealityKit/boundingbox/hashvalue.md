# hashValue

**Framework**: RealityKit  
**Kind**: property

The hash value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
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

- [static func == (BoundingBox, BoundingBox) -> Bool](boundingbox/==(_:_:).md)
  Indicates whether two bounding boxes are equal.
- [static func != (Self, Self) -> Bool](boundingbox/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into: inout Hasher)](boundingbox/hash(into:).md)
  Hashes the essential components of the bounding box by feeding them into the given hash function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingbox/hashvalue)*