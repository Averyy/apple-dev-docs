# modifyUniforms(_:)

**Framework**: Compute Graph  
**Kind**: method

Provides read/write access to the entire uniforms buffer for CPU access.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
final func modifyUniforms<E, R>(_ body: (UnsafeMutableRawBufferPointer) throws(E) -> R) throws(E) -> R where E : Error, R : ~Copyable
```

#### Discussion

ComputeGraph will upload the changes to the GPU before the next simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/modifyuniforms(_:))*