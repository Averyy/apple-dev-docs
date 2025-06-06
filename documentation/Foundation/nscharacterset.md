# NSCharacterSet

**Framework**: Foundation  
**Kind**: class

An object representing a fixed set of Unicode character values for use in search operations.

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
class NSCharacterSet
```

#### Overview

In Swift, this bridges to a [`CharacterSet`](characterset.md); use [`NSCharacterSet`](nscharacterset.md) when you need reference semantics or other Foundation-specific behavior.

An `NSCharacterSet` object represents a set of Unicode-compliant characters. `NSString` and `NSScanner` objects use `NSCharacterSet` objects to group characters together for searching operations, so that they can find any of a particular set of characters during a search. The cluster’s two public classes, `NSCharacterSet` and [`NSMutableCharacterSet`](nsmutablecharacterset.md), declare the programmatic interface for static and dynamic character sets, respectively.

The objects you create using these classes are referred to as character set objects (and when no confusion will result, merely as character sets). Because of the nature of class clusters, character set objects aren’t actual instances of the `NSCharacterSet` or `NSMutableCharacterSet` classes but of one of their private subclasses. Although a character set object’s class is private, its interface is public, as declared by these abstract superclasses, `NSCharacterSet` and `NSMutableCharacterSet`. The character set classes adopt the `NSCopying` and `NSMutableCopying` protocols, making it convenient to convert a character set of one type to the other.

The `NSCharacterSet` class declares the programmatic interface for an object that manages a set of Unicode characters (see the [`NSString`](nsstring.md) class cluster specification for information on Unicode). `NSCharacterSet`’s principal primitive method, [`characterIsMember(_:)`](nscharacterset/characterismember(_:).md), provides the basis for all other instance methods in its interface. A subclass of `NSCharacterSet` needs only to implement this method, plus [`mutableCopy(with:)`](nsmutablecopying/mutablecopy(with:).md), for proper behavior. For optimal performance, a subclass should also override [`bitmapRepresentation`](nscharacterset/bitmaprepresentation.md), which otherwise works by invoking [`characterIsMember(_:)`](nscharacterset/characterismember(_:).md) for every possible Unicode value.

`NSCharacterSet` is “toll-free bridged” with its Core Foundation counterpart, [`CFCharacterSet`](https://developer.apple.com/documentation/CoreFoundation/CFCharacterSet). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

> ❗ **Important**:  The Swift overlay to the Foundation framework provides the [`CharacterSet`](characterset.md) structure, which bridges to the [`NSCharacterSet`](nscharacterset.md) class and its mutable subclass, [`NSMutableCharacterSet`](nsmutablecharacterset.md). For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

 The Swift overlay to the Foundation framework provides the [`CharacterSet`](characterset.md) structure, which bridges to the [`NSCharacterSet`](nscharacterset.md) class and its mutable subclass, [`NSMutableCharacterSet`](nsmutablecharacterset.md). For more information about value types, see [`Working with Cocoa Frameworks`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/WorkingWithCocoaDataTypes.html#//apple_ref/doc/uid/TP40014216-CH6) in [`Using Swift with Cocoa and Objective-C (Swift 4.1)`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Swift/Conceptual/BuildingCocoaApps/index.html#//apple_ref/doc/uid/TP40014216).

## Topics

### Getting Standard Character Sets
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
- [class var whitespaces: CharacterSet](nscharacterset/whitespaces.md)
  A character set containing the characters in Unicode General Category Zs and `CHARACTER TABULATION` (`U+0009`).
### Getting Character Sets for URL Encoding
- [class var urlFragmentAllowed: CharacterSet](nscharacterset/urlfragmentallowed.md)
  Returns the character set for characters allowed in a fragment URL component.
- [class var urlHostAllowed: CharacterSet](nscharacterset/urlhostallowed.md)
  Returns the character set for characters allowed in a host URL subcomponent.
- [class var urlPasswordAllowed: CharacterSet](nscharacterset/urlpasswordallowed.md)
  Returns the character set for characters allowed in a password URL subcomponent.
- [class var urlPathAllowed: CharacterSet](nscharacterset/urlpathallowed.md)
  Returns the character set for characters allowed in a path URL component.
- [class var urlQueryAllowed: CharacterSet](nscharacterset/urlqueryallowed.md)
  Returns the character set for characters allowed in a query URL component.
- [class var urlUserAllowed: CharacterSet](nscharacterset/urluserallowed.md)
  Returns the character set for characters allowed in a user URL subcomponent.
### Creating a Custom Character Set
- [init(coder: NSCoder)](nscharacterset/init(coder:).md)
- [init(charactersIn: String)](nscharacterset/init(charactersin:).md)
  Returns a character set containing the characters in a given string.
- [init(range: NSRange)](nscharacterset/init(range:).md)
  Returns a character set containing characters with Unicode values in a given range.
- [NSOpenStepUnicodeReservedBase](1560803-nsopenstepunicodereservedbase.md)
  Specifies lower bound for a Unicode character range reserved for Apple’s corporate use.
### Creating and Managing Character Sets as Bitmap Representations
- [init(bitmapRepresentation: Data)](nscharacterset/init(bitmaprepresentation:).md)
  Returns a character set containing characters determined by a given bitmap representation.
- [init?(contentsOfFile: String)](nscharacterset/init(contentsoffile:).md)
  Returns a character set read from the bitmap representation stored in the file a given path.
- [var bitmapRepresentation: Data](nscharacterset/bitmaprepresentation.md)
  An `NSData` object encoding the receiver in binary format.
### Inverting a Character Set
- [var inverted: CharacterSet](nscharacterset/inverted.md)
  A character set containing only characters that don’t exist in the receiver.
### Testing Set Membership
- [func characterIsMember(unichar) -> Bool](nscharacterset/characterismember(_:).md)
  Returns a Boolean value that indicates whether a given character is in the receiver.
- [func hasMemberInPlane(UInt8) -> Bool](nscharacterset/hasmemberinplane(_:).md)
  Returns a Boolean value that indicates whether the receiver has at least one member in a given character plane.
- [func isSuperset(of: CharacterSet) -> Bool](nscharacterset/issuperset(of:).md)
  Returns a Boolean value that indicates whether the receiver is a superset of another given character set.
- [func longCharacterIsMember(UTF32Char) -> Bool](nscharacterset/longcharacterismember(_:).md)
  Returns a Boolean value that indicates whether a given long character is a member of the receiver.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSMutableCharacterSet](nsmutablecharacterset.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSMutableCopying](nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset)*