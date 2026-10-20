# Unicode.Scalar.Properties

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

A value that provides access to properties of a Unicode scalar that are defined by the Unicode standard.

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
struct Properties
```

## Topics

### Instance Properties
- [var age: Unicode.Version?](./properties-swift.struct/age.md)
  The earliest version of the Unicode Standard in which the scalar was assigned.
- [var canonicalCombiningClass: Unicode.CanonicalCombiningClass](./properties-swift.struct/canonicalcombiningclass.md)
  The canonical combining class of the scalar.
- [var changesWhenCaseFolded: Bool](./properties-swift.struct/changeswhencasefolded.md)
  A Boolean value indicating whether the scalar’s normalized form differs from the case-fold mapping of each constituent scalar.
- [var changesWhenCaseMapped: Bool](./properties-swift.struct/changeswhencasemapped.md)
  A Boolean value indicating whether the scalar may change when it undergoes case mapping.
- [var changesWhenLowercased: Bool](./properties-swift.struct/changeswhenlowercased.md)
  A Boolean value indicating whether the scalar’s normalized form differs from the `lowercaseMapping` of each constituent scalar.
- [var changesWhenNFKCCaseFolded: Bool](./properties-swift.struct/changeswhennfkccasefolded.md)
  A Boolean value indicating whether the scalar is one that is not identical to its NFKC case-fold mapping.
- [var changesWhenTitlecased: Bool](./properties-swift.struct/changeswhentitlecased.md)
  A Boolean value indicating whether the scalar’s normalized form differs from the `titlecaseMapping` of each constituent scalar.
- [var changesWhenUppercased: Bool](./properties-swift.struct/changeswhenuppercased.md)
  A Boolean value indicating whether the scalar’s normalized form differs from the `uppercaseMapping` of each constituent scalar.
- [var generalCategory: Unicode.GeneralCategory](./properties-swift.struct/generalcategory.md)
  The general category (most usual classification) of the scalar.
- [var isASCIIHexDigit: Bool](./properties-swift.struct/isasciihexdigit.md)
  A Boolean value indicating whether the scalar is an ASCII character commonly used for the representation of hexadecimal numbers.
- [var isAlphabetic: Bool](./properties-swift.struct/isalphabetic.md)
  A Boolean value indicating whether the scalar is alphabetic.
- [var isBidiControl: Bool](./properties-swift.struct/isbidicontrol.md)
  A Boolean value indicating whether the scalar is a format control character that has a specific function in the Unicode Bidirectional Algorithm.
- [var isBidiMirrored: Bool](./properties-swift.struct/isbidimirrored.md)
  A Boolean value indicating whether the scalar is mirrored in bidirectional text.
- [var isCaseIgnorable: Bool](./properties-swift.struct/iscaseignorable.md)
  A Boolean value indicating whether the scalar is ignored for casing purposes.
- [var isCased: Bool](./properties-swift.struct/iscased.md)
  A Boolean value indicating whether the scalar is considered to be either lowercase, uppercase, or titlecase.
- [var isDash: Bool](./properties-swift.struct/isdash.md)
  A Boolean value indicating whether the scalar is a punctuation symbol explicitly called out as a dash in the Unicode Standard or a compatibility equivalent.
- [var isDefaultIgnorableCodePoint: Bool](./properties-swift.struct/isdefaultignorablecodepoint.md)
  A Boolean value indicating whether the scalar is a default-ignorable code point.
- [var isDeprecated: Bool](./properties-swift.struct/isdeprecated.md)
  A Boolean value indicating whether the scalar is deprecated.
- [var isDiacritic: Bool](./properties-swift.struct/isdiacritic.md)
  A Boolean value indicating whether the scalar is a diacritic.
- [var isEmoji: Bool](./properties-swift.struct/isemoji.md)
  A Boolean value indicating whether the scalar has an emoji presentation, whether or not it is the default.
- [var isEmojiModifier: Bool](./properties-swift.struct/isemojimodifier.md)
  A Boolean value indicating whether the scalar is one that can modify a base emoji that precedes it.
- [var isEmojiModifierBase: Bool](./properties-swift.struct/isemojimodifierbase.md)
  A Boolean value indicating whether the scalar is one whose appearance can be changed by an emoji modifier that follows it.
- [var isEmojiPresentation: Bool](./properties-swift.struct/isemojipresentation.md)
  A Boolean value indicating whether the scalar is one that should be rendered with an emoji presentation, rather than a text presentation, by default.
- [var isExtender: Bool](./properties-swift.struct/isextender.md)
  A Boolean value indicating whether the scalar’s principal function is to extend the value or shape of a preceding alphabetic scalar.
- [var isFullCompositionExclusion: Bool](./properties-swift.struct/isfullcompositionexclusion.md)
  A Boolean value indicating whether the scalar is excluded from composition when performing Unicode normalization.
- [var isGraphemeBase: Bool](./properties-swift.struct/isgraphemebase.md)
  A Boolean value indicating whether the scalar is a grapheme base.
- [var isGraphemeExtend: Bool](./properties-swift.struct/isgraphemeextend.md)
  A Boolean value indicating whether the scalar is a grapheme extender.
- [var isHexDigit: Bool](./properties-swift.struct/ishexdigit.md)
  A Boolean value indicating whether the scalar is one that is commonly used for the representation of hexadecimal numbers or a compatibility equivalent.
- [var isIDContinue: Bool](./properties-swift.struct/isidcontinue.md)
  A Boolean value indicating whether the scalar is one which is recommended to be allowed to appear in a non-starting position in a programming language identifier.
- [var isIDSBinaryOperator: Bool](./properties-swift.struct/isidsbinaryoperator.md)
  A Boolean value indicating whether the scalar is an ideographic description character that determines how the two ideographic characters or ideographic description sequences that follow it are to be combined to form a single character.
- [var isIDSTrinaryOperator: Bool](./properties-swift.struct/isidstrinaryoperator.md)
  A Boolean value indicating whether the scalar is an ideographic description character that determines how the three ideographic characters or ideographic description sequences that follow it are to be combined to form a single character.
- [var isIDStart: Bool](./properties-swift.struct/isidstart.md)
  A Boolean value indicating whether the scalar is one which is recommended to be allowed to appear in a starting position in a programming language identifier.
- [var isIdeographic: Bool](./properties-swift.struct/isideographic.md)
  A Boolean value indicating whether the scalar is considered to be a CJKV (Chinese, Japanese, Korean, and Vietnamese) or other siniform (Chinese writing-related) ideograph.
- [var isJoinControl: Bool](./properties-swift.struct/isjoincontrol.md)
  A Boolean value indicating whether the scalar is a format control character that has a specific function in controlling cursive joining and ligation.
- [var isLogicalOrderException: Bool](./properties-swift.struct/islogicalorderexception.md)
  A Boolean value indicating whether the scalar requires special handling for operations involving ordering, such as sorting and searching.
- [var isLowercase: Bool](./properties-swift.struct/islowercase.md)
  A Boolean value indicating whether the scalar’s letterform is considered lowercase.
- [var isMath: Bool](./properties-swift.struct/ismath.md)
  A Boolean value indicating whether the scalar is one that naturally appears in mathematical contexts.
- [var isNoncharacterCodePoint: Bool](./properties-swift.struct/isnoncharactercodepoint.md)
  A Boolean value indicating whether the scalar is permanently reserved for internal use.
- [var isPatternSyntax: Bool](./properties-swift.struct/ispatternsyntax.md)
  A Boolean value indicating whether the scalar is recommended to have syntactic usage in patterns represented in source code.
- [var isPatternWhitespace: Bool](./properties-swift.struct/ispatternwhitespace.md)
  A Boolean value indicating whether the scalar is recommended to be treated as whitespace when parsing patterns represented in source code.
- [var isQuotationMark: Bool](./properties-swift.struct/isquotationmark.md)
  A Boolean value indicating whether the scalar is one that is used in writing to surround quoted text.
- [var isRadical: Bool](./properties-swift.struct/isradical.md)
  A Boolean value indicating whether the scalar is a radical component of CJK characters, Tangut characters, or Yi syllables.
- [var isSentenceTerminal: Bool](./properties-swift.struct/issentenceterminal.md)
  A Boolean value indicating whether the scalar is a punctuation mark that generally marks the end of a sentence.
- [var isSoftDotted: Bool](./properties-swift.struct/issoftdotted.md)
  A Boolean value indicating whether the scalar has a “soft dot” that disappears when a diacritic is placed over the scalar.
- [var isTerminalPunctuation: Bool](./properties-swift.struct/isterminalpunctuation.md)
  A Boolean value indicating whether the scalar is a punctuation symbol that typically marks the end of a textual unit.
- [var isUnifiedIdeograph: Bool](./properties-swift.struct/isunifiedideograph.md)
  A Boolean value indicating whether the scalar is one of the unified CJK ideographs in the Unicode Standard.
- [var isUppercase: Bool](./properties-swift.struct/isuppercase.md)
  A Boolean value indicating whether the scalar’s letterform is considered uppercase.
- [var isVariationSelector: Bool](./properties-swift.struct/isvariationselector.md)
  A Boolean value indicating whether the scalar is a variation selector.
- [var isWhitespace: Bool](./properties-swift.struct/iswhitespace.md)
  A Boolean value indicating whether the scalar is a whitespace character.
- [var isXIDContinue: Bool](./properties-swift.struct/isxidcontinue.md)
  A Boolean value indicating whether the scalar is one which is recommended to be allowed to appear in a non-starting position in a programming language identifier, with adjustments made for NFKC normalized form.
- [var isXIDStart: Bool](./properties-swift.struct/isxidstart.md)
  A Boolean value indicating whether the scalar is one which is recommended to be allowed to appear in a starting position in a programming language identifier, with adjustments made for NFKC normalized form.
- [var lowercaseMapping: String](./properties-swift.struct/lowercasemapping.md)
  The lowercase mapping of the scalar.
- [var name: String?](./properties-swift.struct/name.md)
  The published name of the scalar.
- [var nameAlias: String?](./properties-swift.struct/namealias.md)
  The normative formal alias of the scalar.
- [var numericType: Unicode.NumericType?](./properties-swift.struct/numerictype.md)
  The numeric type of the scalar.
- [var numericValue: Double?](./properties-swift.struct/numericvalue.md)
  The numeric value of the scalar.
- [var titlecaseMapping: String](./properties-swift.struct/titlecasemapping.md)
  The titlecase mapping of the scalar.
- [var uppercaseMapping: String](./properties-swift.struct/uppercasemapping.md)
  The uppercase mapping of the scalar.

## Relationships

### Conforms To
- [Sendable](../../sendable.md)
- [SendableMetatype](../../sendablemetatype.md)

## See Also

### Inspecting a Scalar
- [var value: UInt32](./value.md)
  A numeric representation of the Unicode scalar.
- [var properties: Unicode.Scalar.Properties](./properties-swift.property.md)
  Properties of this scalar defined by the Unicode standard.
- [func hash(into: inout Hasher)](./hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var isASCII: Bool](./isascii.md)
  A Boolean value indicating whether the Unicode scalar is an ASCII character.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct)*