# gpuResourceID

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (readonly) MTLResourceID gpuResourceID;
```

## See Also

### Identifying a pipeline state
- [var device: any MTLDevice](./device.md)
  The device instance that creates the pipeline state.
- [var label: String?](./label.md)
  A string that helps you identify the render pipeline state during debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/gpuresourceid)*