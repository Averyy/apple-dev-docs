# String Comparison Flags

**Framework**: Core Foundation

Flags that specify how string comparisons are performed.

#### Overview

These constants are flags intended for use in the comparison-option parameters in comparison functions such as [`CFStringCompare(_:_:_:)`](cfstringcompare(_:_:_:).md). If you want to request multiple options, combine them with a bitwise-OR operation.

## Topics

### Constants
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
- [static var compareForcedOrdering: CFStringCompareFlags](cfstringcompareflags/compareforcedordering.md)
  Specifies that the comparison is forced to return either `kCFCompareLessThan` or `kCFCompareGreaterThan` if the strings are equivalent but not strictly equal.

## See Also

- [enum CFStringBuiltInEncodings](cfstringbuiltinencodings.md)
  Encodings that are built-in on all platforms on which macOS runs.
- [Invalid String Encoding Flag](invalid-string-encoding-flag.md)
  Special value returned from functions to indicate a string encoding that is not supported or recognized by CFString.
- [External String Encodings](external-string-encodings.md)
  `CFStringEncoding` constants for encodings that may be supported by CFString.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/string-comparison-flags)*