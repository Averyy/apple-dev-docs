# setIntersectionFunctionTable(_:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setIntersectionFunctionTable:(id<MTLIntersectionFunctionTable>) intersectionFunctionTable atIndex:(NSUInteger) index;
```

## Parameters

- `intersectionFunctionTable`: An intersection-function table the method encodes.
- `index`: An index of an intersection-function table within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [`index`](../mtlargumentdescriptor/index.md) property of an [`MTLArgumentDescriptor`](../mtlargumentdescriptor.md) instance.

## See Also

### Encoding function tables
- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, index: Int)](./setvisiblefunctiontable%28_,index%29.md)
  Encodes a reference to a visible-function table into the argument buffer.
- [func setIntersectionFunctionTables([(any MTLIntersectionFunctionTable)?], range: Range<Int>)](./setintersectionfunctiontables%28_,range%29.md)
  Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.
- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], range: Range<Int>)](./setvisiblefunctiontables%28_,range%29.md)
  Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder/setintersectionfunctiontable(_:index:))*