# region

**Framework**: Foundation  
**Kind**: property

The region used by the locale.

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
var region: Locale.Region?
```

#### Discussion

Set this property to override the region for region-related preferences, such as measuring system, calendar, and first day of the week. If unset, the locale uses the region of the language component.

This property corresponds to the `rg` key of the Unicode BCP 47 extension.

## See Also

- [Locale.Region](locale/region-swift.struct.md)
  A type that represents a geographic region, for use in specifying a locale or language.
- [var subdivision: Locale.Subdivision?](locale/components/subdivision.md)
  The optional subdivision of the region used by this locale.
- [Locale.Subdivision](locale/subdivision-swift.struct.md)
  A type that represents a subdivision of a region, such as a state in the US or a province in Canada.
- [var variant: Locale.Variant?](locale/components/variant.md)
  An optional variant used by the locale.
- [Locale.Variant](locale/variant-swift.struct.md)
  A type that represents a locale’s languate variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/components/region)*