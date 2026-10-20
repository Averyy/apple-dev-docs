# alphanumeric()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a character set containing the characters in Unicode General Categories L*, M*, and N*.

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
class func alphanumeric() -> NSMutableCharacterSet
```

```objc
+ (NSMutableCharacterSet *) alphanumericCharacterSet;
```

## See Also

### Getting Standard Character Sets
- [class func capitalizedLetter() -> NSMutableCharacterSet](./capitalizedletter%28%29.md)
  Returns a character set containing the characters in Unicode General Category Lt.
- [class func control() -> NSMutableCharacterSet](./control%28%29.md)
  Returns a character set containing the characters in Unicode General Category Cc and Cf.
- [class func decimalDigit() -> NSMutableCharacterSet](./decimaldigit%28%29.md)
  Returns a character set containing the characters in the category of decimal numbers.
- [class func decomposable() -> NSMutableCharacterSet](./decomposable%28%29.md)
  Returns a character set containing individual Unicode characters that can also be represented as composed character sequences (such as for letters with accents), by the definition of “standard decomposition” in version 3.2 of the Unicode character encoding standard.
- [class func illegal() -> NSMutableCharacterSet](./illegal%28%29.md)
  Returns a character set containing values in the category of Non-Characters or that have not yet been defined in version 3.2 of the Unicode standard.
- [class func letter() -> NSMutableCharacterSet](./letter%28%29.md)
  Returns a character set containing the characters in Unicode General Category L* & M*.
- [class func lowercaseLetter() -> NSMutableCharacterSet](./lowercaseletter%28%29.md)
  Returns a character set containing the characters in Unicode General Category Ll.
- [class func newline() -> NSMutableCharacterSet](./newline%28%29.md)
  Returns a character set containing the newline characters (`U+000A` ~ `U+000D`, `U+0085`, `U+2028`, and `U+2029`).
- [class func nonBase() -> NSMutableCharacterSet](./nonbase%28%29.md)
  Returns a character set containing the characters in Unicode General Category M*.
- [class func punctuation() -> NSMutableCharacterSet](./punctuation%28%29.md)
  Returns a character set containing the characters in Unicode General Category P*.
- [class func symbol() -> NSMutableCharacterSet](./symbol%28%29.md)
  Returns a character set containing the characters in Unicode General Category S*.
- [class func uppercaseLetter() -> NSMutableCharacterSet](./uppercaseletter%28%29.md)
  Returns a character set containing the characters in Unicode General Category Lu and Lt.
- [class func whitespaceAndNewline() -> NSMutableCharacterSet](./whitespaceandnewline%28%29.md)
  Returns a character set containing characters in Unicode General Category Z*, `U+000A` ~ `U+000D`, and `U+0085`.
- [class func whitespace() -> NSMutableCharacterSet](./whitespace%28%29.md)
  Returns a character set containing the characters in Unicode General Category Zs and `CHARACTER TABULATION` (`U+0009`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablecharacterset/alphanumeric())*