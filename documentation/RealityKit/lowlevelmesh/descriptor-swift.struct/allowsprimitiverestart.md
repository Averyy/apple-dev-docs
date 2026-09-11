# allowsPrimitiveRestart

**Framework**: RealityKit  
**Kind**: property

When true, primitive-restart index values (0xFFFF for .uint16, 0xFFFFFFFF for .uint32) are permitted in the index buffer. Every part must then use a strip topology (.triangleStrip or .lineStrip); any other topology is rejected.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var allowsPrimitiveRestart: Bool
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/descriptor-swift.struct/allowsprimitiverestart)*