# inputColorChannels

**Framework**: Metal Performance Shaders  
**Kind**: property

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var inputColorChannels: Int { get }
```

#### Discussion

The number of color channels used by the conversion in the float4 texel

When the conversion is initialized with a NULL CGColorConversionInfoRef this value will be 0


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsfcolorconversion/inputcolorchannels)*