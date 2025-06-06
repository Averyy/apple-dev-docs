# device

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The device instance that creates the pipeline state.

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

You can only use the pipeline state object with this device object.

## See Also

- [var label: String?](mtlrenderpipelinestate/label.md)
  A string that helps you identify the render pipeline state during debugging.
- [var gpuResourceID: MTLResourceID](mtlrenderpipelinestate/gpuresourceid.md)
  An unique identifier that represents the pipeline state, which you can add to an argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/device)*