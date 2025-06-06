# adding(_:)

**Framework**: Foundation  
**Kind**: method

Returns an index path containing the nodes in the receiving index path plus another given index.

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
func adding(_ index: Int) -> IndexPath
```

#### Return Value

A new index path containing the receiving index path’s indexes and `index`.

## Parameters

- `index`: Index to append to the index path’s indexes.

## See Also

- [func removingLastIndex() -> IndexPath](nsindexpath/removinglastindex.md)
  Returns an index path with the nodes in the receiving index path, excluding the last one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsindexpath/adding(_:))*