# NSString

**Framework**: Foundation  
**Kind**: class

A static, plain-text Unicode string object.

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
class NSString
```

## Mentions

- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)

#### Overview

You can use this type in Swift when you need reference semantics or other Foundation-specific behavior.

The [`NSString`](nsstring.md) class and its mutable subclass, [`NSMutableString`](nsmutablestring.md), provide an extensive set of APIs for working with strings, including methods for comparing, searching, and modifying strings. [`NSString`](nsstring.md) objects are used throughout Foundation and other Cocoa frameworks, serving as the basis for all textual and linguistic functionality on the platform.

[`NSString`](nsstring.md) is  with its Core Foundation counterpart, [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString). See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

##### String Objects

An [`NSString`](nsstring.md) object encodes a Unicode-compliant text string, represented as a sequence of UTF–16 code units. All lengths, character indexes, and ranges are expressed in terms of 16-bit platform-endian values, with index values starting at `0`.

An [`NSString`](nsstring.md) object can be initialized from or written to a C buffer, an [`NSData`](nsdata.md) object, or the contents of an [`NSURL`](nsurl.md). It can also be encoded and decoded to and from ASCII, UTF–8, UTF–16, UTF–32, or any other string encoding represented by [`NSStringEncoding`](nsstringencoding.md).

> **Note**:  An immutable string is a text string that is defined when it is created and subsequently cannot be changed. An immutable string is implemented as an array of UTF–16 code units (in other words, a text string). To create and manage an immutable string, use the [`NSString`](nsstring.md) class. To construct and manage a string that can be changed after it has been created, use [`NSMutableString`](nsmutablestring.md).

 An immutable string is a text string that is defined when it is created and subsequently cannot be changed. An immutable string is implemented as an array of UTF–16 code units (in other words, a text string). To create and manage an immutable string, use the [`NSString`](nsstring.md) class. To construct and manage a string that can be changed after it has been created, use [`NSMutableString`](nsmutablestring.md).

The objects you create using [`NSString`](nsstring.md) and [`NSMutableString`](nsmutablestring.md) are referred to as string objects (or, when no confusion will result, merely as strings). The term C string refers to the standard `char *` type.

Because of the nature of class clusters, string objects aren’t actual instances of the [`NSString`](nsstring.md) or [`NSMutableString`](nsmutablestring.md) classes but of one of their private subclasses. Although a string object’s class is private, its interface is public, as declared by these abstract superclasses, [`NSString`](nsstring.md) and [`NSMutableString`](nsmutablestring.md). The string classes adopt the [`NSCopying`](nscopying.md) and [`NSMutableCopying`](nsmutablecopying.md) protocols, making it convenient to convert a string of one type to the other.

###### Understanding Characters

A string object presents itself as a sequence of UTF–16 code units. You can determine how many UTF-16 code units a string object contains with the [`length`](nsstring/length.md) method and can retrieve a specific UTF-16 code unit with the [`character(at:)`](nsstring/character(at:).md) method. These two “primitive” methods provide basic access to a string object.

Most use of strings, however, is at a higher level, with the strings being treated as single entities: You compare strings against one another, search them for substrings, combine them into new strings, and so on. If you need to access string objects character by character, you must understand the Unicode character encoding, specifically issues related to composed character sequences. For details see  (The Unicode Consortium, Boston: Addison-Wesley, 2003, ISBN 0-321-18578-1) and the Unicode Consortium web site: [`http://www.unicode.org/`](https://developer.apple.comhttp://www.unicode.org/). See also [`Characters and Grapheme Clusters`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/stringsClusters.html#//apple_ref/doc/uid/TP40008025) in [`String Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i).

Localized string comparisons are based on the Unicode Collation Algorithm, as tailored for different languages by CLDR (Common Locale Data Repository). Both are projects of the Unicode Consortium. Unicode is a registered trademark of Unicode, Inc.

###### Interpreting Utf 16 Encoded Data

When creating an `NSString` object from a UTF-16-encoded string (or a byte stream interpreted as UTF-16), if the byte order is not otherwise specified, `NSString` assumes that the UTF-16 characters are big-endian, unless there is a BOM (byte-order mark), in which case the BOM dictates the byte order. When creating an `NSString` object from an array of `unichar` values, the returned string is always native-endian, since the array always contains UTF–16 code units in native byte order.

##### Subclassing Notes

