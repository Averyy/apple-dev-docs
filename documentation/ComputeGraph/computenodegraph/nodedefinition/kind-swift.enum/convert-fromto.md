# ComputeNodeGraph.NodeDefinition.Kind.convert(from:to:)

**Framework**: ComputeGraph  
**Kind**: case

Convert from one primitive MTLDataType to another.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
case convert(from: MTLDataType, to: MTLDataType)
```

#### Discussion

Equivalent to calling Metal’s constructor of `to` with a value of type `from`


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/nodedefinition/kind-swift.enum/convert(from:to:))*