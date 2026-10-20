# MPSSetHeapCacheDuration(_:_:)

**Framework**: Metal Performance Shaders  
**Kind**: func  
**Role**: Function

Sets the timeout after which unused cached Metal heaps are released.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
func MPSSetHeapCacheDuration(_ cmdBuf: any MTLCommandBuffer, _ seconds: Double)
```

```c
void MPSSetHeapCacheDuration(id<MTLCommandBuffer>cmdBuf, double seconds);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssetheapcacheduration(_:_:))*