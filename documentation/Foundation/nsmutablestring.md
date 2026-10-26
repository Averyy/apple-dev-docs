# NSMutableString

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSMutableString : NSString
```

#### Overview

In Swift, you can use this type instead of a [`String`](../Swift/string.md) in cases that require reference semantics.

The `NSMutableString` class declares the programmatic interface to an object that manages a mutable string—that is, a string whose contents can be edited—that conceptually represents an array of Unicode characters. To construct and manage an immutable string—or a string that cannot be changed after it has been created—use an object of the [`NSString`](./nsstring.md) class.

The `NSMutableString` class adds one primitive method—[`replaceCharacters(in:with:)`](./nsmutablestring/replacecharacters%28in,with%29.md)—to the basic string-handling behavior inherited from `NSString`. All other methods that modify a string work through this method. For example, [`insert(_:at:)`](./nsmutablestring/insert%28_,at%29.md) simply replaces the characters in a range of `0` length, while [`deleteCharacters(in:)`](./nsmutablestring/deletecharacters%28in%29.md) replaces the characters in a given range with no characters.

NSMutableString is “toll-free bridged” with its Core Foundation counterpart, [`CFMutableString`](../CoreFoundation/cfmutablestring.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

## Topics

### Creating and Initializing a Mutable String
- [init(capacity: Int)](./nsmutablestring/init%28capacity%29.md)
  Returns an `NSMutableString` object initialized with initial storage for a given number of characters,
- [+ stringWithCapacity:](./nsmutablestring/stringwithcapacity_.md)
  Returns an empty `NSMutableString` object with initial storage for a given number of characters.
### Modifying a String
- [func append(String)](./nsmutablestring/append%28_%29.md)
  Adds to the end of the receiver the characters of a given string.
- [func applyTransform(StringTransform, reverse: Bool, range: NSRange, updatedRange: NSRangePointer?) -> Bool](./nsmutablestring/applytransform%28_,reverse,range,updatedrange%29.md)
  Transliterates the receiver by applying a specified ICU string transform.
- [func deleteCharacters(in: NSRange)](./nsmutablestring/deletecharacters%28in%29.md)
  Removes from the receiver the characters in a given range.
- [func insert(String, at: Int)](./nsmutablestring/insert%28_,at%29.md)
  Inserts into the receiver the characters of a given string at a given location.
- [func replaceCharacters(in: NSRange, with: String)](./nsmutablestring/replacecharacters%28in,with%29.md)
  Replaces the characters from `range` with those in `aString`.
- [func replaceOccurrences(of: String, with: String, options: NSString.CompareOptions, range: NSRange) -> Int](./nsmutablestring/replaceoccurrences%28of,with,options,range%29.md)
  Replaces all occurrences of a given string in a given range with another given string, returning the number of replacements.
- [func setString(String)](./nsmutablestring/setstring%28_%29.md)
  Replaces the characters of the receiver with those in a given string.
- [- appendFormat:](./nsmutablestring/appendformat_.md)
  Adds a constructed string to the receiver.
### Constants
- [String Transformations](./string-transformations.md)
  These constants specify transforms used by the [`applyTransform(_:reverse:range:updatedRange:)`](./nsmutablestring/applytransform%28_,reverse,range,updatedrange%29.md) method.
### Instance Methods
- [func appendFormat(NSString, any CVarArg...)](./nsmutablestring/appendformat%28_,_%29.md)

## Relationships

### Inherits From
- [NSString](./nsstring.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSItemProviderReading](./nsitemproviderreading.md)
- [NSItemProviderWriting](./nsitemproviderwriting.md)
- [NSMutableCopying](./nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Strings
- [NSString](./nsstring.md)
  A static, plain-text Unicode string object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablestring)*