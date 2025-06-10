# BNNSGraph.Builder.ConvolutionPadding.custom(padding:)

**Framework**: Accelerate  
**Kind**: case

Custom padding

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
case custom(padding: [Int])
```

#### Discussion

Specify the `padding` array to contain twice the number of spatial dimensions. `padding[2*k]` specifies the amount of padding before spatial dimension `k`, and `padding[2*k+1]` specifies the amount of padding after spatial dimension `k`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/convolutionpadding/custom(padding:))*