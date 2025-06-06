# hash(into:)

**Framework**: PackageDescription  
**Kind**: method

Hashes the essential components of this value by feeding them into the given hasher.

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

#### Discussion

Implement this method to conform to the Hashable protocol. The components used for hashing must be the same as the components compared in your type’s == operator implementation. Call hasher.combine(_:) with each of these components.

> ❗ **Important**:  Never call finalize() on hasher. Doing so may become a compile-time error in the future.

 Never call finalize() on hasher. Doing so may become a compile-time error in the future.

## See Also

- [var hashValue: Int](product/library/librarytype/hashvalue.md)
  The library type’s hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/product/library/librarytype/hash(into:))*