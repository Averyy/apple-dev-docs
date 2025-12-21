# MTLCommandBufferEncoderInfo

**Framework**: Metal  
**Kind**: protocol

A container that provides additional information about a runtime failure a GPU encounters as it runs the commands in a command buffer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLCommandBufferEncoderInfo : NSObjectProtocol
```

#### Overview

To create a command buffer that generates additional information (when a GPU encounters an error running it), configure an [`MTLCommandBufferDescriptor`](mtlcommandbufferdescriptor.md) instance’s [`errorOptions`](mtlcommandbufferdescriptor/erroroptions.md) property. For information about how to retrieve the information from an [`MTLCommandBuffer`](mtlcommandbuffer.md) instance, see its [`error`](mtlcommandbuffer/error.md) property.

## Topics

### Inspecting execution information
- [var label: String](mtlcommandbufferencoderinfo/label.md)
  The name of the encoder that generates the error information.
- [var debugSignposts: [String]](mtlcommandbufferencoderinfo/debugsignposts.md)
  An array of debug signposts that Metal records as the GPU executes the commands of the encoder’s pass.
- [var errorState: MTLCommandEncoderErrorState](mtlcommandbufferencoderinfo/errorstate.md)
  The execution status of the command encoder.
- [enum MTLCommandEncoderErrorState](mtlcommandencodererrorstate.md)
  Possible error conditions for the command encoder’s commands.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var error: (any Error)?](mtlcommandbuffer/error.md)
  A description of an error when the GPU encounters an issue as it runs the command buffer.
- [var errorOptions: MTLCommandBufferErrorOption](mtlcommandbuffer/erroroptions.md)
  Settings that determine which information the command buffer records about execution errors, and how it does it.
- [let MTLCommandBufferEncoderInfoErrorKey: String](mtlcommandbufferencoderinfoerrorkey.md)
  A key to a command buffer error’s user information dictionary that retrieves additional information about a GPU’s runtime error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbufferencoderinfo)*