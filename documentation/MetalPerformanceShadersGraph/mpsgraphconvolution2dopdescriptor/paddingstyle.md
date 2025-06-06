# paddingStyle

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The type of padding applied to the source tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var paddingStyle: MPSGraphPaddingStyle { get set }
```

#### Discussion

If paddingStyle is `MPSGraphPaddingStyleExplicit`, `paddingLeft`, `laddingRight`, `paddingTop`, and `paddingBottom` must to be specified. For all other padding styles, framework compute these values so you dont need to provide these values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution2dopdescriptor/paddingstyle)*