# startIndex

**Framework**: Swift  
**Kind**: property  
**Required**: Yes

The position of the first element in a nonempty collection.

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
var startIndex: Self.Index { get }
```

#### Discussion

If the collection is empty, `startIndex` is equal to `endIndex`.

## See Also

- [var endIndex: Self.Index](collection/endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: Self.Indices](collection/indices-9kkbf.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [func index(after: Self.Index) -> Self.Index](collection/index(after:).md)
  Returns the position immediately after the given index.
- [func formIndex(inout Self.Index, offsetBy: Int)](collection/formindex(_:offsetby:)-393pr.md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](collection/formindex(_:offsetby:limitedby:)-6jwra.md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collection/startindex)*