# intersectionFunctionTableOffset

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

An offset for determining which function in the intersection function table Metal needs to call when testing a ray against the instance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var intersectionFunctionTableOffset: UInt32
```

```c
uint32_t intersectionFunctionTableOffset;
```

## Discussion

By default, after Metal finds an intersection between a ray and a primitive, it runs your specified intersection function to determine whether the ray actually hit the primitive. To determine which function in the intersection table to call, Metal adds this property to the value in the instance’s [`intersectionFunctionTableOffset`](../mtlaccelerationstructuregeometrydescriptor/intersectionfunctiontableoffset.md), and looks up the entry at that index.

## See Also

### Customizing intersection and hit tests for the instance
- [var options: MTLAccelerationStructureInstanceOptions](./options.md)
  The options for the instance.
- [var mask: UInt32](./mask.md)
  A mask to use for the instance when testing a ray against the geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptor/intersectionfunctiontableoffset)*