# compareWidthInsensitive

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

Specifies that the comparison should ignore width differences.

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
static var compareWidthInsensitive: CFStringCompareFlags { get }
```

```c
kCFCompareWidthInsensitive
```

#### Discussion

For example, “a”  is equivalent to `UFF41`.

## See Also

### Constants
- [static var compareCaseInsensitive: CFStringCompareFlags](./comparecaseinsensitive.md)
  Specifies that the comparison should ignore differences in case between alphabetical characters.
- [static var compareBackwards: CFStringCompareFlags](./comparebackwards.md)
  Specifies that the comparison should start at the last elements of the entities being compared (for example, strings or arrays).
- [static var compareAnchored: CFStringCompareFlags](./compareanchored.md)
  Performs searching only on characters at the beginning or end of the range.
- [static var compareNonliteral: CFStringCompareFlags](./comparenonliteral.md)
  Specifies that loose equivalence is acceptable, especially as pertains to diacritical marks.
- [static var compareLocalized: CFStringCompareFlags](./comparelocalized.md)
  Specifies that the comparison should take into account differences related to locale, such as the thousands separator character.
- [static var compareNumerically: CFStringCompareFlags](./comparenumerically.md)
  Specifies that represented numeric values should be used as the basis for comparison and not the actual character values.
- [static var compareDiacriticInsensitive: CFStringCompareFlags](./comparediacriticinsensitive.md)
  Specifies that the comparison should ignore diacritic markers.
- [static var compareForcedOrdering: CFStringCompareFlags](./compareforcedordering.md)
  Specifies that the comparison is forced to return either `kCFCompareLessThan` or `kCFCompareGreaterThan` if the strings are equivalent but not strictly equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags/comparewidthinsensitive)*