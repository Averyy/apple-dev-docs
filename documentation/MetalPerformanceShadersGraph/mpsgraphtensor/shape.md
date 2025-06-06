# shape

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The shape of the tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var shape: [NSNumber]? { get }
```

#### Discussion

Nil shape represents an unranked tensor. -1 value for a dimension represents that it will be resolved via shape inference at runtime and it can be anything.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphtensor/shape)*