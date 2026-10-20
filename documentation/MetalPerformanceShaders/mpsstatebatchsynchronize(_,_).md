# MPSStateBatchSynchronize(_:_:)

**Framework**: Metal Performance Shaders  
**Kind**: func  
**Role**: Function

Removes any copy of the specified state batch from the device’s caches, and, if needed, invalidates any CPU caches.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func MPSStateBatchSynchronize(_ batch: [MPSState], _ cmdBuf: any MTLCommandBuffer)
```

```c
void MPSStateBatchSynchronize(MPSStateBatch *batch, id<MTLCommandBuffer>cmdBuf);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsstatebatchsynchronize(_:_:))*