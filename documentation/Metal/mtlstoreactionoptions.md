# MTLStoreActionOptions

**Framework**: Metal  
**Kind**: struct

Options that modify a store action.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLStoreActionOptions
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)

#### Overview

This property modifies the intended behavior of the store actions in the [`MTLStoreAction`](mtlstoreaction.md) enumeration.

## Topics

### Using programmable sample positions
- [static var customSamplePositions: MTLStoreActionOptions](mtlstoreactionoptions/customsamplepositions.md)
  An option that stores data in a sample-position–agnostic representation.
### Initializers
- [init(rawValue: UInt)](mtlstoreactionoptions/init(rawvalue:).md)
  Creates a store action option from a raw integer value.

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

## See Also

- [protocol MTLParallelRenderCommandEncoder](mtlparallelrendercommandencoder.md)
  An instance that splits up a single render pass so that it can be simultaneously encoded from multiple threads.
- [enum MTLLoadAction](mtlloadaction.md)
  Types of actions performed for an attachment at the start of a rendering pass.
- [enum MTLStoreAction](mtlstoreaction.md)
  Types of actions performed for an attachment at the end of a rendering pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstoreactionoptions)*