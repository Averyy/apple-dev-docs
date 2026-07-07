# modifyUniforms(_:)

**Framework**: Compute Graph  
**Kind**: method

Provides read/write access to the entire uniforms buffer for CPU access.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
final func modifyUniforms<E, R>(_ body: (UnsafeMutableRawBufferPointer) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

ComputeGraph will upload the changes to the GPU before the next simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/modifyuniforms(_:))*