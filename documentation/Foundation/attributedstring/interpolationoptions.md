# AttributedString.InterpolationOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

Options that affect the behavior of string interpolation on the attributed string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct InterpolationOptions
```

## Topics

### Type Properties
- [static let insertAttributesWithoutMerging: AttributedString.InterpolationOptions](./interpolationoptions/insertattributeswithoutmerging.md)
  By default, interpolating an AttributedString will result in the final string having all attributes present at its interpolation point, plus all attributes from the beginning of the interpolated AttributedString. Specify this option to instead indicate that pre-existing attributes at the point of interpolation (e.g., those specified with Markdown syntax) must be ignored. The result will only have the attributes from the interpolated AttributedString. This option has no effect when formatting a plain-text String, since all attributes will be stripped anyway.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/interpolationoptions)*