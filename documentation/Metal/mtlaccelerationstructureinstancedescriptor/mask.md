# mask

**Framework**: Metal  
**Kind**: property

A mask to use for the instance when testing a ray against the geometry.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var mask: UInt32
```

#### Discussion

Metal reserves the top 24 bits for future use.

## See Also

- [var intersectionFunctionTableOffset: UInt32](mtlaccelerationstructureinstancedescriptor/intersectionfunctiontableoffset.md)
  An offset for determining which function in the intersection function table Metal needs to call when testing a ray against the instance.
- [var options: MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureinstancedescriptor/options.md)
  The options for the instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstancedescriptor/mask)*