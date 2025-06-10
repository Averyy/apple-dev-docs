# compactName

**Framework**: Foundation  
**Kind**: property

A locale-appropriate compact name notation.

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
static var compactName: NumberFormatStyleConfiguration.Notation { get }
```

#### Discussion

A compact name notation, when available in the format style’s locale, that uses prefixes or suffixes corresponding to powers of ten. The following example shows a compact name notation in the `fr_FR` locale:

```swift
let compactNameFormatted = 1234.formatted(.number
    .locale(Locale(identifier: "fr_FR"))
    .notation(.compactName)) // "1,2 k"
```

## See Also

- [static var automatic: NumberFormatStyleConfiguration.Notation](numberformatstyleconfiguration/notation/automatic.md)
  A notation that automatically provides locale-appropriate behavior.
- [static var scientific: NumberFormatStyleConfiguration.Notation](numberformatstyleconfiguration/notation/scientific.md)
  A notation constant that formats values with scientific notation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/numberformatstyleconfiguration/notation/compactname)*