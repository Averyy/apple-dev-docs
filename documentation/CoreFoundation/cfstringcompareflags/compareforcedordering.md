# compareForcedOrdering

**Framework**: Core Foundation  
**Kind**: property

Specifies that the comparison is forced to return either `kCFCompareLessThan` or `kCFCompareGreaterThan` if the strings are equivalent but not strictly equal.

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
static var compareForcedOrdering: CFStringCompareFlags { get }
```

#### Discussion

You use this option for stability when sorting (for example, with `kCFCompareCaseInsensitive` specified “aaa” is greater than “AAA”).

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
- [static var compareDiacriticInsensitive: CFStringCompareFlags](cfstringcompareflags/comparediacriticinsensitive.md)
  Specifies that the comparison should ignore diacritic markers.
- [static var compareWidthInsensitive: CFStringCompareFlags](cfstringcompareflags/comparewidthinsensitive.md)
  Specifies that the comparison should ignore width differences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/compareforcedordering)*