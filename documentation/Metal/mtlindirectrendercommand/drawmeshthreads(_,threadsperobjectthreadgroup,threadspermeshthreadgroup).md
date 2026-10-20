# drawMeshThreads(_:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 18.1+
- visionOS 2.1+

## Declaration

```swift
func drawMeshThreads(_ threadsPerGrid: MTLSize, threadsPerObjectThreadgroup: MTLSize, threadsPerMeshThreadgroup: MTLSize)
```

```objc
- (void) drawMeshThreads:(MTLSize) threadsPerGrid threadsPerObjectThreadgroup:(MTLSize) threadsPerObjectThreadgroup threadsPerMeshThreadgroup:(MTLSize) threadsPerMeshThreadgroup;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindirectrendercommand/drawmeshthreads(_:threadsperobjectthreadgroup:threadspermeshthreadgroup:))*