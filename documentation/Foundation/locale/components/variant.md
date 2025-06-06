# variant

**Framework**: Foundation  
**Kind**: property

An optional variant used by the locale.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var variant: Locale.Variant?
```

#### Discussion

Set this property to override the variant of the locale.

This property corresponds to the `va` key of the Unicode BCP 47 extension.

## See Also

- [var region: Locale.Region?](locale/components/region.md)
  The region used by the locale.
- [Locale.Region](locale/region-swift.struct.md)
  A type that represents a geographic region, for use in specifying a locale or language.
- [var subdivision: Locale.Subdivision?](locale/components/subdivision.md)
  The optional subdivision of the region used by this locale.
- [Locale.Subdivision](locale/subdivision-swift.struct.md)
  A type that represents a subdivision of a region, such as a state in the US or a province in Canada.
- [Locale.Variant](locale/variant-swift.struct.md)
  A type that represents a locale’s languate variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/components/variant)*