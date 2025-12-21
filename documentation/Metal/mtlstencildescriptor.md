# MTLStencilDescriptor

**Framework**: Metal  
**Kind**: class

An object that defines the front-facing or back-facing stencil operations of a depth and stencil state object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLStencilDescriptor
```

#### Overview

A stencil test is a comparison between a masked reference value and a masked value stored in a stencil attachment. (A value is  by performing a logical AND operation on it with the [`readMask`](mtlstencildescriptor/readmask.md) value.) The [`MTLStencilDescriptor`](mtlstencildescriptor.md) object defines how to update the contents of the stencil attachment, based on the results of the stencil test and the depth test.

The [`stencilCompareFunction`](mtlstencildescriptor/stencilcomparefunction.md) property defines the stencil test. The [`stencilFailureOperation`](mtlstencildescriptor/stencilfailureoperation.md), [`depthFailureOperation`](mtlstencildescriptor/depthfailureoperation.md), and [`depthStencilPassOperation`](mtlstencildescriptor/depthstencilpassoperation.md) properties specify what to do to a stencil value stored in the stencil attachment for three different test outcomes: if the stencil test fails, if the stencil test passes and the depth test fails, or if both stencil and depth tests succeed, respectively. [`writeMask`](mtlstencildescriptor/writemask.md) determines which stencil bits can be modified as the result of a stencil operation.

## Topics

### Configuring stencil functions and operations
- [var stencilFailureOperation: MTLStencilOperation](mtlstencildescriptor/stencilfailureoperation.md)
  The operation that is performed to update the values in the stencil attachment when the stencil test fails.
- [var depthFailureOperation: MTLStencilOperation](mtlstencildescriptor/depthfailureoperation.md)
  The operation that is performed to update the values in the stencil attachment when the stencil test passes, but the depth test fails.
- [var depthStencilPassOperation: MTLStencilOperation](mtlstencildescriptor/depthstencilpassoperation.md)
  The operation that is performed to update the values in the stencil attachment when both the stencil test and the depth test pass.
- [var stencilCompareFunction: MTLCompareFunction](mtlstencildescriptor/stencilcomparefunction.md)
  The comparison that is performed between the masked reference value and a masked value in the stencil attachment.
- [enum MTLStencilOperation](mtlstenciloperation.md)
  The operation performed on a currently stored stencil value when a comparison test passes or fails.
### Configuring stencil bit mask properties
- [var readMask: UInt32](mtlstencildescriptor/readmask.md)
  A bitmask that determines from which bits that stencil comparison tests can read.
- [var writeMask: UInt32](mtlstencildescriptor/writemask.md)
  A bitmask that determines to which bits that stencil operations can write.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Calculating primitive visibility using depth testing](calculating-primitive-visibility-using-depth-testing.md)
  Determine which pixels are visible in a scene by using a depth texture.
- [protocol MTLDepthStencilState](mtldepthstencilstate.md)
  A depth and stencil state instance that specifies the depth and stencil configuration and operations used in a render pass.
- [class MTLDepthStencilDescriptor](mtldepthstencildescriptor.md)
  An instance that configures new [`MTLDepthStencilState`](mtldepthstencilstate.md) instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstencildescriptor)*