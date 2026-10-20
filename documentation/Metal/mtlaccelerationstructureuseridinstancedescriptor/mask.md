# mask

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```c
uint32_t mask;
```

#### Discussion

Metal reserves the top 24 bits for future use.

## See Also

### Customizing intersection and hit tests for the instance
- [var intersectionFunctionTableOffset: UInt32](./intersectionfunctiontableoffset.md)
  An offset for determining which function in the intersection function table Metal calls when testing a ray against the instance.
- [var options: MTLAccelerationStructureInstanceOptions](./options.md)
  The options for the instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureuseridinstancedescriptor/mask)*