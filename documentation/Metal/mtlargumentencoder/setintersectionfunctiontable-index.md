# setIntersectionFunctionTable(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a reference to a ray-tracing intersection-function table into the argument buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setIntersectionFunctionTable(_ intersectionFunctionTable: (any MTLIntersectionFunctionTable)?, index: Int)
```

## Parameters

- `intersectionFunctionTable`: An intersection-function table the method encodes.
- `index`: An index of an intersection-function table within the argument buffer.   The value corresponds to either the index ID of a declaration in   Metal Shading Language (MSL) or the   property of   an   instance.

## See Also

- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, index: Int)](mtlargumentencoder/setvisiblefunctiontable(_:index:).md)
  Encodes a reference to a visible-function table into the argument buffer.
- [func setIntersectionFunctionTables([(any MTLIntersectionFunctionTable)?], range: Range<Int>)](mtlargumentencoder/setintersectionfunctiontables(_:range:).md)
  Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.
- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], range: Range<Int>)](mtlargumentencoder/setvisiblefunctiontables(_:range:).md)
  Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setintersectionfunctiontable(_:index:))*