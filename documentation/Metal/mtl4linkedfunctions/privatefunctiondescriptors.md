# privateFunctionDescriptors

**Framework**: Metal  
**Kind**: property

Provides an array of private functions to link at the Metal IR level.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var privateFunctionDescriptors: [MTL4FunctionDescriptor]? { get set }
```

#### Discussion

You specify private functions to link separately from [`functionDescriptors`](mtl4linkedfunctions/functiondescriptors.md) because pipelines don’t export private functions as [`MTLFunctionHandle`](mtlfunctionhandle.md) instances.

> **Note**: You can link private functions even when your [`MTLDevice`](mtldevice.md) doesn’t support function pointers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4linkedfunctions/privatefunctiondescriptors)*