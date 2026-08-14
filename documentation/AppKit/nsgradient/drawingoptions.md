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
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/drawingoptions)*