# tolerance

**Framework**: RealityKit  
**Kind**: property

An extension of the distance limit, as a percentage-based error tolerance.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var tolerance: Float
```

#### Discussion

For example, a tolerance of `0.01` extends the distance limit by `1` percent. When the pins exceed this distance, the joint constrains the pins until they are within the distance limit.

> ❗ **Important**: Use a non-negative value for the tolerance.

Use a non-negative value for the tolerance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsdistancejoint/tolerance)*