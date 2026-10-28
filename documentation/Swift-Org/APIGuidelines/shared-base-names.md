---
url: "https://docs.swift.org/latest/documentation/apiguidelines/shared-base-names"
framework: "Swift-Org/APIGuidelines"
---

# Methods can share a base name

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

Methods can share a base name when they share the same basic meaning or when they operate in distinct domains.

## Overview

✅ For example, the following is encouraged, since the methods do essentially the same things:

```swift
extension Shape {
  /// Returns `true` if `other` is within the area of `self`;
  /// otherwise, `false`.
  func **contains**(_ other: **Point**) -> Bool { ... }

  /// Returns `true` if `other` is entirely within the area of `self`;
  /// otherwise, `false`.
  func **contains**(_ other: **Shape**) -> Bool { ... }

  /// Returns `true` if `other` is within the area of `self`;
  /// otherwise, `false`.
  func **contains**(_ other: **LineSegment**) -> Bool { ... }
}
```

✅ And since geometric types and collections are separate domains, this is also fine in the same program:

```swift
extension Collection where Element : Equatable {
  /// Returns `true` if `self` contains an element equal to
  /// `sought`; otherwise, `false`.
  func **contains**(_ sought: Element) -> Bool { ... }
}
```

⛔ However, these `index` methods have different semantics, and should have been named differently:

```swift
extension Database {
  /// Rebuilds the database's search index
  func **index**() { ... }

  /// Returns the `n`th row in the given table.
  func **index**(_ n: Int, inTable: TableID) -> TableRow { ... }
}
```

⛔ Lastly, avoid “overloading on return type” because it causes ambiguities in the presence of type inference.

```swift
extension Box {
  /// Returns the `Int` stored in `self`, if any, and
  /// `nil` otherwise.
  func **value**() -> Int? { ... }

  /// Returns the `String` stored in `self`, if any, and
  /// `nil` otherwise.
  func **value**() -> String? { ... }
}
```

## See Also

### Conventions — General
- [Document computed property complexity](./computed-property-complexity.md)
  Document the complexity of any computed property that is not O(1).
- [Prefer methods and properties to free functions](./methods-over-free-functions.md)
  Prefer methods and properties to free functions.
- [Follow case conventions](./case-conventions.md)
  Follow case conventions.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/shared-base-names)*