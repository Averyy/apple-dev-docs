# setThreadgroupMemoryLength(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the size of a threadgroup memory buffer for a threadgroup argument in the compute shader function.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setThreadgroupMemoryLength(_ length: Int, index: Int)
```

## Parameters

- `length`: The size of the threadgroup memory, in bytes. Use a multiple of   bytes.
- `index`: An integer that corresponds to the index of the argument you annotate with attribute    in the shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/setthreadgroupmemorylength(_:index:))*