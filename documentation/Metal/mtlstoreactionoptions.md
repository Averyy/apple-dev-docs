# MTLStoreActionOptions

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

Options that modify a store action.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.13+ - Deprecated in 27.0
- tvOS 11.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Store action options have no effect on Apple Silicon

## Declaration

```swift
struct MTLStoreActionOptions
```

```c
enum MTLStoreActionOptions : NSUInteger;
```

## Mentions

- [Understanding the Metal 4 core API](./understanding-the-metal-4-core-api.md)

#### Overview

This property modifies the intended behavior of the store actions in the [`MTLStoreAction`](./mtlstoreaction.md) enumeration.

## Topics

### Using programmable sample positions
- [static var customSamplePositions: MTLStoreActionOptions](./mtlstoreactionoptions/customsamplepositions.md)
  An option that stores data in a sample-position–agnostic representation.
### Initializers
- [init(rawValue: UInt)](./mtlstoreactionoptions/init%28rawvalue%29.md)
  Creates a store action option from a raw integer value.
### Enumeration Cases
- [MTLStoreActionOptionNone](./mtlstoreactionoptions/mtlstoreactionoptionnone.md)
  An option that doesn’t modify the intended behavior of a store action.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Encoding a render pass in parallel
- [protocol MTLParallelRenderCommandEncoder](./mtlparallelrendercommandencoder.md)
  An instance that splits up a single render pass so that it can be simultaneously encoded from multiple threads.
- [enum MTLLoadAction](./mtlloadaction.md)
  Types of actions performed for an attachment at the start of a rendering pass.
- [enum MTLStoreAction](./mtlstoreaction.md)
  Types of actions performed for an attachment at the end of a rendering pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstoreactionoptions)*