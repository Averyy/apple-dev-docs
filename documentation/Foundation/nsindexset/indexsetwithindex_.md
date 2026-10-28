# indexSetWithIndex:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates an index set with an index.

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
+ (instancetype) indexSetWithIndex:(NSUInteger) value;
```

## Return Value

[`NSIndexSet`](../nsindexset.md) object containing `index`.

## Parameters

- `value`: An index. Must be in the range `0 .. NSNotFound - 1`.

## See Also

### Creating Index Sets
- [+ indexSet](./indexset.md)
  Creates an empty index set.
- [+ indexSetWithIndexesInRange:](./indexsetwithindexesinrange_.md)
  Creates an index set with an index range.
- [convenience init(index: Int)](./init%28index%29.md)
  Initializes an allocated [`NSIndexSet`](../nsindexset.md) object with an index.
- [init(indexesIn: NSRange)](./init%28indexesin%29.md)
  Initializes an allocated [`NSIndexSet`](../nsindexset.md) object with an index range.
- [init(indexSet: IndexSet)](./init%28indexset%29.md)
  Initializes an allocated [`NSIndexSet`](../nsindexset.md) object with an index set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/indexsetwithindex:)*