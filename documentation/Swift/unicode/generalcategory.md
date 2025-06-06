# Unicode.GeneralCategory

**Framework**: Swift  
**Kind**: enum

The most general classification of a Unicode scalar.

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
enum GeneralCategory
```

#### Overview

The general category of a scalar is its “first-order, most usual categorization”. It does not attempt to cover multiple uses of some scalars, such as the use of letters to represent Roman numerals.

## Topics

### Operators
- [static func == (Unicode.GeneralCategory, Unicode.GeneralCategory) -> Bool](unicode/generalcategory/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [Unicode.GeneralCategory.closePunctuation](unicode/generalcategory/closepunctuation.md)
  A closing punctuation mark of a pair.
- [Unicode.GeneralCategory.connectorPunctuation](unicode/generalcategory/connectorpunctuation.md)
  A connecting punctuation mark, like a tie.
- [Unicode.GeneralCategory.control](unicode/generalcategory/control.md)
  A C0 or C1 control code.
- [Unicode.GeneralCategory.currencySymbol](unicode/generalcategory/currencysymbol.md)
  A currency sign.
- [Unicode.GeneralCategory.dashPunctuation](unicode/generalcategory/dashpunctuation.md)
  A dash or hyphen punctuation mark.
- [Unicode.GeneralCategory.decimalNumber](unicode/generalcategory/decimalnumber.md)
  A decimal digit.
- [Unicode.GeneralCategory.enclosingMark](unicode/generalcategory/enclosingmark.md)
  An enclosing combining mark.
- [Unicode.GeneralCategory.finalPunctuation](unicode/generalcategory/finalpunctuation.md)
  A final quotation mark.
- [Unicode.GeneralCategory.format](unicode/generalcategory/format.md)
  A format control character.
- [Unicode.GeneralCategory.initialPunctuation](unicode/generalcategory/initialpunctuation.md)
  An initial quotation mark.
- [Unicode.GeneralCategory.letterNumber](unicode/generalcategory/letternumber.md)
  A letter-like numeric character.
- [Unicode.GeneralCategory.lineSeparator](unicode/generalcategory/lineseparator.md)
  A line separator, which is specifically (and only) U+2028 LINE SEPARATOR.
- [Unicode.GeneralCategory.lowercaseLetter](unicode/generalcategory/lowercaseletter.md)
  A lowercase letter.
- [Unicode.GeneralCategory.mathSymbol](unicode/generalcategory/mathsymbol.md)
  A symbol of mathematical use.
- [Unicode.GeneralCategory.modifierLetter](unicode/generalcategory/modifierletter.md)
  A modifier letter.
- [Unicode.GeneralCategory.modifierSymbol](unicode/generalcategory/modifiersymbol.md)
  A non-letterlike modifier symbol.
- [Unicode.GeneralCategory.nonspacingMark](unicode/generalcategory/nonspacingmark.md)
  A non-spacing combining mark with zero advance width (abbreviated Mn).
- [Unicode.GeneralCategory.openPunctuation](unicode/generalcategory/openpunctuation.md)
  An opening punctuation mark of a pair.
- [Unicode.GeneralCategory.otherLetter](unicode/generalcategory/otherletter.md)
  Other letters, including syllables and ideographs.
- [Unicode.GeneralCategory.otherNumber](unicode/generalcategory/othernumber.md)
  A numeric character of another type.
- [Unicode.GeneralCategory.otherPunctuation](unicode/generalcategory/otherpunctuation.md)
  A punctuation mark of another type.
- [Unicode.GeneralCategory.otherSymbol](unicode/generalcategory/othersymbol.md)
  A symbol of another type.
- [Unicode.GeneralCategory.paragraphSeparator](unicode/generalcategory/paragraphseparator.md)
  A paragraph separator, which is specifically (and only) U+2029 PARAGRAPH SEPARATOR.
- [Unicode.GeneralCategory.privateUse](unicode/generalcategory/privateuse.md)
  A private-use character.
- [Unicode.GeneralCategory.spaceSeparator](unicode/generalcategory/spaceseparator.md)
  A space character of non-zero width.
- [Unicode.GeneralCategory.spacingMark](unicode/generalcategory/spacingmark.md)
  A spacing combining mark with positive advance width.
- [Unicode.GeneralCategory.surrogate](unicode/generalcategory/surrogate.md)
  A surrogate code point.
- [Unicode.GeneralCategory.titlecaseLetter](unicode/generalcategory/titlecaseletter.md)
  A digraph character whose first part is uppercase.
- [Unicode.GeneralCategory.unassigned](unicode/generalcategory/unassigned.md)
  A reserved unassigned code point or a non-character.
- [Unicode.GeneralCategory.uppercaseLetter](unicode/generalcategory/uppercaseletter.md)
  An uppercase letter.
### Instance Properties
- [var hashValue: Int](unicode/generalcategory/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](unicode/generalcategory/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](unicode/generalcategory/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)

## See Also

- [Unicode.CanonicalCombiningClass](unicode/canonicalcombiningclass.md)
  The classification of a scalar used in the Canonical Ordering Algorithm defined by the Unicode Standard.
- [Unicode.NumericType](unicode/numerictype.md)
  The numeric type of a scalar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/generalcategory)*