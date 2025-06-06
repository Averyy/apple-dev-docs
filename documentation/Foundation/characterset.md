# CharacterSet

**Framework**: Foundation  
**Kind**: struct

A set of Unicode character values for use in search operations.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CharacterSet
```

#### Overview

A `CharacterSet` represents a set of Unicode-compliant characters. Foundation types use `CharacterSet` to group characters together for searching operations, so that they can find any of a particular set of characters during a search.

This type provides “copy-on-write” behavior, and is also bridged to the Objective-C `NSCharacterSet` class.

## Topics

### Getting Standard Character Sets
- [static var alphanumerics: CharacterSet](characterset/alphanumerics.md)
  Returns a character set containing the characters in Unicode General Categories L*, M*, and N*.
- [static var capitalizedLetters: CharacterSet](characterset/capitalizedletters.md)
  Returns a character set containing the characters in Unicode General Category Lt.
- [static var controlCharacters: CharacterSet](characterset/controlcharacters.md)
  Returns a character set containing the characters in Unicode General Category Cc and Cf.
- [static var decimalDigits: CharacterSet](characterset/decimaldigits.md)
  Returns a character set containing the characters in the category of Decimal Numbers.
- [static var decomposables: CharacterSet](characterset/decomposables.md)
  Returns a character set containing individual Unicode characters that can also be represented as composed character sequences (such as for letters with accents), by the definition of “standard decomposition” in version 3.2 of the Unicode character encoding standard.
- [static var illegalCharacters: CharacterSet](characterset/illegalcharacters.md)
  Returns a character set containing values in the category of Non-Characters or that have not yet been defined in version 3.2 of the Unicode standard.
- [static var letters: CharacterSet](characterset/letters.md)
  Returns a character set containing the characters in Unicode General Category L* & M*.
- [static var lowercaseLetters: CharacterSet](characterset/lowercaseletters.md)
  Returns a character set containing the characters in Unicode General Category Ll.
- [static var newlines: CharacterSet](characterset/newlines.md)
  Returns a character set containing the newline characters (`U+000A ~ U+000D`, `U+0085`, `U+2028`, and `U+2029`).
- [static var nonBaseCharacters: CharacterSet](characterset/nonbasecharacters.md)
  Returns a character set containing the characters in Unicode General Category M*.
- [static var punctuationCharacters: CharacterSet](characterset/punctuationcharacters.md)
  Returns a character set containing the characters in Unicode General Category P*.
- [static var symbols: CharacterSet](characterset/symbols.md)
  Returns a character set containing the characters in Unicode General Category S*.
- [static var uppercaseLetters: CharacterSet](characterset/uppercaseletters.md)
  Returns a character set containing the characters in Unicode General Category Lu and Lt.
- [static var whitespaces: CharacterSet](characterset/whitespaces.md)
  Returns a character set containing the characters in Unicode General Category Zs and `CHARACTER TABULATION (U+0009)`.
- [static var whitespacesAndNewlines: CharacterSet](characterset/whitespacesandnewlines.md)
  Returns a character set containing characters in Unicode General Category Z*, `U+000A ~ U+000D`, and `U+0085`.
### Getting Character Sets for URL Encoding
- [static var urlFragmentAllowed: CharacterSet](characterset/urlfragmentallowed.md)
  Returns the character set for characters allowed in a fragment URL component.
- [static var urlHostAllowed: CharacterSet](characterset/urlhostallowed.md)
  Returns the character set for characters allowed in a host URL subcomponent.
- [static var urlPasswordAllowed: CharacterSet](characterset/urlpasswordallowed.md)
  Returns the character set for characters allowed in a password URL subcomponent.
- [static var urlPathAllowed: CharacterSet](characterset/urlpathallowed.md)
  Returns the character set for characters allowed in a path URL component.
- [static var urlQueryAllowed: CharacterSet](characterset/urlqueryallowed.md)
  Returns the character set for characters allowed in a query URL component.
- [static var urlUserAllowed: CharacterSet](characterset/urluserallowed.md)
  Returns the character set for characters allowed in a user URL subcomponent.
### Creating a Custom Character Set
- [init()](characterset/init.md)
  Initialize an empty instance.
### Creating and Managing Bitmap Representations
- [var bitmapRepresentation: Data](characterset/bitmaprepresentation.md)
  Returns a representation of the `CharacterSet` in binary format.
### Inverting a Character Set
- [func invert()](characterset/invert.md)
  Invert the contents of the `CharacterSet`.
- [var inverted: CharacterSet](characterset/inverted.md)
  Returns an inverted copy of the receiver.
### Combining Character Sets
- [func formIntersection(CharacterSet)](characterset/formintersection(_:).md)
  Sets the value to an intersection of the `CharacterSet` with another `CharacterSet`.
- [func formSymmetricDifference(CharacterSet)](characterset/formsymmetricdifference(_:).md)
  Sets the value to an exclusive or of the `CharacterSet` with another `CharacterSet`.
- [func formUnion(CharacterSet)](characterset/formunion(_:).md)
  Sets the value to a union of the `CharacterSet` with another `CharacterSet`.
- [func hasMember(inPlane: UInt8) -> Bool](characterset/hasmember(inplane:).md)
  Returns true if the `CharacterSet` has a member in the specified plane.
- [func insert(charactersIn: String)](characterset/insert(charactersin:)-2syuj.md)
  Insert the values from the specified string into the `CharacterSet`.
- [func intersection(CharacterSet) -> CharacterSet](characterset/intersection(_:).md)
  Returns an intersection of the `CharacterSet` with another `CharacterSet`.
- [func invert()](characterset/invert.md)
  Invert the contents of the `CharacterSet`.
- [func isSuperset(of: CharacterSet) -> Bool](characterset/issuperset(of:).md)
  Returns true if `self` is a superset of `other`.
- [func remove(charactersIn: String)](characterset/remove(charactersin:)-3sayw.md)
  Remove the values from the specified string from the `CharacterSet`.
- [func subtracting(CharacterSet) -> CharacterSet](characterset/subtracting(_:).md)
  Returns a `CharacterSet` created by removing elements in `other` from `self`.
- [func symmetricDifference(CharacterSet) -> CharacterSet](characterset/symmetricdifference(_:).md)
  Returns an exclusive or of the `CharacterSet` with another `CharacterSet`.
- [func union(CharacterSet) -> CharacterSet](characterset/union(_:).md)
  Returns a union of the `CharacterSet` with another `CharacterSet`.
### Adding Characters
- [func insert(charactersIn: String)](characterset/insert(charactersin:)-2syuj.md)
  Insert the values from the specified string into the `CharacterSet`.
### Removing Characters
- [func remove(charactersIn: String)](characterset/remove(charactersin:)-3sayw.md)
  Remove the values from the specified string from the `CharacterSet`.
- [func subtracting(CharacterSet) -> CharacterSet](characterset/subtracting(_:).md)
  Returns a `CharacterSet` created by removing elements in `other` from `self`.
### Testing Set Membership
- [func hasMember(inPlane: UInt8) -> Bool](characterset/hasmember(inplane:).md)
  Returns true if the `CharacterSet` has a member in the specified plane.
- [func isSuperset(of: CharacterSet) -> Bool](characterset/issuperset(of:).md)
  Returns true if `self` is a superset of `other`.
### Comparing Character Sets
- [static func == (CharacterSet, CharacterSet) -> Bool](characterset/==(_:_:).md)
  Returns true if the two `CharacterSet`s are equal.
### Using Reference Types
- [class NSCharacterSet](nscharacterset.md)
  An object representing a fixed set of Unicode character values for use in search operations.
- [class NSMutableCharacterSet](nsmutablecharacterset.md)
  An object representing a mutable set of Unicode character values for use in search operations.
### Initializers
- [init(bitmapRepresentation: Data)](characterset/init(bitmaprepresentation:).md)
- [init(charactersIn: ClosedRange<Unicode.Scalar>)](characterset/init(charactersin:)-87iva.md)
- [init(charactersIn: String)](characterset/init(charactersin:)-87m2b.md)
- [init(charactersIn: Range<Unicode.Scalar>)](characterset/init(charactersin:)-8tcll.md)
- [init?(contentsOfFile: String)](characterset/init(contentsoffile:).md)
### Instance Methods
- [func contains(Unicode.Scalar) -> Bool](characterset/contains(_:).md)
- [func insert(Unicode.Scalar) -> (inserted: Bool, memberAfterInsert: Unicode.Scalar)](characterset/insert(_:).md)
- [func insert(charactersIn: Range<Unicode.Scalar>)](characterset/insert(charactersin:)-7urdg.md)
- [func insert(charactersIn: ClosedRange<Unicode.Scalar>)](characterset/insert(charactersin:)-803uz.md)
- [func remove(Unicode.Scalar) -> Unicode.Scalar?](characterset/remove(_:).md)
- [func remove(charactersIn: ClosedRange<Unicode.Scalar>)](characterset/remove(charactersin:)-1kqte.md)
- [func remove(charactersIn: Range<Unicode.Scalar>)](characterset/remove(charactersin:)-5td97.md)
- [func subtract(CharacterSet)](characterset/subtract(_:).md)
- [func update(with: Unicode.Scalar) -> Unicode.Scalar?](characterset/update(with:).md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [ReferenceConvertible](referenceconvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [typealias UnicodeScalar = Unicode.Scalar](../Swift/UnicodeScalar.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/characterset)*