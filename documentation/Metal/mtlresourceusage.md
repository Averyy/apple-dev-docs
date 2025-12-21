# MTLResourceUsage

**Framework**: Metal  
**Kind**: struct

Options that describe how a graphics or compute function uses an argument buffer’s resource.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLResourceUsage
```

## Mentions

- [Tracking the resource residency of argument buffers](tracking-the-resource-residency-of-argument-buffers.md)

#### Overview

You can combine multiple [`MTLResourceUsage`](mtlresourceusage.md) values with a bitwise OR (`|`) if the resource serves multiple purposes over its lifetime. You can enable options for certain resources that indicate whether the Metal driver needs to convert the resource to another format, such as whether it needs to decompress a color render target.

## Topics

### Initializers
- [init(rawValue: UInt)](mtlresourceusage/init(rawvalue:).md)
  Creates a set of resource options from a raw value.
### Type Properties
- [static var read: MTLResourceUsage](mtlresourceusage/read.md)
  An option that enables reading from the resource.
- [static var sample: MTLResourceUsage](mtlresourceusage/sample.md)
  An option that enables sampling from the resource.
- [static var write: MTLResourceUsage](mtlresourceusage/write.md)
  An option that enables writing to the resource.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [typealias MTLGPUAddress](mtlgpuaddress.md)
  A 64-bit unsigned integer type appropriate for storing GPU addresses.
- [protocol MTLAllocation](mtlallocation.md)
  A memory allocation from a Metal GPU device, such as a memory heap, texture, or data buffer.
- [protocol MTLResource](mtlresource.md)
  An allocation of memory accessible to a GPU.
- [struct MTLResourceOptions](mtlresourceoptions.md)
  Optional arguments used to set the behavior of a resource.
- [struct MTLResourceID](mtlresourceid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceusage)*