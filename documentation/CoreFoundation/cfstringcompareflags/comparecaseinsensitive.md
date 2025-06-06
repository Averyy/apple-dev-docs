# compareCaseInsensitive

**Framework**: Core Foundation  
**Kind**: property

Specifies that the comparison should ignore differences in case between alphabetical characters.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static var compareCaseInsensitive: CFStringCompareFlags { get }
```

## See Also

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
- [static var compareDiacriticInsensitive: CFStringCompareFlags](cfstringcompareflags/comparediacriticinsensitive.md)
  Specifies that the comparison should ignore diacritic markers.
- [static var compareWidthInsensitive: CFStringCompareFlags](cfstringcompareflags/comparewidthinsensitive.md)
  Specifies that the comparison should ignore width differences.
- [static var compareForcedOrdering: CFStringCompareFlags](cfstringcompareflags/compareforcedordering.md)
  Specifies that the comparison is forced to return either `kCFCompareLessThan` or `kCFCompareGreaterThan` if the strings are equivalent but not strictly equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/comparecaseinsensitive)*