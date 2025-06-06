# PGDisplayCoord_t

**Framework**: Paravirtualized Graphics  
**Kind**: struct

Coordinates that describe sizes or offsets within a 2D array of pixels.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
struct PGDisplayCoord_t
```

## Topics

### Creating Display Coordinates
- [init()](pgdisplaycoord_t/init.md)
  Initializes a default display coordinate.
- [init(x: UInt16, y: UInt16)](pgdisplaycoord_t/init(x:y:).md)
  Initializes a coordinate.
### Inspecting Coordinate Values
- [var x: UInt16](pgdisplaycoord_t/x.md)
  The horizontal coordinate value.
- [var y: UInt16](pgdisplaycoord_t/y.md)
  The vertical coordinate value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class PGDisplayDescriptor](pgdisplaydescriptor.md)
  A descriptor for a virtual display.
- [protocol PGDisplay](pgdisplay.md)
  An object that provides display functionality to the guest operating system in a way that the host-side virtual machine app can intercept.
- [class PGDisplayMode](pgdisplaymode.md)
  A description of a supported display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaycoord_t)*