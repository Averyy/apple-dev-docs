# commandQueue

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The command queue that creates the command buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var commandQueue: any MTLCommandQueue { get }
```

#### Discussion

Each command buffer can only submit its commands to the queue that creates it.

## See Also

- [var label: String?](mtlcommandbuffer/label.md)
  An optional name that can help you identify the command buffer.
- [var device: any MTLDevice](mtlcommandbuffer/device.md)
  The GPU device that indirectly owns the command buffer because you create it from a command queue the device also owns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/commandqueue)*