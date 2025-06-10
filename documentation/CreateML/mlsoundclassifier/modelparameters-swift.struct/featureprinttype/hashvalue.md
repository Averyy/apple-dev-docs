# hashValue

**Framework**: Create ML  
**Kind**: property

The hash value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var hashValue: Int { get }
```

#### Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

## See Also

- [func hash(into: inout Hasher)](mlsoundclassifier/modelparameters-swift.struct/featureprinttype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype/hashvalue)*