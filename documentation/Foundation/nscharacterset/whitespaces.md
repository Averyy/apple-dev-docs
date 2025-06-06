# whitespaces

**Framework**: Foundation  
**Kind**: property

A character set containing the characters in Unicode General Category Zs and `CHARACTER TABULATION` (`U+0009`).

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var whitespaces: CharacterSet { get }
```

#### Return Value

A character set containing all the whitespace characters.

#### Discussion

This set doesn’t contain the newline or carriage return characters.

## See Also

- [class var alphanumerics: CharacterSet](nscharacterset/alphanumerics.md)
  A character set containing the characters in Unicode General Categories L*, M*, and N*.
- [class var capitalizedLetters: CharacterSet](nscharacterset/capitalizedletters.md)
  A character set containing the characters in Unicode General Category Lt.
- [class var controlCharacters: CharacterSet](nscharacterset/controlcharacters.md)
  A character set containing the characters in Unicode General Category Cc and Cf.
- [class var decimalDigits: CharacterSet](nscharacterset/decimaldigits.md)
  A character set containing the characters in the category of Decimal Numbers.
- [class var decomposables: CharacterSet](nscharacterset/decomposables.md)
  A character set containing individual Unicode characters that can also be represented as composed character sequences (such as for letters with accents), by the definition of “standard decomposition” in version 3.2 of the Unicode character encoding standard.
- [class var illegalCharacters: CharacterSet](nscharacterset/illegalcharacters.md)
  A character set containing values in the category of Non-Characters or that have not yet been defined in version 3.2 of the Unicode standard.
- [class var letters: CharacterSet](nscharacterset/letters.md)
  A character set containing the characters in Unicode General Category L* & M*.
- [class var lowercaseLetters: CharacterSet](nscharacterset/lowercaseletters.md)
  A character set containing the characters in Unicode General Category Ll.
- [class var newlines: CharacterSet](nscharacterset/newlines.md)
  A character set containing the newline characters (`U+000A` ~ `U+000D`, `U+0085`, `U+2028`, and `U+2029`).
- [class var nonBaseCharacters: CharacterSet](nscharacterset/nonbasecharacters.md)
  A character set containing the characters in Unicode General Category M*.
- [class var punctuationCharacters: CharacterSet](nscharacterset/punctuationcharacters.md)
  A character set containing the characters in Unicode General Category P*.
- [class var symbols: CharacterSet](nscharacterset/symbols.md)
  A character set containing the characters in Unicode General Category S*.
- [class var uppercaseLetters: CharacterSet](nscharacterset/uppercaseletters.md)
  A character set containing the characters in Unicode General Category Lu and Lt.
- [class var whitespacesAndNewlines: CharacterSet](nscharacterset/whitespacesandnewlines.md)
  A character set containing characters in Unicode General Category Z*, `U+000A` ~ `U+000D`, and `U+0085`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/whitespaces)*