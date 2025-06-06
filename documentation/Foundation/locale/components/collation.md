# collation

**Framework**: Foundation  
**Kind**: property

The string sort order of the locale.

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
var collation: Locale.Collation?
```

#### Discussion

Set this property to override the locale’s default string sort order. To request the collation used by the locale, use the [`Locale`](locale.md) property [`collation`](locale/collation-swift.property.md).

This property corresponds to the `co` key of the Unicode BCP 47 extension.

## See Also

- [Locale.Collation](locale/collation-swift.struct.md)
  A type that represents the string sort order used by the locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/components/collation)*