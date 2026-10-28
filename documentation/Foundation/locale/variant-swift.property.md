# variant

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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
var variant: Locale.Variant? { get }
```

## Discussion

This property corresponds to the `va` key of the Unicode BCP 47 extension.

For locale instances created with the `va` specifier (such as `en-US@va=posix`), or with a custom [`Locale.Components`](./components.md), this property represents the custom variant. Otherwise, it represents the locale’s default variant.

## See Also

### Getting region components
- [var region: Locale.Region?](./region-swift.property.md)
  The region used by the locale.
- [Locale.Region](./region-swift.struct.md)
  A type that represents a geographic region, for use in specifying a locale or language.
- [var subdivision: Locale.Subdivision?](./subdivision-swift.property.md)
  The optional subdivision of the region used by this locale.
- [Locale.Subdivision](./subdivision-swift.struct.md)
  A type that represents a subdivision of a region, such as a state in the US or a province in Canada.
- [Locale.Variant](./variant-swift.struct.md)
  A type that represents a locale’s language variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/variant-swift.property)*