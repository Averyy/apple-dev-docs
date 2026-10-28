# indexPathWithIndexes:length:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates an index path with one or more nodes.

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
+ (instancetype) indexPathWithIndexes:(const NSUInteger[]) indexes length:(NSUInteger) length;
```

## Return Value

Index path with `indexes` up to `length`.

## Parameters

- `indexes`: Array of indexes to make up the index path.
- `length`: Number of nodes to include in the index path.

## See Also

### Creating and Initializing Index Paths
- [+ indexPathWithIndex:](./indexpathwithindex_.md)
  Creates a one-node index path.
- [convenience init(index: Int)](./init%28index%29.md)
  Initializes an index path with a single node.
- [init(indexes: UnsafePointer<Int>?, length: Int)](./init%28indexes,length%29.md)
  Initializes an index path with the given nodes and length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/indexpathwithindexes:length:)*