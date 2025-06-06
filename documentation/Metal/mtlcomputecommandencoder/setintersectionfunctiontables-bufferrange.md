# setIntersectionFunctionTables(_:bufferRange:)

**Framework**: Metal  
**Kind**: method

Binds multiple intersection function tables to the buffer argument table, allowing you to call their functions on the GPU.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func setIntersectionFunctionTables(_ intersectionFunctionTables: [(any MTLIntersectionFunctionTable)?], bufferRange: Range<Int>)
```

#### Discussion

> ⚠️ **Warning**:  This method requires that the number of instances in `visibleFunctionTables` be the same as the length of `bufferRange`.

 This method requires that the number of instances in `visibleFunctionTables` be the same as the length of `bufferRange`.

## Parameters

- `intersectionFunctionTables`: An array of   instances to bind.
- `bufferRange`: The argument buffer table indices to bind each of the   to, in the order they appear.

## See Also

- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](mtlcomputecommandencoder/setvisiblefunctiontable(_:bufferindex:).md)
  Binds a visible function table to the buffer argument table, allowing you to call its functions on the GPU.
- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](mtlcomputecommandencoder/setvisiblefunctiontables(_:bufferrange:).md)
  Binds multiple visible function tables to the buffer argument table, allowing you to call their functions on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setintersectionfunctiontables(_:bufferrange:))*