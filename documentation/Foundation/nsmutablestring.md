# NSMutableString

**Framework**: Foundation  
**Kind**: class

A dynamic plain-text Unicode string object.

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
class NSMutableString
```

#### Overview

In Swift, you can use this type instead of a [`String`](https://developer.apple.com/documentation/Swift/String) in cases that require reference semantics.

The `NSMutableString` class declares the programmatic interface to an object that manages a mutable string—that is, a string whose contents can be edited—that conceptually represents an array of Unicode characters. To construct and manage an immutable string—or a string that cannot be changed after it has been created—use an object of the [`NSString`](nsstring.md) class.

The `NSMutableString` class adds one primitive method—[`replaceCharacters(in:with:)`](nsmutablestring/replacecharacters(in:with:).md)—to the basic string-handling behavior inherited from `NSString`. All other methods that modify a string work through this method. For example, [`insert(_:at:)`](nsmutablestring/insert(_:at:).md) simply replaces the characters in a range of `0` length, while [`deleteCharacters(in:)`](nsmutablestring/deletecharacters(in:).md) replaces the characters in a given range with no characters.

NSMutableString is “toll-free bridged” with its Core Foundation counterpart, [`CFMutableString`](https://developer.apple.com/documentation/CoreFoundation/CFMutableString). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

## Topics

### Creating and Initializing a Mutable String
- [init(capacity: Int)](nsmutablestring/init(capacity:).md)
  Returns an `NSMutableString` object initialized with initial storage for a given number of characters,
### Modifying a String
- [func append(String)](nsmutablestring/append(_:).md)
  Adds to the end of the receiver the characters of a given string.
- [func applyTransform(StringTransform, reverse: Bool, range: NSRange, updatedRange: NSRangePointer?) -> Bool](nsmutablestring/applytransform(_:reverse:range:updatedrange:).md)
  Transliterates the receiver by applying a specified ICU string transform.
- [func deleteCharacters(in: NSRange)](nsmutablestring/deletecharacters(in:).md)
  Removes from the receiver the characters in a given range.
- [func insert(String, at: Int)](nsmutablestring/insert(_:at:).md)
  Inserts into the receiver the characters of a given string at a given location.
- [func replaceCharacters(in: NSRange, with: String)](nsmutablestring/replacecharacters(in:with:).md)
  Replaces the characters from `range` with those in `aString`.
- [func replaceOccurrences(of: String, with: String, options: NSString.CompareOptions, range: NSRange) -> Int](nsmutablestring/replaceoccurrences(of:with:options:range:).md)
  Replaces all occurrences of a given string in a given range with another given string, returning the number of replacements.
- [func setString(String)](nsmutablestring/setstring(_:).md)
  Replaces the characters of the receiver with those in a given string.
### Constants
- [String Transformations](string-transformations.md)
  These constants specify transforms used by the [`applyTransform(_:reverse:range:updatedRange:)`](nsmutablestring/applytransform(_:reverse:range:updatedrange:).md) method.
### Instance Methods
- [func appendFormat(NSString, any CVarArg...)](nsmutablestring/appendformat(_:_:).md)

## Relationships

### Inherits From
- [NSString](nsstring.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSItemProviderReading](nsitemproviderreading.md)
- [NSItemProviderWriting](nsitemproviderwriting.md)
- [NSMutableCopying](nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablestring)*