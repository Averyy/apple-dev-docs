# setVisibleFunctionTable(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a reference to a visible-function table into the argument buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setVisibleFunctionTable(_ visibleFunctionTable: (any MTLVisibleFunctionTable)?, index: Int)
```

## Parameters

- `visibleFunctionTable`: A visible-function table the method encodes.
- `index`: The index of a visible-function table within the argument buffer.   The value corresponds to either the index ID of a declaration in   Metal Shading Language (MSL) or the   property of   an   instance.

## See Also

- [func setIntersectionFunctionTable((any MTLIntersectionFunctionTable)?, index: Int)](mtlargumentencoder/setintersectionfunctiontable(_:index:).md)
  Encodes a reference to a ray-tracing intersection-function table into the argument buffer.
- [func setIntersectionFunctionTables([(any MTLIntersectionFunctionTable)?], range: Range<Int>)](mtlargumentencoder/setintersectionfunctiontables(_:range:).md)
  Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.
- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], range: Range<Int>)](mtlargumentencoder/setvisiblefunctiontables(_:range:).md)
  Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setvisiblefunctiontable(_:index:))*