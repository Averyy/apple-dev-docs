# init(index:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes an index path with a single node.

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
convenience init(index: Int)
```

```objc
- (instancetype) initWithIndex:(NSUInteger) index;
```

## Return Value

Initialized [`NSIndexPath`](../nsindexpath.md) object representing a one-node index path with `index`.

## Parameters

- `index`: Index of the item in node 0 to point to.

## See Also

### Creating and Initializing Index Paths
- [init(indexes: UnsafePointer<Int>?, length: Int)](./init%28indexes,length%29.md)
  Initializes an index path with the given nodes and length.
- [+ indexPathWithIndexes:length:](./indexpathwithindexes_length_.md)
  Creates an index path with one or more nodes.
### Related Documentation
- [+ indexPathWithIndex:](./indexpathwithindex_.md)
  Creates a one-node index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/init(index:))*