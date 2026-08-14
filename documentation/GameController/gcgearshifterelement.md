# GCGearShifterElement

**Framework**: Game Controller  
**Kind**: class

An element that represents either a pattern or a sequential gear shift.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
class GCGearShifterElement
```

## Topics

### Accessing input values
- [var patternInput: (any GCSwitchPositionInput)?](gcgearshifterelement/patterninput.md)
  The input object for a pattern gear shift.
- [var sequentialInput: (any GCRelativeInput)?](gcgearshifterelement/sequentialinput.md)
  The input object for a sequential gear shift.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [GCPhysicalInputElement](gcphysicalinputelement.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [protocol GCAxisInput](gcaxisinput.md)
  The common properties of inputs that provide absolute values along an axis with a fixed origin.
- [protocol GCRelativeInput](gcrelativeinput.md)
  The common properties of inputs that provide positions along an axis that are relative to the previous position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcgearshifterelement)*