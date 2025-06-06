# indices

**Framework**: Swift  
**Kind**: property  
**Required**: Yes

The indices that are valid for subscripting the collection, in ascending order.

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
var indices: Self.Indices { get }
```

#### Discussion

A collection’s `indices` property can hold a strong reference to the collection itself, causing the collection to be nonuniquely referenced. If you mutate the collection while iterating over its indices, a strong reference can result in an unexpected copy of the collection. To avoid the unexpected copy, use the `index(after:)` method starting with `startIndex` to produce indices instead.

```swift
var c = MyFancyCollection([10, 20, 30, 40, 50])
var i = c.startIndex
while i != c.endIndex {
    c[i] /= 5
    i = c.index(after: i)
}
// c == MyFancyCollection([2, 4, 6, 8, 10])
```

## See Also

- [var startIndex: Self.Index](collection/startindex.md)
  The position of the first element in a nonempty collection.
- [var endIndex: Self.Index](collection/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [func index(after: Self.Index) -> Self.Index](collection/index(after:).md)
  Returns the position immediately after the given index.
- [func formIndex(inout Self.Index, offsetBy: Int)](collection/formindex(_:offsetby:)-393pr.md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](collection/formindex(_:offsetby:limitedby:)-6jwra.md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collection/indices-9kkbf)*