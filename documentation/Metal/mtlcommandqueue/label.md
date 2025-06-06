# label

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

An optional name that can help you identify the command queue.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get set }
```

#### Discussion

Set labels to help you quickly identify a GPU at runtime in the Metal debugging and profiling tools. See `Enhancing Frame Capture by Using Labels`.

## See Also

- [var device: any MTLDevice](mtlcommandqueue/device.md)
  The GPU device that creates the command queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandqueue/label)*