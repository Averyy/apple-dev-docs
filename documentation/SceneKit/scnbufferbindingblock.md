# SCNBufferBindingBlock

**Framework**: SceneKit  
**Kind**: typealias

A block SceneKit calls at render time for working with buffers in a Metal shader, used by the [`handleBinding(ofBufferNamed:frequency:handler:)`](scnprogram/handlebinding(ofbuffernamed:frequency:handler:).md) method.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
typealias SCNBufferBindingBlock = (any SCNBufferStream, SCNNode, any SCNShadable, SCNRenderer) -> Void
```

#### Discussion

The block takes the following parameters:

## See Also

- [func handleBinding(ofBufferNamed: String, frequency: SCNBufferFrequency, handler: SCNBufferBindingBlock)](scnprogram/handlebinding(ofbuffernamed:frequency:handler:).md)
  Registers a block for SceneKit to call at render time for binding a Metal buffer to the shader program.
- [enum SCNBufferFrequency](scnbufferfrequency.md)
  Options for how often SceneKit should execute the binding handler you provide with the [`handleBinding(ofBufferNamed:frequency:handler:)`](scnprogram/handlebinding(ofbuffernamed:frequency:handler:).md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbufferbindingblock)*