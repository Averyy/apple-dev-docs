# Locale.IdentifierType.cldr

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

The type of identifiers that follow CLDR (Common Locale Data Repository) conventions.

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
case cldr
```

## Discussion

The components in this type of identifier use the same components as in [`Locale.IdentifierType.icu`](./icu.md), but don’t use the key-value type keyword list. An example of this type is `th_TH_u_ca_gregory_nu_thai`.

## See Also

### Standard Identifier Types
- [Locale.IdentifierType.icu](./icu.md)
  The type of identifiers that follow ICU (International Components for Unicode) conventions.
- [Locale.IdentifierType.bcp47](./bcp47.md)
  The type of BCP 47 language identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/identifiertype/cldr)*