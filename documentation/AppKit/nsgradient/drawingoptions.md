# NSGradient.DrawingOptions

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that specify gradient drawing options.

**Availability**:
- macOS

## Declaration

```swift
struct DrawingOptions
```

```c
enum NSGradientDrawingOptions : NSUInteger;
```

#### Overview

These constants are used by the primitive drawing methods to determine if drawing occurs outside of the gradient start and end locations.

## Topics

### Constants
- [static var drawsBeforeStartingLocation: NSGradient.DrawingOptions](./drawingoptions/drawsbeforestartinglocation.md)
  Drawing extends before the gradient starting point.
- [static var drawsAfterEndingLocation: NSGradient.DrawingOptions](./drawingoptions/drawsafterendinglocation.md)
  Drawing extends beyond the gradient end point.
### Initializers
- [init(rawValue: UInt)](./drawingoptions/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgradient/drawingoptions)*