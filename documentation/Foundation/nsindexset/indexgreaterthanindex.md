# indexGreaterThanIndex(_:)

**Framework**: Foundation  
**Kind**: method

Returns either the closest index in the index set that is greater than a specific index or the not-found indicator.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func indexGreaterThanIndex(_ value: Int) -> Int
```

#### Return Value

Closest index in the index set greater than `index`; NSNotFound when the index set contains no qualifying index.

## Parameters

- `value`: Index being inquired about.

## See Also

- [var firstIndex: Int](nsindexset/firstindex.md)
  The first index in the index set.
- [var lastIndex: Int](nsindexset/lastindex.md)
  The last index in the index set.
- [func indexLessThanIndex(Int) -> Int](nsindexset/indexlessthanindex(_:).md)
  Returns either the closest index in the index set that is less than a specific index or the not-found indicator.
- [func indexLessThanOrEqual(to: Int) -> Int](nsindexset/indexlessthanorequal(to:).md)
  Returns either the closest index in the index set that is less than or equal to a specific index or the not-found indicator.
- [func indexGreaterThanOrEqual(to: Int) -> Int](nsindexset/indexgreaterthanorequal(to:).md)
  Returns either the closest index in the index set that is greater than or equal to a specific index or the not-found indicator.
- [func getIndexes(UnsafeMutablePointer<Int>, maxCount: Int, inIndexRange: NSRangePointer?) -> Int](nsindexset/getindexes(_:maxcount:inindexrange:).md)
  The index set fills an index buffer with the indexes contained both in the index set and in an index range, returning the number of indexes copied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/indexgreaterthanindex(_:))*