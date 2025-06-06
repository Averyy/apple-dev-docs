# mask

**Framework**: Metal  
**Kind**: property

A mask to use for the instance when testing a ray against the geometry.

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

- [var intersectionFunctionTableOffset: UInt32](mtlaccelerationstructureuseridinstancedescriptor/intersectionfunctiontableoffset.md)
  An offset for determining which function in the intersection function table Metal calls when testing a ray against the instance.
- [var options: MTLAccelerationStructureInstanceOptions](mtlaccelerationstructureuseridinstancedescriptor/options.md)
  The options for the instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/mask)*