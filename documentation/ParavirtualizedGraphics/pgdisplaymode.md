# PGDisplayMode

**Framework**: Paravirtualized Graphics  
**Kind**: class  
**Role**: Class

A description of a supported display mode.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
class PGDisplayMode
```

```objc
@interface PGDisplayMode : NSObject
```

## Topics

### Creating a Display Mode
- [init?(sizeInPixels: PGDisplayCoord_t, refreshRateInHz: Double)](./pgdisplaymode/init%28sizeinpixels,refreshrateinhz%29.md)
  Creates a new display mode.
### Inspecting Mode Properties
- [var sizeInPixels: PGDisplayCoord_t](./pgdisplaymode/sizeinpixels.md)
  The display mode’s dimensions in pixels.
- [var refreshRate: Double](./pgdisplaymode/refreshrate.md)
  The mode’s refresh rate.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Displays
- [class PGDisplayDescriptor](./pgdisplaydescriptor.md)
  A descriptor for a virtual display.
- [protocol PGDisplay](./pgdisplay.md)
  An object that provides display functionality to the guest operating system in a way that the host-side virtual machine app can intercept.
- [struct PGDisplayCoord_t](./pgdisplaycoord_t.md)
  Coordinates that describe sizes or offsets within a 2D array of pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaymode)*