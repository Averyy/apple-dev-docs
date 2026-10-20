# device

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The GPU device that indirectly owns the command buffer because you create it from a command queue the device also owns.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var device: any MTLDevice { get }
```

```objc
@property (readonly) id<MTLDevice> device;
```

#### Discussion

The command buffer can only work with other instances that [`device`](./device.md) creates, directly or indirectly, such as buffers and textures.

## See Also

### Identifying the command buffer
- [var label: String?](./label.md)
  An optional name that can help you identify the command buffer.
- [var commandQueue: any MTLCommandQueue](./commandqueue.md)
  The command queue that creates the command buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/device)*