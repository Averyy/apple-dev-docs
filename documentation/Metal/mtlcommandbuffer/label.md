# label

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An optional name that can help you identify the command buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var label: String? { get set }
```

```objc
@property (atomic, copy, nullable) NSString * label;
```

#### Discussion

Set labels to help you quickly identify a command buffer at runtime in the Metal debugging and profiling tools. See [Naming resources and commands](../../Xcode/naming-resources-and-commands.md).

## See Also

### Identifying the command buffer
- [var commandQueue: any MTLCommandQueue](./commandqueue.md)
  The command queue that creates the command buffer.
- [var device: any MTLDevice](./device.md)
  The GPU device that indirectly owns the command buffer because you create it from a command queue the device also owns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/label)*