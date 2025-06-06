# strides

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

Defines strides for spatial dimensions. Must be four numbers, one for each spatial dimension, fastest running index last.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var strides: [NSNumber] { get set }
```

#### Discussion

Default value: `@[ @1, @1, @1, @1 ]`


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpooling4dopdescriptor/strides)*