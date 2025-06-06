# hashValue

**Framework**: RealityKit  
**Kind**: property

The hash value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var hashValue: Int { get }
```

#### Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

`hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

## See Also

- [func hash(into: inout Hasher)](lowlevelmesh/vertexsemantic/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [static func == (LowLevelMesh.VertexSemantic, LowLevelMesh.VertexSemantic) -> Bool](lowlevelmesh/vertexsemantic/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/vertexsemantic/hashvalue)*