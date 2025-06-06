# compareDiacriticInsensitive

**Framework**: Core Foundation  
**Kind**: property

Specifies that the comparison should ignore diacritic markers.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var compareDiacriticInsensitive: CFStringCompareFlags { get }
```

#### Discussion

For example, “ö” (“o-umlaut”) is equivalent to “o”.

Diacritic markers are designated as all non-spacing marks below `U+0510`.

## See Also

- [static var compareCaseInsensitive: CFStringCompareFlags](cfstringcompareflags/comparecaseinsensitive.md)
  Specifies that the comparison should ignore differences in case between alphabetical characters.
- [static var compareBackwards: CFStringCompareFlags](cfstringcompareflags/comparebackwards.md)
  Specifies that the comparison should start at the last elements of the entities being compared (for example, strings or arrays).
- [static var compareAnchored: CFStringCompareFlags](cfstringcompareflags/compareanchored.md)
  Performs searching only on characters at the beginning or end of the range.
- [static var compareNonliteral: CFStringCompareFlags](cfstringcompareflags/comparenonliteral.md)
  Specifies that loose equivalence is acceptable, especially as pertains to diacritical marks.
- [static var compareLocalized: CFStringCompareFlags](cfstringcompareflags/comparelocalized.md)
  Specifies that the comparison should take into account differences related to locale, such as the thousands separator character.
- [static var compareNumerically: CFStringCompareFlags](cfstringcompareflags/comparenumerically.md)
  Specifies that represented numeric values should be used as the basis for comparison and not the actual character values.
- [static var compareWidthInsensitive: CFStringCompareFlags](cfstringcompareflags/comparewidthinsensitive.md)
  Specifies that the comparison should ignore width differences.
- [static var compareForcedOrdering: CFStringCompareFlags](cfstringcompareflags/compareforcedordering.md)
  Specifies that the comparison is forced to return either `kCFCompareLessThan` or `kCFCompareGreaterThan` if the strings are equivalent but not strictly equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/comparediacriticinsensitive)*