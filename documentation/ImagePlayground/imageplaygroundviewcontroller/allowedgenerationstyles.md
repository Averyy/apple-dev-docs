# allowedGenerationStyles

**Framework**: Image Playground  
**Kind**: property

A list of allowed generation styles to choose from in the playground.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency var allowedGenerationStyles: [ImagePlaygroundStyle] { get set }
```

#### Discussion

The `selectedGenerationStyle` is expected to be included in this list.

Use `ImagePlaygroundStyle/all` to check the list of all possible styles, and pass a subset of those.

## See Also

- [var selectedGenerationStyle: ImagePlaygroundStyle](imageplaygroundviewcontroller/selectedgenerationstyle.md)
  Generation style to pre-select upong launching the playground among those in `allowedGenerationStyles`.
- [var personalizationPolicy: ImagePlaygroundPersonalizationPolicy](imageplaygroundviewcontroller/personalizationpolicy.md)
  The policy to apply when determining whether to include people in generated images.
- [enum ImagePlaygroundPersonalizationPolicy](imageplaygroundpersonalizationpolicy.md)
  A policy for enabling or disabling personalization in the system interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/allowedgenerationstyles)*