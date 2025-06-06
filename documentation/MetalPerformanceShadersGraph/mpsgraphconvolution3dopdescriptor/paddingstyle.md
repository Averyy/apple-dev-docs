# paddingStyle

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

The type of padding that is applied to the source tensor.

**Availability**:
- iOS 16.3+
- iPadOS 16.3+
- Mac Catalyst 16.3+
- macOS 13.2+
- tvOS 16.3+
- visionOS 1.0+

## Declaration

```swift
var paddingStyle: MPSGraphPaddingStyle { get set }
```

#### Discussion

If paddingStyle is `MPSGraphPaddingStyleExplicit`, `paddingLeft`, `laddingRight`, `paddingTop`, `paddingBottom`,   `paddingFront` and `paddingBack` must to be specified. For all other padding styles, framework compute these values so you dont need to provide these values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphconvolution3dopdescriptor/paddingstyle)*