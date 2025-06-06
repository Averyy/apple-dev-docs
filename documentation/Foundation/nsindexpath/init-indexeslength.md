# init(indexes:length:)

**Framework**: Foundation  
**Kind**: init

Initializes an index path with the given nodes and length.

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
init(indexes: UnsafePointer<Int>?, length: Int)
```

#### Return Value

Initialized [`NSIndexPath`](nsindexpath.md) object with `indexes` up to `length`.

#### Discussion

This method is a designated initializer of [`NSIndexPath`](nsindexpath.md).

## Parameters

- `indexes`: Array of indexes to make up the index path.
- `length`: Number of nodes to include in the index path.

## See Also

- [convenience init(index: Int)](nsindexpath/init(index:).md)
  Initializes an index path with a single node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/init(indexes:length:))*