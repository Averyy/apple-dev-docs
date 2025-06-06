# error

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A description of an error when the GPU encounters an issue as it runs the command buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var error: (any Error)? { get }
```

## Mentions

- [Preparing Your Metal App to Run in the Background](preparing-your-metal-app-to-run-in-the-background.md)

#### Discussion

You typically check this property during development to get more information about a runtime issue. The property remains `nil` unless the GPU can’t successfully run the command buffer.

An error’s [`userInfo`](https://developer.apple.com/documentation/foundation/nserror/1411580-userinfo) dictionary property contains additional information if the command buffer’s [`errorOptions`](mtlcommandbuffer/erroroptions.md) property includes [`encoderExecutionStatus`](mtlcommandbuffererroroption/encoderexecutionstatus.md). You can retrieve an [`MTLCommandBufferEncoderInfo`](mtlcommandbufferencoderinfo.md) instance from the dictionary by accessing it with [`MTLCommandBufferEncoderInfoErrorKey`](mtlcommandbufferencoderinfoerrorkey.md).

## See Also

- [var errorOptions: MTLCommandBufferErrorOption](mtlcommandbuffer/erroroptions.md)
  Settings that determine which information the command buffer records about execution errors, and how it does it.
- [protocol MTLCommandBufferEncoderInfo](mtlcommandbufferencoderinfo.md)
  A container that provides additional information about a runtime failure a GPU encounters as it runs the commands in a command buffer.
- [let MTLCommandBufferEncoderInfoErrorKey: String](mtlcommandbufferencoderinfoerrorkey.md)
  A key to a command buffer error’s user information dictionary that retrieves additional information about a GPU’s runtime error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/error)*