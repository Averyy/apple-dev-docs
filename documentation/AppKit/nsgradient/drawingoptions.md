# NSGradient.DrawingOptions

**Framework**: AppKit  
**Kind**: struct

Constants that specify gradient drawing options.

**Availability**:
- macOS ?+

## Declaration

```swift
struct DrawingOptions
```

#### Overview

These constants are used by the primitive drawing methods to determine if drawing occurs outside of the gradient start and end locations.

## Topics

### Constants
- [static var drawsBeforeStartingLocation: NSGradient.DrawingOptions](nsgradient/drawingoptions/drawsbeforestartinglocation.md)
  Drawing extends before the gradient starting point.
- [static var drawsAfterEndingLocation: NSGradient.DrawingOptions](nsgradient/drawingoptions/drawsafterendinglocation.md)
  Drawing extends beyond the gradient end point.
### Initializers
- [init(rawValue: UInt)](nsgradient/drawingoptions/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/drawingoptions)*