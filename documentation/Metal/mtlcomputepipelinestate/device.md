# device

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The device instance that created the pipeline state.

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

This compute state instance is only usable on the device set in this property.

## See Also

- [var gpuResourceID: MTLResourceID](mtlcomputepipelinestate/gpuresourceid.md)
  An unique identifier that represents the pipeline state, which you can add to an argument buffer.
- [var label: String?](mtlcomputepipelinestate/label.md)
  A string that helps you identify the compute pipeline state during debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/device)*