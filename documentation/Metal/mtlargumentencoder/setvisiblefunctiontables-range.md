# setVisibleFunctionTables(_:range:)

**Framework**: Metal  
**Kind**: method

Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func setVisibleFunctionTables(_ visibleFunctionTables: [(any MTLVisibleFunctionTable)?], range: Range<Int>)
```

## Parameters

- `visibleFunctionTables`: An array of visible-function tables the method encodes.
- `range`: A range of indices within the argument buffer for each element in  .   The values correspond to either the index IDs of declarations in   Metal Shading Language (MSL) or the   property   of   instances.

## See Also

- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, index: Int)](mtlargumentencoder/setvisiblefunctiontable(_:index:).md)
  Encodes a reference to a visible-function table into the argument buffer.
- [func setIntersectionFunctionTable((any MTLIntersectionFunctionTable)?, index: Int)](mtlargumentencoder/setintersectionfunctiontable(_:index:).md)
  Encodes a reference to a ray-tracing intersection-function table into the argument buffer.
- [func setIntersectionFunctionTables([(any MTLIntersectionFunctionTable)?], range: Range<Int>)](mtlargumentencoder/setintersectionfunctiontables(_:range:).md)
  Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setvisiblefunctiontables(_:range:))*