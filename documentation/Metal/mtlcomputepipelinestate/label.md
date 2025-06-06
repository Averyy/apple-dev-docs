# label

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

A string that helps you identify the compute pipeline state during debugging.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get }
```

#### Discussion

Labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See `Enhancing Frame Capture by Using Labels`.

## See Also

- [var device: any MTLDevice](mtlcomputepipelinestate/device.md)
  The device instance that created the pipeline state.
- [var gpuResourceID: MTLResourceID](mtlcomputepipelinestate/gpuresourceid.md)
  An unique identifier that represents the pipeline state, which you can add to an argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/label)*