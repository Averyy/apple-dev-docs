# writesDepth

**Framework**: RealityKit  
**Kind**: property

A boolean value that determines whether this material writes its depth into RealityKit’s depth buffer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var writesDepth: Bool { get set }
```

#### Discussion

If true, meshes with this material will occlude objects behind them by writing their depth into RealityKit’s depth buffer.

If false, meshes with this material will not write their depth into RealityKit’s depth buffer, and may be overwritten by objects drawn behind them, depending on draw order.

The default value is true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/videomaterial/writesdepth-6i035)*