# indexSetWithIndexesInRange:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates an index set with an index range.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) indexSetWithIndexesInRange:(NSRange) range;
```

#### Return Value

[`NSIndexSet`](../nsindexset.md) object containing `indexRange`.

#### Discussion

The resulting index set has a [`firstIndex`](./firstindex.md) equal to the `location` of `indexRange`, and a [`count`](./count.md) equal to the `length` of `indexRange`. Specifying a zero-length range results in an empty index set.

## Parameters

- `range`: An index range. Must be in the range `0 .. NSNotFound - 1`.

## See Also

### Creating Index Sets
- [+ indexSet](./indexset.md)
  Creates an empty index set.
- [+ indexSetWithIndex:](./indexsetwithindex_.md)
  Creates an index set with an index.
- [convenience init(index: Int)](./init%28index%29.md)
  Initializes an allocated [`NSIndexSet`](../nsindexset.md) object with an index.
- [init(indexesIn: NSRange)](./init%28indexesin%29.md)
  Initializes an allocated [`NSIndexSet`](../nsindexset.md) object with an index range.
- [init(indexSet: IndexSet)](./init%28indexset%29.md)
  Initializes an allocated [`NSIndexSet`](../nsindexset.md) object with an index set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/indexsetwithindexesinrange:)*