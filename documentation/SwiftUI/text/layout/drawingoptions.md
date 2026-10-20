# Text.Layout.DrawingOptions

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Option flags used when drawing `Text.Layout` lines or runs into a graphics context.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@frozen
struct DrawingOptions
```

## Topics

### Type Properties
- [static var disablesSubpixelQuantization: Text.Layout.DrawingOptions](./drawingoptions/disablessubpixelquantization.md)
  If set, subpixel quantization requested by the text engine is disabled. This can be useful for text that will be animated to prevent it jittering.

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Copyable](../../../Swift/copyable.md)
- [Equatable](../../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../../Swift/optionset.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)
- [SetAlgebra](../../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/layout/drawingoptions)*