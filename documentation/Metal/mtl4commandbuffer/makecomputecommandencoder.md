# makeComputeCommandEncoder()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a compute command encoder.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeComputeCommandEncoder() -> (any MTL4ComputeCommandEncoder)?
```

#### Return Value

The created [`MTL4ComputeCommandEncoder`](mtl4computecommandencoder.md) instance, or `nil` if the function fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/makecomputecommandencoder())*