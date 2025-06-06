# remove(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Removes the given element and any elements subsumed by the given element.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@discardableResult
mutating func remove(_ member: Self.Element) -> Self.Element?
```

#### Return Value

For ordinary sets, an element equal to `member` if `member` is contained in the set; otherwise, `nil`. In some cases, a returned element may be distinguishable from `member` by identity comparison or some other means.

For sets where the set type and element type are the same, like `OptionSet` types, this method returns any intersection between the set and `[member]`, or `nil` if the intersection is empty.

## Parameters

- `member`: The element of the set to remove.

## See Also

- [func insert(Self.Element) -> (inserted: Bool, memberAfterInsert: Self.Element)](setalgebra/insert(_:).md)
  Inserts the given element in the set if it is not already present.
- [func update(with: Self.Element) -> Self.Element?](setalgebra/update(with:).md)
  Inserts the given element into the set unconditionally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/setalgebra/remove(_:))*