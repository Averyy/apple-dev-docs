# device

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The GPU device that creates the command queue.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var device: any MTLDevice { get }
```

#### Discussion

The command queue can submit work only to the GPU the [`MTLDevice`](mtldevice.md) instance represents.

## See Also

- [var label: String?](mtlcommandqueue/label.md)
  An optional name that can help you identify the command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue/device)*