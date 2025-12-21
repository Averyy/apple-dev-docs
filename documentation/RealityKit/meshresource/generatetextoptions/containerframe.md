# containerFrame

**Framework**: RealityKit  
**Kind**: property

The size in points of the frame where the text is laid out.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var containerFrame: CGRect?
```

#### Discussion

The points are scaled at a ratio of 72 points per meter.

The container frame has the same origin as the local coordinate system.

> **Note**: Use a value of `nil` to denote an arbitrarily large frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshresource/generatetextoptions/containerframe)*