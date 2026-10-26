# indexPathWithIndex:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a one-node index path.

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
+ (instancetype) indexPathWithIndex:(NSUInteger) index;
```

#### Return Value

One-node index path with `index`.

## Parameters

- `index`: Index of the item in node 0 to point to.

## See Also

### Related Documentation
- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
### Creating and Initializing Index Paths
- [+ indexPathWithIndexes:length:](./indexpathwithindexes_length_.md)
  Creates an index path with one or more nodes.
- [convenience init(index: Int)](./init%28index%29.md)
  Initializes an index path with a single node.
- [init(indexes: UnsafePointer<Int>?, length: Int)](./init%28indexes,length%29.md)
  Initializes an index path with the given nodes and length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/indexpathwithindex:)*