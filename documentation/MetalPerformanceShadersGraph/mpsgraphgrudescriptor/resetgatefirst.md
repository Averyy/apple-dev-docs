# resetGateFirst

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

A parameter that controls the internal order of the GRU gates.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var resetGateFirst: Bool { get set }
```

#### Discussion

If set to `YES` then the layer will use the gate-ordering `[ r, z, o ]` instead of default `[ z, r, o ]`. Default value: `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphgrudescriptor/resetgatefirst)*