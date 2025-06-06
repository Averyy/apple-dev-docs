# PGDisplayMode

**Framework**: Paravirtualized Graphics  
**Kind**: class

A description of a supported display mode.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
class PGDisplayMode
```

## Topics

### Creating a Display Mode
- [init?(sizeInPixels: PGDisplayCoord_t, refreshRateInHz: Double)](pgdisplaymode/init(sizeinpixels:refreshrateinhz:).md)
  Creates a new display mode.
### Inspecting Mode Properties
- [var sizeInPixels: PGDisplayCoord_t](pgdisplaymode/sizeinpixels.md)
  The display mode’s dimensions in pixels.
- [var refreshRate: Double](pgdisplaymode/refreshrate.md)
  The mode’s refresh rate.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PGDisplayDescriptor](pgdisplaydescriptor.md)
  A descriptor for a virtual display.
- [protocol PGDisplay](pgdisplay.md)
  An object that provides display functionality to the guest operating system in a way that the host-side virtual machine app can intercept.
- [struct PGDisplayCoord_t](pgdisplaycoord_t.md)
  Coordinates that describe sizes or offsets within a 2D array of pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaymode)*