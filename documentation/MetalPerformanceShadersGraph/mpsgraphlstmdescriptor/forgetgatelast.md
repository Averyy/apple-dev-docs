# forgetGateLast

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

A parameter that controls the internal order of the LSTM gates.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
var forgetGateLast: Bool { get set }
```

#### Discussion

If set to `YES` then the layer will use the gate-ordering `[ i, z, f, o ]` instead of default `[ i, f, z, o ]`. Default value: `NO`


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphlstmdescriptor/forgetgatelast)*