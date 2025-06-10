# blendMode

**Framework**: RealityKit  
**Kind**: property

Modes that describe how materials using the created `UnlitMaterial.Program` will be blended with content behind them.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS ?+
- visionOS 2.0+

## Declaration

```swift
var blendMode: MaterialParameterTypes.BlendMode?
```

#### Discussion

Default value is nil, which will cause this material to render opaque, and not blend with background content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unlitmaterial/program-9tv7i/descriptor-swift.struct/blendmode)*