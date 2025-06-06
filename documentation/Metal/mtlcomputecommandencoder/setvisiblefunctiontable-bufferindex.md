# setVisibleFunctionTable(_:bufferIndex:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Binds a visible function table to the buffer argument table, allowing you to call its functions on the GPU.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setVisibleFunctionTable(_ visibleFunctionTable: (any MTLVisibleFunctionTable)?, bufferIndex: Int)
```

## Parameters

- `visibleFunctionTable`: The   to bind.
- `bufferIndex`: The index the function table binds to in the buffer argument table.

## See Also

- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](mtlcomputecommandencoder/setvisiblefunctiontables(_:bufferrange:).md)
  Binds multiple visible function tables to the buffer argument table, allowing you to call their functions on the GPU.
- [func setIntersectionFunctionTables([(any MTLIntersectionFunctionTable)?], bufferRange: Range<Int>)](mtlcomputecommandencoder/setintersectionfunctiontables(_:bufferrange:).md)
  Binds multiple intersection function tables to the buffer argument table, allowing you to call their functions on the GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setvisiblefunctiontable(_:bufferindex:))*