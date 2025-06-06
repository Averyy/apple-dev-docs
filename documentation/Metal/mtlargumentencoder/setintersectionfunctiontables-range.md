# setIntersectionFunctionTables(_:range:)

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
func setIntersectionFunctionTables(_ intersectionFunctionTables: [(any MTLIntersectionFunctionTable)?], range: Range<Int>)
```

## Parameters

- `intersectionFunctionTables`: An array of intersection-function tables the method encodes.
- `range`: A range of indices within the argument buffer for each element in  .   The values correspond to either the index IDs of declarations in   Metal Shading Language (MSL) or the   property   of   instances.

## See Also

- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, index: Int)](mtlargumentencoder/setvisiblefunctiontable(_:index:).md)
  Encodes a reference to a visible-function table into the argument buffer.
- [func setIntersectionFunctionTable((any MTLIntersectionFunctionTable)?, index: Int)](mtlargumentencoder/setintersectionfunctiontable(_:index:).md)
  Encodes a reference to a ray-tracing intersection-function table into the argument buffer.
- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], range: Range<Int>)](mtlargumentencoder/setvisiblefunctiontables(_:range:).md)
  Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setintersectionfunctiontables(_:range:))*