# label

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
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

```objc
@property (readonly, nullable) NSString * label;
```

#### Discussion

Labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../Xcode/naming-resources-and-commands.md).

## See Also

### Identifying a pipeline state
- [var device: any MTLDevice](./device.md)
  The device instance that created the pipeline state.
- [var gpuResourceID: MTLResourceID](./gpuresourceid.md)
  An unique identifier that represents the pipeline state, which you can add to an argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/label)*