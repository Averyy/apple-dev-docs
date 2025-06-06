# intersectionFunctionTableOffset

**Framework**: Metal  
**Kind**: property

An offset for determining which function in the intersection function table Metal calls when testing a ray against the instance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var intersectionFunctionTableOffset: UInt32
```

#### Discussion

By default, after Metal finds an intersection between a ray and a primitive, it runs your specified intersection function to determine whether the ray actually hit the primitive. To determine which function in the intersection table to call, Metal adds this property to the value in the instance’s [`intersectionFunctionTableOffset`](mtlaccelerationstructuregeometrydescriptor/intersectionfunctiontableoffset.md), and looks up the entry at that index.

## See Also

- [var options: MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureuseridinstancedescriptor/options.md)
  The options for the instance.
- [var mask: UInt32](mtlaccelerationstructureuseridinstancedescriptor/mask.md)
  A mask to use for the instance when testing a ray against the geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/intersectionfunctiontableoffset)*