# CFStringCompareFlags

**Framework**: Core Foundation  
**Kind**: struct

A [`CFOptionFlags`](cfoptionflags.md) type for specifying options for string comparison .

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
struct CFStringCompareFlags
```

#### Overview

See [`String Comparison Flags`](string-comparison-flags.md) for values.

## Topics

### Initializers
- [init(rawValue: CFOptionFlags)](cfstringcompareflags/init(rawvalue:).md)
### Type Properties
- [static var compareAnchored: CFStringCompareFlags](cfstringcompareflags/compareanchored.md)
  Performs searching only on characters at the beginning or end of the range.
- [static var compareBackwards: CFStringCompareFlags](cfstringcompareflags/comparebackwards.md)
  Specifies that the comparison should start at the last elements of the entities being compared (for example, strings or arrays).
- [static var compareCaseInsensitive: CFStringCompareFlags](cfstringcompareflags/comparecaseinsensitive.md)
  Specifies that the comparison should ignore differences in case between alphabetical characters.
- [static var compareDiacriticInsensitive: CFStringCompareFlags](cfstringcompareflags/comparediacriticinsensitive.md)
  Specifies that the comparison should ignore diacritic markers.
- [static var compareForcedOrdering: CFStringCompareFlags](cfstringcompareflags/compareforcedordering.md)
  Specifies that the comparison is forced to return either `kCFCompareLessThan` or `kCFCompareGreaterThan` if the strings are equivalent but not strictly equal.
- [static var compareLocalized: CFStringCompareFlags](cfstringcompareflags/comparelocalized.md)
  Specifies that the comparison should take into account differences related to locale, such as the thousands separator character.
- [static var compareNonliteral: CFStringCompareFlags](cfstringcompareflags/comparenonliteral.md)
  Specifies that loose equivalence is acceptable, especially as pertains to diacritical marks.
- [static var compareNumerically: CFStringCompareFlags](cfstringcompareflags/comparenumerically.md)
  Specifies that represented numeric values should be used as the basis for comparison and not the actual character values.
- [static var compareWidthInsensitive: CFStringCompareFlags](cfstringcompareflags/comparewidthinsensitive.md)
  Specifies that the comparison should ignore width differences.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [typealias CFStringEncoding](cfstringencoding.md)
  An integer type for constants used to specify supported string encodings in various CFString functions.
- [enum CFStringEncodings](cfstringencodings.md)
  Index type for constants used to specify external string encodings.
- [struct CFStringInlineBuffer](cfstringinlinebuffer.md)
  Defines the buffer and related fields used for in-line buffer access of characters in CFString objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringcompareflags)*