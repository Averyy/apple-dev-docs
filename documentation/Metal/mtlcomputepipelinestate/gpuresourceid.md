# gpuResourceID

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

An unique identifier that represents the pipeline state, which you can add to an argument buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var gpuResourceID: MTLResourceID { get }
```

## Mentions

- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)

## See Also

- [var device: any MTLDevice](mtlcomputepipelinestate/device.md)
  The device instance that created the pipeline state.
- [var label: String?](mtlcomputepipelinestate/label.md)
  A string that helps you identify the compute pipeline state during debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/gpuresourceid)*