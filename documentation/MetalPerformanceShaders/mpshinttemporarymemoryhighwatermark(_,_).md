# MPSHintTemporaryMemoryHighWaterMark(_:_:)

**Framework**: Metal Performance Shaders  
**Kind**: func  
**Role**: Function

Triggers Metal Performance Shaders to prefetch a Metal heap of the indicated size into its internal cache.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func MPSHintTemporaryMemoryHighWaterMark(_ cmdBuf: any MTLCommandBuffer, _ bytes: Int)
```

```c
void MPSHintTemporaryMemoryHighWaterMark(id<MTLCommandBuffer>cmdBuf, NSUInteger bytes);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpshinttemporarymemoryhighwatermark(_:_:))*