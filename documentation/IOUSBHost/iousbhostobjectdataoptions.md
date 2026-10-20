# IOUSBHostObjectDataOptions

**Framework**: IOUSBHost  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
struct IOUSBHostObjectDataOptions
```

```c
enum IOUSBHostObjectDataOptions : NSUInteger;
```

#### Overview

Options for dataWithCapacity:options:error

```
         task as well as the kernel.  This option is recommended when allocating isochronous frame lists.
```

## Topics

### Initializers
- [init(rawValue: UInt)](./iousbhostobjectdataoptions/init%28rawvalue%29.md)
### Type Properties
- [static var kernelUserShared: IOUSBHostObjectDataOptions](./iousbhostobjectdataoptions/kernelusershared.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobjectdataoptions)*