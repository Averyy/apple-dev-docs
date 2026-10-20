# subdivision

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The optional subdivision of the region used by this locale.

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
var subdivision: Locale.Subdivision? { get }
```

#### Discussion

This property corresponds to the `sd` key of the Unicode BCP 47 extension.

## See Also

### Getting region components
- [var region: Locale.Region?](./region-swift.property.md)
  The region used by the locale.
- [Locale.Region](./region-swift.struct.md)
  A type that represents a geographic region, for use in specifying a locale or language.
- [Locale.Subdivision](./subdivision-swift.struct.md)
  A type that represents a subdivision of a region, such as a state in the US or a province in Canada.
- [var variant: Locale.Variant?](./variant-swift.property.md)
  An optional variant used by the locale.
- [Locale.Variant](./variant-swift.struct.md)
  A type that represents a locale’s language variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/subdivision-swift.property)*