It is possible to subclass [`NSString`](nsstring.md) (and [`NSMutableString`](nsmutablestring.md)), but doing so requires providing storage facilities for the string (which is not inherited by subclasses) and implementing two primitive methods. The abstract [`NSString`](nsstring.md) and [`NSMutableString`](nsmutablestring.md) classes are the public interface of a class cluster consisting mostly of private, concrete classes that create and return a string object appropriate for a given situation. Making your own concrete subclass of this cluster imposes certain requirements (discussed in [`Methods to Override`](nsstring#Methods-to-Override.md)).

Make sure your reasons for subclassing [`NSString`](nsstring.md) are valid. Instances of your subclass should represent a string and not something else. Thus the only attributes the subclass should have are the length of the character buffer it’s managing and access to individual characters in the buffer. Valid reasons for making a subclass of [`NSString`](nsstring.md) include providing a different backing store (perhaps for better performance) or implementing some aspect of object behavior differently, such as memory management. If your purpose is to add non-essential attributes or metadata to your subclass of [`NSString`](nsstring.md), a better alternative would be object composition (see [`Alternatives to Subclassing`](nsstring#Alternatives-to-Subclassing.md)). Cocoa already provides an example of this with the [`NSAttributedString`](nsattributedstring.md) class.

###### Methods to Override

Any subclass of `NSString`    override the primitive instance methods [`length`](nsstring/length.md) and [`character(at:)`](nsstring/character(at:).md). These methods must operate on the backing store that you provide for the characters of the string. For this backing store you can use a static array, a dynamically allocated buffer, a standard `NSString` object, or some other data type or mechanism. You may also choose to override, partially or fully, any other `NSString` method for which you want to provide an alternative implementation. For example, for better performance it is recommended that you override [`getCharacters(_:range:)`](nsstring/getcharacters(_:range:).md) and give it a faster implementation.

You might want to implement an initializer for your subclass that is suited to the backing store that the subclass is managing. The `NSString` class does not have a designated initializer, so your initializer need only invoke the [`init()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/init()) method of `super`. The `NSString` class adopts the [`NSCopying`](nscopying.md), [`NSMutableCopying`](nsmutablecopying.md), and [`NSCoding`](nscoding.md) protocols; if you want instances of your own custom subclass created from copying or coding, override the methods in these protocols.

###### Alternatives to Subclassing

Often a better and easier alternative to making a subclass of `NSString`—or of any other abstract, public class of a class cluster, for that matter—is object composition. This is especially the case when your intent is to add to the subclass metadata or some other attribute that is not essential to a string object. In object composition, you would have an `NSString` object as one instance variable of your custom class (typically a subclass of `NSObject`) and one or more instance variables that store the metadata that you want for the custom object. Then just design your subclass interface to include accessor methods for the embedded string object and the metadata.

If the behavior you want to add supplements that of the existing class, you could write a category on `NSString`. Keep in mind, however, that this category will be in effect for all instances of `NSString` that you use, and this might have unintended consequences.

## Topics

### Creating and Initializing Strings
- [init()](nsstring/init.md)
  Returns an initialized `NSString` object that contains no characters.
- [convenience init?(bytes: UnsafeRawPointer, length: Int, encoding: UInt)](nsstring/init(bytes:length:encoding:).md)
  Returns an initialized `NSString` object containing a given number of bytes from a given buffer of bytes interpreted in a given encoding.
- [convenience init?(bytesNoCopy: UnsafeMutableRawPointer, length: Int, encoding: UInt, freeWhenDone: Bool)](nsstring/init(bytesnocopy:length:encoding:freewhendone:).md)
  Returns an initialized `NSString` object that contains a given number of bytes from a given buffer of bytes interpreted in a given encoding, and optionally frees the buffer.
- [convenience init(characters: UnsafePointer<unichar>, length: Int)](nsstring/init(characters:length:).md)
  Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [convenience init(charactersNoCopy: UnsafeMutablePointer<unichar>, length: Int, freeWhenDone: Bool)](nsstring/init(charactersnocopy:length:freewhendone:).md)
  Returns an initialized `NSString` object that contains a given number of characters from a given C array of UTF-16 code units.
- [convenience init(string: String)](nsstring/init(string:)-210xa.md)
  Returns an `NSString` object initialized by copying the characters from another given string.
- [convenience init?(CString: UnsafePointer<CChar>, encoding: UInt)](nsstring/init(cstring:encoding:)-20f9h.md)
  Returns an `NSString` object initialized using the characters in a given C array, interpreted according to a given encoding.
- [convenience init?(UTF8String: UnsafePointer<CChar>)](nsstring/init(utf8string:)-vg2b.md)
  Returns an `NSString` object initialized by copying the characters from a given C array of UTF8-encoded bytes.
- [convenience init(format: String, arguments: CVaListPointer)](nsstring/init(format:arguments:).md)
  Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted without any localization.
- [convenience init(format: String, locale: Any?, arguments: CVaListPointer)](nsstring/init(format:locale:arguments:).md)
  Returns an `NSString` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information. This method is meant to be called from within a variadic function, where the argument list will be available.
- [convenience init?(data: Data, encoding: UInt)](nsstring/init(data:encoding:).md)
  Returns an `NSString` object initialized by converting given data into UTF-16 code units using a given encoding.
- [class func localizedUserNotificationString(forKey: String, arguments: [Any]?) -> String](nsstring/localizedusernotificationstring(forkey:arguments:).md)
  Returns a localized string intended for display in a notification alert.
- [class func localizedStringWithFormat(NSString, any CVarArg...) -> Self](nsstring/localizedstringwithformat(_:_:).md)
- [convenience init?(CString: UnsafePointer<CChar>, encoding: UInt)](nsstring/init(cstring:encoding:)-7auq8.md)
  Returns a string containing the bytes in a given C array, interpreted according to a given encoding.
- [convenience init?(UTF8String: UnsafePointer<CChar>)](nsstring/init(utf8string:)-8bcy8.md)
  Returns a string created by copying the data from a given C array of UTF8-encoded bytes.
- [typealias unichar](unichar.md)
  Type for UTF-16 code units.
### Creating and Initializing a String from a File
- [convenience init(contentsOfFile: String, encoding: UInt) throws](nsstring/init(contentsoffile:encoding:).md)
  Returns an `NSString` object initialized by reading data from the file at a given path using a given encoding.
- [convenience init(contentsOfFile: String, usedEncoding: UnsafeMutablePointer<UInt>?) throws](nsstring/init(contentsoffile:usedencoding:).md)
  Returns an `NSString` object initialized by reading data from the file at a given path and returns by reference the encoding used to interpret the characters.
### Creating and Initializing a String from an URL
- [convenience init(contentsOfURL: URL, encoding: UInt) throws](nsstring/init(contentsofurl:encoding:)-x6cv.md)
  Returns a string created by reading data from a given URL interpreted using a given encoding.
- [convenience init(contentsOfURL: URL, encoding: UInt) throws](nsstring/init(contentsofurl:encoding:)-715fw.md)
  Returns an `NSString` object initialized by reading data from a given URL interpreted using a given encoding.
- [convenience init(contentsOfURL: URL, usedEncoding: UnsafeMutablePointer<UInt>?) throws](nsstring/init(contentsofurl:usedencoding:)-9jrum.md)
  Returns a string created by reading data from a given URL and returns by reference the encoding used to interpret the data.
- [convenience init(contentsOfURL: URL, usedEncoding: UnsafeMutablePointer<UInt>?) throws](nsstring/init(contentsofurl:usedencoding:)-2c72d.md)
  Returns an `NSString` object initialized by reading data from a given URL and returns by reference the encoding used to interpret the data.
### Getting a String’s Length
- [var length: Int](nsstring/length.md)
  The number of UTF-16 code units in the receiver.
- [func lengthOfBytes(using: UInt) -> Int](nsstring/lengthofbytes(using:).md)
  Returns the number of bytes required to store the receiver in a given encoding.
- [func maximumLengthOfBytes(using: UInt) -> Int](nsstring/maximumlengthofbytes(using:).md)
  Returns the maximum number of bytes needed to store the receiver in a given encoding.
### Getting Characters and Bytes
- [func character(at: Int) -> unichar](nsstring/character(at:).md)
  Returns the character at a given UTF-16 code unit index.
- [func getCharacters(UnsafeMutablePointer<unichar>, range: NSRange)](nsstring/getcharacters(_:range:).md)
  Copies characters from a given range in the receiver into a given buffer.
- [func getBytes(UnsafeMutableRawPointer?, maxLength: Int, usedLength: UnsafeMutablePointer<Int>?, encoding: UInt, options: NSString.EncodingConversionOptions, range: NSRange, remaining: NSRangePointer?) -> Bool](nsstring/getbytes(_:maxlength:usedlength:encoding:options:range:remaining:).md)
  Gets a given range of characters as bytes in a specified encoding.
### Getting C Strings
- [func cString(using: UInt) -> UnsafePointer<CChar>?](nsstring/cstring(using:).md)
  Returns a representation of the string as a C string using a given encoding.
- [func getCString(UnsafeMutablePointer<CChar>, maxLength: Int, encoding: UInt) -> Bool](nsstring/getcstring(_:maxlength:encoding:).md)
  Converts the string to a given encoding and stores it in a buffer.
- [var utf8String: UnsafePointer<CChar>?](nsstring/utf8string.md)
  A null-terminated UTF8 representation of the string.
### Identifying and Comparing Strings
- [func caseInsensitiveCompare(String) -> ComparisonResult](nsstring/caseinsensitivecompare(_:).md)
  Returns the result of invoking [`compare(_:options:)`](nsstring/compare(_:options:).md) with `NSCaseInsensitiveSearch` as the only option.
- [func localizedCaseInsensitiveCompare(String) -> ComparisonResult](nsstring/localizedcaseinsensitivecompare(_:).md)
  Compares the string with a given string using a case-insensitive, localized, comparison.
- [func compare(String) -> ComparisonResult](nsstring/compare(_:).md)
  Returns the result of invoking [`compare(_:options:range:)`](nsstring/compare(_:options:range:).md) with no options and the receiver’s full extent as the range.
- [func localizedCompare(String) -> ComparisonResult](nsstring/localizedcompare(_:).md)
  Compares the string and a given string using a localized comparison.
- [func compare(String, options: NSString.CompareOptions) -> ComparisonResult](nsstring/compare(_:options:).md)
  Compares the string with the specified string using the given options.
- [func compare(String, options: NSString.CompareOptions, range: NSRange) -> ComparisonResult](nsstring/compare(_:options:range:).md)
  Returns the result of invoking [`compare(_:options:range:locale:)`](nsstring/compare(_:options:range:locale:).md) with a `nil` locale.
- [func compare(String, options: NSString.CompareOptions, range: NSRange, locale: Any?) -> ComparisonResult](nsstring/compare(_:options:range:locale:).md)
  Compares the string using the specified options and returns the lexical ordering for the range.
- [func localizedStandardCompare(String) -> ComparisonResult](nsstring/localizedstandardcompare(_:).md)
  Compares strings as sorted by the Finder.
- [func hasPrefix(String) -> Bool](nsstring/hasprefix(_:).md)
  Returns a Boolean value that indicates whether a given string matches the beginning characters of the receiver.
- [func hasSuffix(String) -> Bool](nsstring/hassuffix(_:).md)
  Returns a Boolean value that indicates whether a given string matches the ending characters of the receiver.
- [func isEqual(to: String) -> Bool](nsstring/isequal(to:).md)
  Returns a Boolean value that indicates whether a given string is equal to the receiver using a literal Unicode-based comparison.
- [var hash: Int](nsstring/hash.md)
  An unsigned integer that can be used as a hash table address.
- [NSString.CompareOptions](nsstring/compareoptions.md)
  These values represent the options available to many of the string classes’ search and comparison methods.
- [NSString.EncodingConversionOptions](nsstring/encodingconversionoptions.md)
  Options for converting string encodings.
### Combining Strings
- [func appendingFormat(NSString, any CVarArg...) -> NSString](nsstring/appendingformat(_:_:).md)
- [func appending(String) -> String](nsstring/appending(_:).md)
  Returns a new string made by appending a given string to the receiver.
- [func padding(toLength: Int, withPad: String, startingAt: Int) -> String](nsstring/padding(tolength:withpad:startingat:).md)
  Returns a new string formed from the receiver by either removing characters from the end, or by appending as many occurrences as necessary of a given pad string.
### Changing Case
- [var lowercased: String](nsstring/lowercased.md)
  A lowercase representation of the string.
- [var localizedLowercase: String](nsstring/localizedlowercase.md)
  Returns a version of the string with all letters converted to lowercase, taking into account the current locale.
- [func lowercased(with: Locale?) -> String](nsstring/lowercased(with:).md)
  Returns a version of the string with all letters converted to lowercase, taking into account the specified locale.
- [var uppercased: String](nsstring/uppercased.md)
  An uppercase representation of the string.
- [var localizedUppercase: String](nsstring/localizeduppercase.md)
  Returns a version of the string with all letters converted to uppercase, taking into account the current locale.
- [func uppercased(with: Locale?) -> String](nsstring/uppercased(with:).md)
  Returns a version of the string with all letters converted to uppercase, taking into account the specified locale.
- [var capitalized: String](nsstring/capitalized.md)
  A capitalized representation of the string.
- [var localizedCapitalized: String](nsstring/localizedcapitalized.md)
  Returns a capitalized representation of the receiver using the current locale.
- [func capitalized(with: Locale?) -> String](nsstring/capitalized(with:).md)
  Returns a capitalized representation of the receiver using the specified locale.
### Dividing Strings
- [func components(separatedBy: String) -> [String]](nsstring/components(separatedby:)-238fy.md)
  Returns an array containing substrings from the receiver that have been divided by a given separator.
- [func components(separatedBy: CharacterSet) -> [String]](nsstring/components(separatedby:)-27x9g.md)
  Returns an array containing substrings from the receiver that have been divided by characters in a given set.
- [func trimmingCharacters(in: CharacterSet) -> String](nsstring/trimmingcharacters(in:).md)
  Returns a new string made by removing from both ends of the receiver characters contained in a given character set.
- [func substring(from: Int) -> String](nsstring/substring(from:).md)
  Returns a new string containing the characters of the receiver from the one at a given index to the end.
- [func substring(with: NSRange) -> String](nsstring/substring(with:).md)
  Returns a string object containing the characters of the receiver that lie within a given range.
- [func substring(to: Int) -> String](nsstring/substring(to:).md)
  Returns a new string containing the characters of the receiver up to, but not including, the one at a given index.
### Normalizing Strings
- [var decomposedStringWithCanonicalMapping: String](nsstring/decomposedstringwithcanonicalmapping.md)
  A string made by normalizing the string’s contents using the Unicode Normalization Form D.
- [var decomposedStringWithCompatibilityMapping: String](nsstring/decomposedstringwithcompatibilitymapping.md)
  A string made by normalizing the receiver’s contents using the Unicode Normalization Form KD.
- [var precomposedStringWithCanonicalMapping: String](nsstring/precomposedstringwithcanonicalmapping.md)
  A string made by normalizing the string’s contents using the Unicode Normalization Form C.
- [var precomposedStringWithCompatibilityMapping: String](nsstring/precomposedstringwithcompatibilitymapping.md)
  A string made by normalizing the receiver’s contents using the Unicode Normalization Form KC.
### Folding Strings
- [func folding(options: NSString.CompareOptions, locale: Locale?) -> String](nsstring/folding(options:locale:).md)
  Creates a string suitable for comparison by removing the specified character distinctions from a string.
### Transforming Strings
- [func applyingTransform(StringTransform, reverse: Bool) -> String?](nsstring/applyingtransform(_:reverse:).md)
  Returns a new string by applying a specified transform to the string.
- [struct StringTransform](stringtransform.md)
  Constants representing an ICU string transform.
### Finding Characters and Substrings
- [func contains(String) -> Bool](nsstring/contains(_:).md)
  Returns a Boolean value indicating whether the string contains a given string by performing a case-sensitive, locale-unaware search.
- [func localizedCaseInsensitiveContains(String) -> Bool](nsstring/localizedcaseinsensitivecontains(_:).md)
  Returns a Boolean value indicating whether the string contains a given string by performing a case-insensitive, locale-aware search.
- [func localizedStandardContains(String) -> Bool](nsstring/localizedstandardcontains(_:).md)
  Returns a Boolean value indicating whether the string contains a given string by performing a case and diacritic insensitive, locale-aware search.
- [func rangeOfCharacter(from: CharacterSet) -> NSRange](nsstring/rangeofcharacter(from:).md)
  Finds and returns the range in the string of the first character from a given character set.
- [func rangeOfCharacter(from: CharacterSet, options: NSString.CompareOptions) -> NSRange](nsstring/rangeofcharacter(from:options:).md)
  Finds and returns the range in the string of the first character, using given options, from a given character set.
- [func rangeOfCharacter(from: CharacterSet, options: NSString.CompareOptions, range: NSRange) -> NSRange](nsstring/rangeofcharacter(from:options:range:).md)
  Finds and returns the range in the string of the first character from a given character set found in a given range with given options.
- [func range(of: String) -> NSRange](nsstring/range(of:).md)
  Finds and returns the range of the first occurrence of a given string within the string.
- [func range(of: String, options: NSString.CompareOptions) -> NSRange](nsstring/range(of:options:).md)
  Finds and returns the range of the first occurrence of a given string within the string, subject to given options.
- [func range(of: String, options: NSString.CompareOptions, range: NSRange) -> NSRange](nsstring/range(of:options:range:).md)
  Finds and returns the range of the first occurrence of a given string, within the given range of the string, subject to given options.
- [func range(of: String, options: NSString.CompareOptions, range: NSRange, locale: Locale?) -> NSRange](nsstring/range(of:options:range:locale:).md)
  Finds and returns the range of the first occurrence of a given string within a given range of the string, subject to given options, using the specified locale, if any.
- [func localizedStandardRange(of: String) -> NSRange](nsstring/localizedstandardrange(of:).md)
  Finds and returns the range of the first occurrence of a given string within the string by performing a case and diacritic insensitive, locale-aware search.
- [func enumerateLines((String, UnsafeMutablePointer<ObjCBool>) -> Void)](nsstring/enumeratelines(_:).md)
  Enumerates all the lines in the string.
- [func enumerateSubstrings(in: NSRange, options: NSString.EnumerationOptions, using: (String?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsstring/enumeratesubstrings(in:options:using:).md)
  Enumerates the substrings of the specified type in the specified range of the string.
### Replacing Substrings
- [func replacingOccurrences(of: String, with: String) -> String](nsstring/replacingoccurrences(of:with:).md)
  Returns a new string in which all occurrences of a target string in the receiver are replaced by another given string.
- [func replacingOccurrences(of: String, with: String, options: NSString.CompareOptions, range: NSRange) -> String](nsstring/replacingoccurrences(of:with:options:range:).md)
  Returns a new string in which all occurrences of a target string in a specified range of the receiver are replaced by another given string.
- [func replacingCharacters(in: NSRange, with: String) -> String](nsstring/replacingcharacters(in:with:).md)
  Returns a new string in which the characters in a specified range of the receiver are replaced by a given string.
### Getting a Shared Prefix
- [func commonPrefix(with: String, options: NSString.CompareOptions) -> String](nsstring/commonprefix(with:options:).md)
  Returns a string containing characters the receiver and a given string have in common, starting from the beginning of each up to the first characters that aren’t equivalent.
### Performing Linguistic Analysis
- [func enumerateLinguisticTags(in: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, using: (NSLinguisticTag?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsstring/enumeratelinguistictags(in:scheme:options:orthography:using:).md)
  Performs linguistic analysis on the specified string by enumerating the specific range of the string, providing the Block with the located tags.
- [func linguisticTags(in: NSRange, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options, orthography: NSOrthography?, tokenRanges: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> [NSLinguisticTag]](nsstring/linguistictags(in:scheme:options:orthography:tokenranges:).md)
  Returns an array of linguistic tags for the specified range and requested tags within the receiving string.
- [NSString.EnumerationOptions](nsstring/enumerationoptions.md)
  Constants to specify kinds of substrings and styles of enumeration.
### Determining Line and Paragraph Ranges
- [func getLineStart(UnsafeMutablePointer<Int>?, end: UnsafeMutablePointer<Int>?, contentsEnd: UnsafeMutablePointer<Int>?, for: NSRange)](nsstring/getlinestart(_:end:contentsend:for:).md)
  Returns by reference the beginning of the first line and the end of the last line touched by the given range.
- [func lineRange(for: NSRange) -> NSRange](nsstring/linerange(for:).md)
  Returns the range of characters representing the line or lines containing a given range.
- [func getParagraphStart(UnsafeMutablePointer<Int>?, end: UnsafeMutablePointer<Int>?, contentsEnd: UnsafeMutablePointer<Int>?, for: NSRange)](nsstring/getparagraphstart(_:end:contentsend:for:).md)
  Returns by reference the beginning of the first paragraph and the end of the last paragraph touched by the given range.
- [func paragraphRange(for: NSRange) -> NSRange](nsstring/paragraphrange(for:).md)
  Returns the range of characters representing the paragraph or paragraphs containing a given range.
### Determining Composed Character Sequences
- [func rangeOfComposedCharacterSequence(at: Int) -> NSRange](nsstring/rangeofcomposedcharactersequence(at:).md)
  Returns the range in the receiver of the composed character sequence located at a given index.
- [func rangeOfComposedCharacterSequences(for: NSRange) -> NSRange](nsstring/rangeofcomposedcharactersequences(for:).md)
  Returns the range in the string of the composed character sequences for a given range.
### Writing to a File or URL
- [func write(toFile: String, atomically: Bool, encoding: UInt) throws](nsstring/write(tofile:atomically:encoding:).md)
  Writes the contents of the receiver to a file at a given path using a given encoding.
- [func write(to: URL, atomically: Bool, encoding: UInt) throws](nsstring/write(to:atomically:encoding:).md)
  Writes the contents of the receiver to the URL specified by `url` using the specified encoding.
### Converting String Contents Into a Property List
- [func propertyList() -> Any](nsstring/propertylist.md)
  Parses the receiver as a text representation of a property list, returning an `NSString`, `NSData`, `NSArray`, or `NSDictionary` object, according to the topmost element.
- [func propertyListFromStringsFileFormat() -> [AnyHashable : Any]?](nsstring/propertylistfromstringsfileformat.md)
  Returns a dictionary object initialized with the keys and values found in the receiver.
### Sizing and Drawing Strings
- [func draw(at: CGPoint, withAttributes: [NSAttributedString.Key : Any]?)](nsstring/draw(at:withattributes:).md)
  Draws the receiver with the font and other display characteristics of the given attributes, at the specified point in the current graphics context.
- [func draw(in: CGRect, withAttributes: [NSAttributedString.Key : Any]?)](nsstring/draw(in:withattributes:).md)
  Draws the attributed string inside the specified bounding rectangle.
- [func draw(with: CGRect, options: NSStringDrawingOptions, attributes: [NSAttributedString.Key : Any]?, context: NSStringDrawingContext?)](nsstring/draw(with:options:attributes:context:).md)
  Draws the attributed string in the specified bounding rectangle using the provided options.
- [func boundingRect(with: CGSize, options: NSStringDrawingOptions, attributes: [NSAttributedString.Key : Any]?, context: NSStringDrawingContext?) -> CGRect](nsstring/boundingrect(with:options:attributes:context:).md)
  Calculates and returns the bounding rect for the receiver drawn using the given options and display characteristics, within the specified rectangle in the current graphics context.
- [func size(withAttributes: [NSAttributedString.Key : Any]?) -> CGSize](nsstring/size(withattributes:).md)
  Returns the bounding box size the receiver occupies when drawn with the given attributes.
- [func variantFittingPresentationWidth(Int) -> String](nsstring/variantfittingpresentationwidth(_:).md)
  Returns a string variation suitable for the specified presentation width.
- [struct NSStringDrawingOptions](../UIKit/NSStringDrawingOptions.md)
  Constants that specify the rendering options for drawing a string.
### Getting Numeric Values
- [var doubleValue: Double](nsstring/doublevalue.md)
  The floating-point value of the string as a `double`.
- [var floatValue: Float](nsstring/floatvalue.md)
  The floating-point value of the string as a `float`.
- [var intValue: Int32](nsstring/intvalue.md)
  The integer value of the string.
- [var integerValue: Int](nsstring/integervalue.md)
  The `NSInteger` value of the string.
- [var longLongValue: Int64](nsstring/longlongvalue.md)
  The `long long` value of the string.
- [var boolValue: Bool](nsstring/boolvalue.md)
  The Boolean value of the string.
### Working with Encodings
- [class var availableStringEncodings: UnsafePointer<UInt>](nsstring/availablestringencodings.md)
  Returns a zero-terminated list of the encodings string objects support in the application’s environment.
- [class var defaultCStringEncoding: UInt](nsstring/defaultcstringencoding.md)
  Returns the C-string encoding assumed for any method accepting a C string as an argument.
- [class func stringEncoding(for: Data, encodingOptions: [StringEncodingDetectionOptionsKey : Any]?, convertedString: AutoreleasingUnsafeMutablePointer<NSString?>?, usedLossyConversion: UnsafeMutablePointer<ObjCBool>?) -> UInt](nsstring/stringencoding(for:encodingoptions:convertedstring:usedlossyconversion:).md)
  Returns the string encoding for the given data as detected by attempting to create a string according to the specified encoding options.
- [class func localizedName(of: UInt) -> String](nsstring/localizedname(of:).md)
  Returns a human-readable string giving the name of a given encoding.
- [func canBeConverted(to: UInt) -> Bool](nsstring/canbeconverted(to:).md)
  Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.
- [func data(using: UInt) -> Data?](nsstring/data(using:).md)
  Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [func data(using: UInt, allowLossyConversion: Bool) -> Data?](nsstring/data(using:allowlossyconversion:).md)
  Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [var description: String](nsstring/description.md)
- [var fastestEncoding: UInt](nsstring/fastestencoding.md)
  The fastest encoding to which the receiver may be converted without loss of information.
- [var smallestEncoding: UInt](nsstring/smallestencoding.md)
  The smallest encoding to which the receiver can be converted without loss of information.
- [struct StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey.md)
- [NSString Handling Exception Names](nsstring-handling-exception-names.md)
  These constants define the names of exceptions raised if `NSString` cannot represent a string in a given encoding, or parse a string as a property list.
### Working with Paths
- [class func path(withComponents: [String]) -> String](nsstring/path(withcomponents:).md)
  Returns a string built from the strings in a given array by concatenating them with a path separator between each pair.
- [var pathComponents: [String]](nsstring/pathcomponents.md)
  The file-system path components of the receiver.
- [func completePath(into: AutoreleasingUnsafeMutablePointer<NSString?>?, caseSensitive: Bool, matchesInto: AutoreleasingUnsafeMutablePointer<NSArray?>?, filterTypes: [String]?) -> Int](nsstring/completepath(into:casesensitive:matchesinto:filtertypes:).md)
  Interprets the receiver as a path in the file system and attempts to perform filename completion, returning a numeric value that indicates whether a match was possible, and by reference the longest path that matches the receiver.
- [var fileSystemRepresentation: UnsafePointer<CChar>](nsstring/filesystemrepresentation.md)
  A file system-specific representation of the receiver.
- [func getFileSystemRepresentation(UnsafeMutablePointer<CChar>, maxLength: Int) -> Bool](nsstring/getfilesystemrepresentation(_:maxlength:).md)
  Interprets the receiver as a system-independent path and fills a buffer with a C-string in a format and encoding suitable for use with file-system calls.
- [var isAbsolutePath: Bool](nsstring/isabsolutepath.md)
  A Boolean value that indicates whether the receiver represents an absolute path.
- [var lastPathComponent: String](nsstring/lastpathcomponent.md)
  The last path component of the receiver.
- [var pathExtension: String](nsstring/pathextension.md)
  The path extension, if any, of the string as interpreted as a path.
- [var abbreviatingWithTildeInPath: String](nsstring/abbreviatingwithtildeinpath.md)
  A new string that replaces the current home directory portion of the current path with a tilde (`~`) character.
- [func appendingPathComponent(String) -> String](nsstring/appendingpathcomponent(_:).md)
  Returns a new string made by appending to the receiver a given string.
- [func appendingPathExtension(String) -> String?](nsstring/appendingpathextension(_:).md)
  Returns a new string made by appending to the receiver an extension separator followed by a given extension.
- [var deletingLastPathComponent: String](nsstring/deletinglastpathcomponent.md)
  A new string made by deleting the last path component from the receiver, along with any final path separator.
- [var deletingPathExtension: String](nsstring/deletingpathextension.md)
  A new string made by deleting the extension (if any, and only the last) from the receiver.
- [var expandingTildeInPath: String](nsstring/expandingtildeinpath.md)
  A new string made by expanding the initial component of the receiver to its full path value.
- [var resolvingSymlinksInPath: String](nsstring/resolvingsymlinksinpath.md)
  A new string made from the receiver by resolving all symbolic links and standardizing path.
- [var standardizingPath: String](nsstring/standardizingpath.md)
  A new string made by removing extraneous path components from the receiver.
- [func strings(byAppendingPaths: [String]) -> [String]](nsstring/strings(byappendingpaths:).md)
  Returns an array of strings made by separately appending to the receiver each string in a given array.
### Working with URL Strings
- [func addingPercentEncoding(withAllowedCharacters: CharacterSet) -> String?](nsstring/addingpercentencoding(withallowedcharacters:).md)
  Returns a new string made from the receiver by replacing all characters not in the specified set with percent-encoded characters.
- [var removingPercentEncoding: String?](nsstring/removingpercentencoding.md)
  Returns a new string made from the receiver by replacing all percent encoded sequences with the matching UTF-8 characters.
### Deprecated
- [class func string(withCString: UnsafePointer<CChar>) -> Any?](nsstring/string(withcstring:).md)
  Creates a new string using a given C-string.
- [convenience init?(CString: UnsafePointer<CChar>)](nsstring/init(cstring:).md)
  Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding.
- [class func string(withCString: UnsafePointer<CChar>, length: Int) -> Any?](nsstring/string(withcstring:length:).md)
  Returns a string containing the characters in a given C-string.
- [convenience init?(CString: UnsafePointer<CChar>, length: Int)](nsstring/init(cstring:length:).md)
  Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding.
- [convenience init?(CStringNoCopy: UnsafeMutablePointer<CChar>, length: Int, freeWhenDone: Bool)](nsstring/init(cstringnocopy:length:freewhendone:).md)
  Initializes the receiver, a newly allocated `NSString` object, by converting the data in a given C-string from the default C-string encoding into the Unicode character encoding.
- [class func string(withContentsOfFile: String) -> Any?](nsstring/string(withcontentsoffile:).md)
  Returns a string created by reading data from the file named by a given path.
- [convenience init?(contentsOfFile: String)](nsstring/init(contentsoffile:).md)
  Initializes the receiver, a newly allocated `NSString` object, by reading data from the file named by `path`.
- [class func string(withContentsOf: URL) -> Any?](nsstring/string(withcontentsof:).md)
  Returns a string created by reading data from the file named by a given URL.
- [convenience init?(contentsOfURL: URL)](nsstring/init(contentsofurl:).md)
  Initializes the receiver, a newly allocated `NSString` object, by reading data from the location named by a given URL.
- [func write(toFile: String, atomically: Bool) -> Bool](nsstring/write(tofile:atomically:).md)
  Writes the contents of the receiver to the file specified by a given path.
- [func write(to: URL, atomically: Bool) -> Bool](nsstring/write(to:atomically:).md)
  Writes the contents of the receiver to the location specified by a given URL.
- [func getCharacters(UnsafeMutablePointer<unichar>)](nsstring/getcharacters(_:).md)
  Copies all characters from the receiver into a given buffer.
- [func cString() -> UnsafePointer<CChar>?](nsstring/cstring.md)
  Returns a representation of the receiver as a C string in the default C-string encoding.
- [func lossyCString() -> UnsafePointer<CChar>?](nsstring/lossycstring.md)
  Returns a representation of the receiver as a C string in the default C-string encoding, possibly losing information in converting to that encoding.
- [func cStringLength() -> Int](nsstring/cstringlength.md)
  Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding.
- [func getCString(UnsafeMutablePointer<CChar>)](nsstring/getcstring(_:).md)
  Invokes [`getCString(_:maxLength:range:remaining:)`](nsstring/getcstring(_:maxlength:range:remaining:).md) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range.
- [func getCString(UnsafeMutablePointer<CChar>, maxLength: Int)](nsstring/getcstring(_:maxlength:).md)
  Invokes [`getCString(_:maxLength:range:remaining:)`](nsstring/getcstring(_:maxlength:range:remaining:).md) with `maxLength` as the maximum length in char-sized units, the receiver’s entire extent as the range, and `NULL` for the remaining range.
- [func getCString(UnsafeMutablePointer<CChar>, maxLength: Int, range: NSRange, remaining: NSRangePointer?)](nsstring/getcstring(_:maxlength:range:remaining:).md)
  Converts the receiver’s content to the default C-string encoding and stores them in a given buffer.
- [func addingPercentEscapes(using: UInt) -> String?](nsstring/addingpercentescapes(using:).md)
  Returns a representation of the receiver using a given encoding to determine the percent escapes necessary to convert the receiver into a legal URL string.
- [func replacingPercentEscapes(using: UInt) -> String?](nsstring/replacingpercentescapes(using:).md)
  Returns a new string made by replacing in the receiver all percent escapes with the matching characters as determined by a given encoding.
- [func draw(with: NSRect, options: NSString.DrawingOptions, attributes: [NSAttributedString.Key : Any]?)](nsstring/draw(with:options:attributes:).md)
  Draws the receiver with the specified options and other display characteristics of the given attributes, within the specified rectangle in the current graphics context.
- [func boundingRect(with: NSSize, options: NSString.DrawingOptions, attributes: [NSAttributedString.Key : Any]?) -> NSRect](nsstring/boundingrect(with:options:attributes:).md)
  Calculates and returns the bounding rect for the receiver drawn using the given options and display characteristics, within the specified rectangle in the current graphics context.
### Structures
- [NSString.DrawingOptions](nsstring/drawingoptions.md)
### Initializers
- [convenience init?(bytesNoCopy: UnsafeMutableRawPointer, length: Int, encoding: UInt, deallocator: ((UnsafeMutableRawPointer, Int) -> Void)?)](nsstring/init(bytesnocopy:length:encoding:deallocator:).md)
- [convenience init(charactersNoCopy: UnsafeMutablePointer<unichar>, length: Int, deallocator: ((UnsafeMutablePointer<unichar>, Int) -> Void)?)](nsstring/init(charactersnocopy:length:deallocator:).md)
- [init?(coder: NSCoder)](nsstring/init(coder:).md)
- [convenience init(format: NSString, any CVarArg...)](nsstring/init(format:_:).md)
- [convenience init(format: NSString, locale: Locale?, any CVarArg...)](nsstring/init(format:locale:_:).md)
- [init?(pasteboardPropertyList: Any, ofType: NSPasteboard.PasteboardType)](nsstring/init(pasteboardpropertylist:oftype:).md)
- [convenience init(string: NSString)](nsstring/init(string:)-7xgq7.md)
### Instance Properties
- [var customPlaygroundQuickLook: PlaygroundQuickLook](nsstring/customplaygroundquicklook.md)
### Instance Methods
- [func appendingPathComponent(String, conformingTo: UTType) -> String](nsstring/appendingpathcomponent(_:conformingto:).md)
- [func appendingPathExtension(for: UTType) -> String](nsstring/appendingpathextension(for:).md)
- [func sr_sensorForDeletionRecordsFromSensor() -> SRSensor?](nsstring/sr_sensorfordeletionrecordsfromsensor.md)
### Type Methods
- [class func deferredLocalizedIntentsString(with: String, any CVarArg...) -> NSString](nsstring/deferredlocalizedintentsstring(with:_:).md)
- [class func deferredLocalizedIntentsString(with: String, table: String, any CVarArg...) -> NSString](nsstring/deferredlocalizedintentsstring(with:table:_:).md)
- [class func deferredLocalizedIntentsString(with: String, table: String, arguments: CVaListPointer) -> NSString](nsstring/deferredlocalizedintentsstring(with:table:arguments:).md)
### Default Implementations
- [ExpressibleByStringLiteral Implementations](nsstring/expressiblebystringliteral-implementations.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSMutableString](nsmutablestring.md)
### Conforms To
- [CKRecordValue](../CloudKit/CKRecordValue-c.protocol.md)
- [CKRecordValueProtocol](../CloudKit/CKRecordValueProtocol.md)
- [CNKeyDescriptor](../Contacts/CNKeyDescriptor.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
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
- [NSPasteboardReading](../AppKit/NSPasteboardReading.md)
- [NSPasteboardWriting](../AppKit/NSPasteboardWriting.md)
- [NSSecureCoding](nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring)*