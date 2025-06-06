# offsets

**Framework**: Metal Performance Shaders Graph  
**Kind**: property

An array of length four that determines from which offset to start reading the input tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var offsets: [NSNumber] { get set }
```

#### Discussion

Only used when `paddingStyle` is `MPSGraphPaddingStyleExplicitOffset`. For example zero offset means that the first stencil window will align its top-left corner (in 4 dimensions) to the top-left corner of the input tensor. Default value: `@[ @0, @0, @0, @0 ]`


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphstencilopdescriptor/offsets)*