# Unicode.CanonicalCombiningClass

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

The classification of a scalar used in the Canonical Ordering Algorithm defined by the Unicode Standard.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CanonicalCombiningClass
```

## Overview

Canonical combining classes are used by the ordering algorithm to determine if two sequences of combining marks should be considered canonically equivalent (that is, identical in interpretation). Two sequences are canonically equivalent if they are equal when sorting the scalars in ascending order by their combining class.

For example, consider the sequence `"\u{0041}\u{0301}\u{0316}"` (LATIN CAPITAL LETTER A, COMBINING ACUTE ACCENT, COMBINING GRAVE ACCENT BELOW). The combining classes of these scalars have the numeric values 0, 230, and 220, respectively. Sorting these scalars by their combining classes yields `"\u{0041}\u{0316}\u{0301}"`, so two strings that differ only by the ordering of those scalars would compare as equal:

```swift
let aboveBeforeBelow = "\u{0041}\u{0301}\u{0316}"
let belowBeforeAbove = "\u{0041}\u{0316}\u{0301}"
print(aboveBeforeBelow == belowBeforeAbove)
// Prints "true"
```

## Named and Unnamed Combining Classes

Canonical combining classes are defined in the Unicode Standard as integers in the range `0...254`. For convenience, the standard assigns symbolic names to a subset of these combining classes.

The `CanonicalCombiningClass` type conforms to `RawRepresentable` with a raw value of type `UInt8`. You can create instances of the type by using the static members named after the symbolic names, or by using the `init(rawValue:)` initializer.

```swift
let overlayClass = Unicode.CanonicalCombiningClass(rawValue: 1)
let overlayClassIsOverlay = overlayClass == .overlay
// overlayClassIsOverlay == true
```

## Topics

### Operators
- [static func == (Unicode.CanonicalCombiningClass, Unicode.CanonicalCombiningClass) -> Bool](./canonicalcombiningclass/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (Unicode.CanonicalCombiningClass, Unicode.CanonicalCombiningClass) -> Bool](./canonicalcombiningclass/op%28_,_%29.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
### Initializers
- [init(rawValue: UInt8)](./canonicalcombiningclass/init%28rawvalue%29.md)
  Creates a new canonical combining class with the given raw integer value.
### Instance Properties
- [var hashValue: Int](./canonicalcombiningclass/hashvalue.md)
  The hash value.
- [let rawValue: UInt8](./canonicalcombiningclass/rawvalue-swift.property.md)
  The raw integer value of the canonical combining class.
### Instance Methods
- [func hash(into: inout Hasher)](./canonicalcombiningclass/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [Unicode.CanonicalCombiningClass.RawValue](./canonicalcombiningclass/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let above: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/above.md)
  Distinct marks directly above.
- [static let aboveLeft: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/aboveleft.md)
  Distinct marks at the top left.
- [static let aboveRight: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/aboveright.md)
  Distinct marks at the top right.
- [static let attachedAbove: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/attachedabove.md)
  Marks attached directly above.
- [static let attachedAboveRight: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/attachedaboveright.md)
  Marks attached at the top right.
- [static let attachedBelow: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/attachedbelow.md)
  Marks attached directly below.
- [static let attachedBelowLeft: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/attachedbelowleft.md)
  Marks attached at the bottom left.
- [static let below: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/below.md)
  Distinct marks directly below.
- [static let belowLeft: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/belowleft.md)
  Distinct marks at the bottom left.
- [static let belowRight: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/belowright.md)
  Distinct marks at the bottom right.
- [static let doubleAbove: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/doubleabove.md)
  Distinct marks extending above two bases.
- [static let doubleBelow: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/doublebelow.md)
  Distinct marks subtending two bases.
- [static let iotaSubscript: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/iotasubscript.md)
  Greek iota subscript only (U+0345 COMBINING GREEK YPOGEGRAMMENI).
- [static let kanaVoicing: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/kanavoicing.md)
  Combining marks that are attached to hiragana and katakana to indicate voicing changes.
- [static let left: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/left.md)
  Distinct marks to the left.
- [static let notReordered: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/notreordered.md)
  Base glyphs that occupy their own space and do not combine with others.
- [static let nukta: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/nukta.md)
  Diacritic nukta marks in Brahmi-derived scripts.
- [static let overlay: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/overlay.md)
  Marks that overlay a base letter or symbol.
- [static let right: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/right.md)
  Distinct marks to the right.
- [static let virama: Unicode.CanonicalCombiningClass](./canonicalcombiningclass/virama.md)
  Diacritic virama marks in Brahmi-derived scripts.
### Default Implementations
- [Comparable Implementations](./canonicalcombiningclass/comparable-implementations.md)
- [Equatable Implementations](./canonicalcombiningclass/equatable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../comparable.md)
- [Equatable](../equatable.md)
- [Hashable](../hashable.md)
- [RawRepresentable](../rawrepresentable.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)

## See Also

### Unicode Scalar Classifications
- [Unicode.GeneralCategory](./generalcategory.md)
  The most general classification of a Unicode scalar.
- [Unicode.NumericType](./numerictype.md)
  The numeric type of a scalar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/canonicalcombiningclass)*