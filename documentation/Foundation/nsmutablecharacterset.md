# NSMutableCharacterSet

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object representing a mutable set of Unicode character values for use in search operations.

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
class NSMutableCharacterSet
```

```objc
@interface NSMutableCharacterSet : NSCharacterSet
```

## Overview

In Swift, this object bridges to [`CharacterSet`](./characterset.md); use [`NSMutableCharacterSet`](./nsmutablecharacterset.md) when you need reference semantics or other Foundation-specific behavior.

The `NSMutableCharacterSet` class declares the programmatic interface to objects that manage a modifiable set of Unicode characters. You can add or remove characters from a mutable character set as numeric values in `NSRange` structures or as character values in strings, combine character sets by union or intersection, and invert a character set.

Mutable character sets are less efficient to use than immutable character sets. If you don’t need to change a character set after creating it, create an immutable copy with `copy` and use that.

`NSMutableCharacterSet` defines no primitive methods. Subclasses must implement all methods declared by this class in addition to the primitives of [`NSCharacterSet`](./nscharacterset.md). They must also implement [`mutableCopy(with:)`](./nsmutablecopying/mutablecopy%28with%29.md).

`NSMutableCharacterSet` is “toll-free bridged” with its Core Foundation counterpart, [`CFMutableCharacterSet`](../CoreFoundation/cfmutablecharacterset.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`CharacterSet`](./characterset.md) structure, which bridges to the [`NSMutableCharacterSet`](./nsmutablecharacterset.md) class and its immutable superclass, [`NSCharacterSet`](./nscharacterset.md).  For more information about value types, see [Working with Foundation Types](../Swift/working-with-foundation-types.md).

## Topics

### Getting Standard Character Sets
- [class func alphanumeric() -> NSMutableCharacterSet](./nsmutablecharacterset/alphanumeric%28%29.md)
  Returns a character set containing the characters in Unicode General Categories L*, M*, and N*.
- [class func capitalizedLetter() -> NSMutableCharacterSet](./nsmutablecharacterset/capitalizedletter%28%29.md)
  Returns a character set containing the characters in Unicode General Category Lt.
- [class func control() -> NSMutableCharacterSet](./nsmutablecharacterset/control%28%29.md)
  Returns a character set containing the characters in Unicode General Category Cc and Cf.
- [class func decimalDigit() -> NSMutableCharacterSet](./nsmutablecharacterset/decimaldigit%28%29.md)
  Returns a character set containing the characters in the category of decimal numbers.
- [class func decomposable() -> NSMutableCharacterSet](./nsmutablecharacterset/decomposable%28%29.md)
  Returns a character set containing individual Unicode characters that can also be represented as composed character sequences (such as for letters with accents), by the definition of “standard decomposition” in version 3.2 of the Unicode character encoding standard.
- [class func illegal() -> NSMutableCharacterSet](./nsmutablecharacterset/illegal%28%29.md)
  Returns a character set containing values in the category of Non-Characters or that have not yet been defined in version 3.2 of the Unicode standard.
- [class func letter() -> NSMutableCharacterSet](./nsmutablecharacterset/letter%28%29.md)
  Returns a character set containing the characters in Unicode General Category L* & M*.
- [class func lowercaseLetter() -> NSMutableCharacterSet](./nsmutablecharacterset/lowercaseletter%28%29.md)
  Returns a character set containing the characters in Unicode General Category Ll.
- [class func newline() -> NSMutableCharacterSet](./nsmutablecharacterset/newline%28%29.md)
  Returns a character set containing the newline characters (`U+000A` ~ `U+000D`, `U+0085`, `U+2028`, and `U+2029`).
- [class func nonBase() -> NSMutableCharacterSet](./nsmutablecharacterset/nonbase%28%29.md)
  Returns a character set containing the characters in Unicode General Category M*.
- [class func punctuation() -> NSMutableCharacterSet](./nsmutablecharacterset/punctuation%28%29.md)
  Returns a character set containing the characters in Unicode General Category P*.
- [class func symbol() -> NSMutableCharacterSet](./nsmutablecharacterset/symbol%28%29.md)
  Returns a character set containing the characters in Unicode General Category S*.
- [class func uppercaseLetter() -> NSMutableCharacterSet](./nsmutablecharacterset/uppercaseletter%28%29.md)
  Returns a character set containing the characters in Unicode General Category Lu and Lt.
- [class func whitespaceAndNewline() -> NSMutableCharacterSet](./nsmutablecharacterset/whitespaceandnewline%28%29.md)
  Returns a character set containing characters in Unicode General Category Z*, `U+000A` ~ `U+000D`, and `U+0085`.
- [class func whitespace() -> NSMutableCharacterSet](./nsmutablecharacterset/whitespace%28%29.md)
  Returns a character set containing the characters in Unicode General Category Zs and `CHARACTER TABULATION` (`U+0009`).
### Creating Custom Character Sets
- [init(charactersIn: String)](./nsmutablecharacterset/init%28charactersin%29.md)
  Returns a character set containing the characters in a given string.
- [init(range: NSRange)](./nsmutablecharacterset/init%28range%29.md)
  Returns a character set containing characters with Unicode values in a given range.
- [init(bitmapRepresentation: Data)](./nsmutablecharacterset/init%28bitmaprepresentation%29.md)
  Returns a character set containing characters determined by a given bitmap representation.
- [init?(contentsOfFile: String)](./nsmutablecharacterset/init%28contentsoffile%29.md)
  Returns a character set read from the bitmap representation stored in the file a given path.
### Adding and Removing Characters
- [func addCharacters(in: NSRange)](./nsmutablecharacterset/addcharacters%28in%29-4ppyw.md)
  Adds to the receiver the characters whose Unicode values are in a given range.
- [func removeCharacters(in: NSRange)](./nsmutablecharacterset/removecharacters%28in%29-70nqp.md)
  Removes from the receiver the characters whose Unicode values are in a given range.
- [func addCharacters(in: String)](./nsmutablecharacterset/addcharacters%28in%29-7q02.md)
  Adds to the receiver the characters in a given string.
- [func removeCharacters(in: String)](./nsmutablecharacterset/removecharacters%28in%29-762gt.md)
  Removes from the receiver the characters in a given string.
### Combining Character Sets
- [func formIntersection(with: CharacterSet)](./nsmutablecharacterset/formintersection%28with%29.md)
  Modifies the receiver so it contains only characters that exist in both the receiver and another set.
- [func formUnion(with: CharacterSet)](./nsmutablecharacterset/formunion%28with%29.md)
  Modifies the receiver so it contains all characters that exist in either the receiver or another set.
### Inverting a Character Set
- [func invert()](./nsmutablecharacterset/invert%28%29.md)
  Replaces all the characters in the receiver with all the characters it didn’t previously contain.

## Relationships

### Inherits From
- [NSCharacterSet](./nscharacterset.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSMutableCopying](./nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Characters
- [NSCharacterSet](./nscharacterset.md)
  An object representing a fixed set of Unicode character values for use in search operations.
- [unichar](./unichar.md)
  Type for UTF-16 code units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablecharacterset)*