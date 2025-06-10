# MTLCommandBufferEncoderInfoErrorKey

**Framework**: Metal  
**Kind**: var

A key to a command buffer error’s user information dictionary that retrieves additional information about a GPU’s runtime error.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
let MTLCommandBufferEncoderInfoErrorKey: String
```

#### Discussion

You can retrieve an [`MTLCommandBufferEncoderInfo`](mtlcommandbufferencoderinfo.md) instance from the [`userInfo`](https://developer.apple.com/documentation/Foundation/NSError/userInfo) dictionary of a command buffer’s [`error`](mtlcommandbuffer/error.md) property.

## See Also

- [var error: (any Error)?](mtlcommandbuffer/error.md)
  A description of an error when the GPU encounters an issue as it runs the command buffer.
- [var errorOptions: MTLCommandBufferErrorOption](mtlcommandbuffer/erroroptions.md)
  Settings that determine which information the command buffer records about execution errors, and how it does it.
- [protocol MTLCommandBufferEncoderInfo](mtlcommandbufferencoderinfo.md)
  A container that provides additional information about a runtime failure a GPU encounters as it runs the commands in a command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbufferencoderinfoerrorkey)*