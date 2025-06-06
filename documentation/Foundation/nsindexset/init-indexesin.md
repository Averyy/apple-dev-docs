# init(indexesIn:)

**Framework**: Foundation  
**Kind**: init

Initializes an allocated [`NSIndexSet`](nsindexset.md) object with an index range.

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
init(indexesIn range: NSRange)
```

#### Return Value

Initialized [`NSIndexSet`](nsindexset.md) object with `indexRange`.

#### Discussion

This method raises an [`rangeException`](nsexceptionname/rangeexception.md) when `indexRange` would add an index that exceeds the maximum allowed value for unsigned integers.

The resulting index set has a [`firstIndex`](nsindexset/firstindex.md) equal to the `location` of `indexRange`, and a [`count`](nsindexset/count.md) equal to the `length` of `indexRange`. Specifying a zero-length range results in an empty index set.

This method is a designated initializer for [`NSIndexSet`](nsindexset.md).

## Parameters

- `range`: An index range. Must be in the range  ..

## See Also

- [convenience init(index: Int)](nsindexset/init(index:).md)
  Initializes an allocated [`NSIndexSet`](nsindexset.md) object with an index.
- [init(indexSet: IndexSet)](nsindexset/init(indexset:).md)
  Initializes an allocated [`NSIndexSet`](nsindexset.md) object with an index set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/init(indexesin:))*