# init(indexSet:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes an allocated [`NSIndexSet`](../nsindexset.md) object with an index set.

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
init(indexSet: IndexSet)
```

```objc
- (instancetype) initWithIndexSet:(NSIndexSet *) indexSet;
```

## Return Value

Initialized [`NSIndexSet`](../nsindexset.md) object with `indexSet`.

## Discussion

This method is a designated initializer for [`NSIndexSet`](../nsindexset.md).

## Parameters

- `indexSet`: An index set.

## See Also

### Creating Index Sets
- [convenience init(index: Int)](./init%28index%29.md)
  Initializes an allocated [`NSIndexSet`](../nsindexset.md) object with an index.
- [init(indexesIn: NSRange)](./init%28indexesin%29.md)
  Initializes an allocated [`NSIndexSet`](../nsindexset.md) object with an index range.
- [+ indexSet](./indexset.md)
  Creates an empty index set.
- [+ indexSetWithIndex:](./indexsetwithindex_.md)
  Creates an index set with an index.
- [+ indexSetWithIndexesInRange:](./indexsetwithindexesinrange_.md)
  Creates an index set with an index range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexset/init(indexset:))*