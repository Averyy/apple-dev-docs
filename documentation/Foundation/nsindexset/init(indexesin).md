# init(indexesIn:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes an allocated [`NSIndexSet`](../nsindexset.md) object with an index range.

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

```objc
- (instancetype) initWithIndexesInRange:(NSRange) range;
```

#### Return Value

Initialized [`NSIndexSet`](../nsindexset.md) object with `indexRange`.

#### Discussion

This method raises an [`rangeException`](../nsexceptionname/rangeexception.md) when `indexRange` would add an index that exceeds the maximum allowed value for unsigned integers.

The resulting index set has a [`firstIndex`](./firstindex.md) equal to the `location` of `indexRange`, and a [`count`](./count.md) equal to the `length` of `indexRange`. Specifying a zero-length range results in an empty index set.

This method is a designated initializer for [`NSIndexSet`](../nsindexset.md).

## Parameters

- `range`: An index range. Must be in the range `0 .. NSNotFound - 1`..

## See Also

### Creating Index Sets
- [convenience init(index: Int)](./init%28index%29.md)
  Initializes an allocated [`NSIndexSet`](../nsindexset.md) object with an index.
- [init(indexSet: IndexSet)](./init%28indexset%29.md)
  Initializes an allocated [`NSIndexSet`](../nsindexset.md) object with an index set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/init(indexesin:))*