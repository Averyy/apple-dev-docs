# errorOptions

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Settings that determine which information the command buffer records about execution errors, and how it does it.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var errorOptions: MTLCommandBufferErrorOption { get }
```

```objc
@property (readonly) MTLCommandBufferErrorOption errorOptions;
```

#### Discussion

The property reflects the [`errorOptions`](../mtlcommandbufferdescriptor/erroroptions.md) property of the [`MTLCommandBufferDescriptor`](../mtlcommandbufferdescriptor.md) instance at the time you create the command buffer.

## See Also

### Getting error details
- [var error: (any Error)?](./error.md)
  A description of an error when the GPU encounters an issue as it runs the command buffer.
- [protocol MTLCommandBufferEncoderInfo](../mtlcommandbufferencoderinfo.md)
  A container that provides additional information about a runtime failure a GPU encounters as it runs the commands in a command buffer.
- [let MTLCommandBufferEncoderInfoErrorKey: String](../mtlcommandbufferencoderinfoerrorkey.md)
  A key to a command buffer error’s user information dictionary that retrieves additional information about a GPU’s runtime error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/erroroptions)*