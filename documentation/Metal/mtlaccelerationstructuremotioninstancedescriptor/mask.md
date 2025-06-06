# mask

**Framework**: Metal  
**Kind**: property

A mask used for this instance when testing a ray against the geometry.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var mask: UInt32
```

#### Discussion

Metal reserves the top 24 bits for future use.

## See Also

- [var intersectionFunctionTableOffset: UInt32](mtlaccelerationstructuremotioninstancedescriptor/intersectionfunctiontableoffset.md)
  An offset used to determine which function in the intersection function table Metal should call when testing a ray against this instance.
- [var options: MTLAccelerationStructureInstanceOptions](mtlaccelerationstructuremotioninstancedescriptor/options.md)
  The options for this instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuremotioninstancedescriptor/mask)*