# makeComputeCommandEncoder()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a compute command encoder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeComputeCommandEncoder() -> (any MTL4ComputeCommandEncoder)?
```

```objc
- (id<MTL4ComputeCommandEncoder>) computeCommandEncoder;
```

## Return Value

The created [`MTL4ComputeCommandEncoder`](../mtl4computecommandencoder.md) instance, or `nil` if the function fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandbuffer/makecomputecommandencoder())*