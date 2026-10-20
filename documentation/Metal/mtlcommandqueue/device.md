# device

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The GPU device that creates the command queue.

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

The command queue can submit work only to the GPU the [`MTLDevice`](../mtldevice.md) instance represents.

## See Also

### Identifying the command queue
- [var label: String?](./label.md)
  An optional name that can help you identify the command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue/device)*