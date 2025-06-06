# selectedGenerationStyle

**Framework**: Image Playground  
**Kind**: property

Generation style to pre-select upong launching the playground among those in `allowedGenerationStyles`.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency var selectedGenerationStyle: ImagePlaygroundStyle { get set }
```

#### Discussion

Use `ImagePlaygroundStyle.all` to check the list of all possible styles, and pass one of those.

## See Also

- [var allowedGenerationStyles: [ImagePlaygroundStyle]](imageplaygroundviewcontroller/allowedgenerationstyles.md)
  A list of allowed generation styles to choose from in the playground.
- [var personalizationPolicy: ImagePlaygroundPersonalizationPolicy](imageplaygroundviewcontroller/personalizationpolicy.md)
  The policy to apply when determining whether to include people in generated images.
- [enum ImagePlaygroundPersonalizationPolicy](imageplaygroundpersonalizationpolicy.md)
  A policy for enabling or disabling personalization in the system interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/selectedgenerationstyle)*