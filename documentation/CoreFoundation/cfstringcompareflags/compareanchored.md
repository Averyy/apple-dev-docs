# compareAnchored

**Framework**: Core Foundation  
**Kind**: property

Performs searching only on characters at the beginning or end of the range.

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
static var compareAnchored: CFStringCompareFlags { get }
```

#### Discussion

No match at the beginning or end means nothing is found, even if a matching sequence of characters occurs elsewhere in the string.

## See Also

- [static var compareCaseInsensitive: CFStringCompareFlags](cfstringcompareflags/comparecaseinsensitive.md)
  Specifies that the comparison should ignore differences in case between alphabetical characters.
- [static var compareBackwards: CFStringCompareFlags](cfstringcompareflags/comparebackwards.md)
  Specifies that the comparison should start at the last elements of the entities being compared (for example, strings or arrays).
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/compareanchored)*