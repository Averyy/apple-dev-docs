# personalizationPolicy

**Framework**: Image Playground  
**Kind**: property

The policy to apply when determining whether to include people in generated images.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
@preconcurrency var personalizationPolicy: ImagePlaygroundPersonalizationPolicy { get set }
```

#### Discussion

Personalization lets the view controller offer support for incorporating people into the images it generates. When enabled, the view controller allows someone to build images that include:

- A person from their Photos library
- A character represented by an appearance and a skin tone

When enabled, the view controller offers a way to import an image of a person from the Photos library. It also supports choosing someone from a people picker, and by detecting names in any input text and using that information to find images.

The default value of this property is [`ImagePlaygroundPersonalizationPolicy.automatic`](imageplaygroundpersonalizationpolicy/automatic.md), which corresponds to [`ImagePlaygroundPersonalizationPolicy.enabled`](imageplaygroundpersonalizationpolicy/enabled.md).

## See Also

- [var selectedGenerationStyle: ImagePlaygroundStyle](imageplaygroundviewcontroller/selectedgenerationstyle.md)
  Generation style to pre-select upong launching the playground among those in `allowedGenerationStyles`.
- [var allowedGenerationStyles: [ImagePlaygroundStyle]](imageplaygroundviewcontroller/allowedgenerationstyles.md)
  A list of allowed generation styles to choose from in the playground.
- [enum ImagePlaygroundPersonalizationPolicy](imageplaygroundpersonalizationpolicy.md)
  A policy for enabling or disabling personalization in the system interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundviewcontroller/personalizationpolicy)*