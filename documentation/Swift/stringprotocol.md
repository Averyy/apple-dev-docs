# StringProtocol

**Framework**: Swift  
**Kind**: protocol  
**Role**: Protocol

A type that can represent a string as a collection of characters.

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
protocol StringProtocol : BidirectionalCollection, Comparable, ExpressibleByStringInterpolation, Hashable, LosslessStringConvertible, TextOutputStream, TextOutputStreamable where Self.Element == Character, Self.Index == String.Index, Self.StringInterpolation == DefaultStringInterpolation, Self.SubSequence : StringProtocol
```

#### Overview

Do not declare new conformances to `StringProtocol`. Only the `String` and `Substring` types in the standard library are valid conforming types.

## Topics

### Operators
- [static func != <RHS>(Self, RHS) -> Bool](./stringprotocol/noteq%28_,_%29.md)
### Associated Types
- [associatedtype SubSequence = Substring](./stringprotocol/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
- [associatedtype UTF16View : BidirectionalCollection](./stringprotocol/utf16view.md)
- [associatedtype UTF8View : Collection](./stringprotocol/utf8view.md)
- [associatedtype UnicodeScalarView : BidirectionalCollection](./stringprotocol/unicodescalarview.md)
### Initializers
- [init(cString: UnsafePointer<CChar>)](./stringprotocol/init%28cstring%29.md)
  Creates a string from the null-terminated, UTF-8 encoded sequence of bytes at the given pointer.
- [init<C, Encoding>(decoding: C, as: Encoding.Type)](./stringprotocol/init%28decoding,as%29.md)
  Creates a string from the given Unicode code units in the specified encoding.
- [init<Encoding>(decodingCString: UnsafePointer<Encoding.CodeUnit>, as: Encoding.Type)](./stringprotocol/init%28decodingcstring,as%29.md)
  Creates a string from the null-terminated sequence of bytes at the given pointer.
### Instance Properties
- [var capitalized: String](./stringprotocol/capitalized.md)
  A copy of the string with each word changed to its corresponding capitalized spelling.
- [var decomposedStringWithCanonicalMapping: String](./stringprotocol/decomposedstringwithcanonicalmapping.md)
  A string created by normalizing the string’s contents using Form D.
- [var decomposedStringWithCompatibilityMapping: String](./stringprotocol/decomposedstringwithcompatibilitymapping.md)
  A string created by normalizing the string’s contents using Form KD.
- [var fastestEncoding: String.Encoding](./stringprotocol/fastestencoding.md)
  The fastest encoding to which the string can be converted without loss of information.
- [var hash: Int](./stringprotocol/hash.md)
  An unsigned integer that can be used as a hash table address.
- [var localizedCapitalized: String](./stringprotocol/localizedcapitalized.md)
  A capitalized representation of the string that is produced using the current locale.
- [var localizedLowercase: String](./stringprotocol/localizedlowercase.md)
  A lowercase version of the string that is produced using the current locale.
- [var localizedUppercase: String](./stringprotocol/localizeduppercase.md)
  An uppercase version of the string that is produced using the current locale.
- [var precomposedStringWithCanonicalMapping: String](./stringprotocol/precomposedstringwithcanonicalmapping.md)
  A string created by normalizing the string’s contents using Form C.
- [var precomposedStringWithCompatibilityMapping: String](./stringprotocol/precomposedstringwithcompatibilitymapping.md)
  A string created by normalizing the string’s contents using Form KC.
- [var removingPercentEncoding: String?](./stringprotocol/removingpercentencoding.md)
  Returns a new string created by replacing all percent-encoded sequences with the matching UTF-8 characters.
- [var smallestEncoding: String.Encoding](./stringprotocol/smallestencoding.md)
  The smallest encoding to which the string can be converted without loss of information.
- [var unicodeScalars: Self.UnicodeScalarView](./stringprotocol/unicodescalars.md)
- [var utf16: Self.UTF16View](./stringprotocol/utf16.md)
- [var utf8: Self.UTF8View](./stringprotocol/utf8.md)
### Instance Methods
- [func addingPercentEncoding(withAllowedCharacters: CharacterSet) -> String?](./stringprotocol/addingpercentencoding%28withallowedcharacters%29.md)
  Returns a new string created by replacing all characters not in the specified set with percent-encoded characters.
- [func appending(some StringProtocol) -> String](./stringprotocol/appending%28_%29.md)
  Returns a new string created by appending the given string.
- [func appendingFormat<T>(T, any CVarArg...) -> String](./stringprotocol/appendingformat%28_,_%29.md)
  Returns a string created by appending a string constructed from a given format string and the following arguments.
- [func applyingTransform(StringTransform, reverse: Bool) -> String?](./stringprotocol/applyingtransform%28_,reverse%29.md)
  Perform string transliteration.
- [func cString(using: String.Encoding) -> [CChar]?](./stringprotocol/cstring%28using%29.md)
  Returns a representation of the string as a C string using a given encoding.
- [func canBeConverted(to: String.Encoding) -> Bool](./stringprotocol/canbeconverted%28to%29.md)
  Returns a Boolean value that indicates whether the string can be converted to the specified encoding without loss of information.
- [func capitalized(with: Locale?) -> String](./stringprotocol/capitalized%28with%29.md)
  Returns a capitalized representation of the string using the specified locale.
- [func caseInsensitiveCompare<T>(T) -> ComparisonResult](./stringprotocol/caseinsensitivecompare%28_%29.md)
  Returns the result of invoking `compare:options:` with `NSCaseInsensitiveSearch` as the only option.
- [func commonPrefix<T>(with: T, options: String.CompareOptions) -> String](./stringprotocol/commonprefix%28with,options%29.md)
  Returns a string containing characters this string and the given string have in common, starting from the beginning of each up to the first characters that aren’t equivalent.
- [func compare<T>(T, options: String.CompareOptions, range: Range<Self.Index>?, locale: Locale?) -> ComparisonResult](./stringprotocol/compare%28_,options,range,locale%29.md)
  Compares the string using the specified options and returns the lexical ordering for the range.
- [func completePath(into: UnsafeMutablePointer<String>?, caseSensitive: Bool, matchesInto: UnsafeMutablePointer<[String]>?, filterTypes: [String]?) -> Int](./stringprotocol/completepath%28into,casesensitive,matchesinto,filtertypes%29.md)
  Interprets the string as a path in the file system and attempts to perform filename completion, returning a numeric value that indicates whether a match was possible, and by reference the longest path that matches the string.
- [func components(separatedBy: CharacterSet) -> [String]](./stringprotocol/components%28separatedby%29-4j26n.md)
  Returns an array containing substrings from the string that have been divided by characters in the given set.
- [func components<T>(separatedBy: T) -> [String]](./stringprotocol/components%28separatedby%29-8gl9t.md)
  Returns an array containing substrings from the string that have been divided by the given separator.
- [func contains<T>(T) -> Bool](./stringprotocol/contains%28_%29-40kbf.md)
  Returns `true` if `other` is non-empty and contained within `self` by case-sensitive, non-literal search. Otherwise, returns `false`.
- [func contains(String) -> Bool](./stringprotocol/contains%28_%29-78f5t.md)
- [func contains(Substring) -> Bool](./stringprotocol/contains%28_%29-78p35.md)
- [func data(using: String.Encoding, allowLossyConversion: Bool) -> Data?](./stringprotocol/data%28using,allowlossyconversion%29.md)
  Returns a `Data` containing a representation of the `String` encoded using a given encoding.
- [func dataDetectorMatches(DataDetector.MatchType, options: DataDetector.Options) -> some AsyncSequence<DataDetector.Match, Never>
](./stringprotocol/datadetectormatches%28_,options%29.md)
  Searches for known data types in a string or a substring.
- [func enumerateLines(invoking: (String, inout Bool) -> Void)](./stringprotocol/enumeratelines%28invoking%29.md)
  Enumerates all the lines in a string.
- [func enumerateLinguisticTags<T, R>(in: R, scheme: T, options: NSLinguisticTagger.Options, orthography: NSOrthography?, invoking: (String, Range<Self.Index>, Range<Self.Index>, inout Bool) -> Void)](./stringprotocol/enumeratelinguistictags%28in,scheme,options,orthography,invoking%29.md)
  Performs linguistic analysis on the specified string by enumerating the specific range of the string, providing the Block with the located tags.
- [func enumerateSubstrings<R>(in: R, options: String.EnumerationOptions, (String?, Range<Self.Index>, Range<Self.Index>, inout Bool) -> Void)](./stringprotocol/enumeratesubstrings%28in,options,_%29.md)
  Enumerates the substrings of the specified type in the specified range of the string.
- [func folding(options: String.CompareOptions, locale: Locale?) -> String](./stringprotocol/folding%28options,locale%29.md)
  Returns a string with the given character folding options applied.
- [func getBytes<R>(inout [UInt8], maxLength: Int, usedLength: UnsafeMutablePointer<Int>, encoding: String.Encoding, options: String.EncodingConversionOptions, range: R, remaining: UnsafeMutablePointer<Range<Self.Index>>) -> Bool](./stringprotocol/getbytes%28_,maxlength,usedlength,encoding,options,range,remaining%29.md)
  Writes the given `range` of characters into `buffer` in a given `encoding`, without any allocations.  Does not NULL-terminate.
- [func getCString(inout [CChar], maxLength: Int, encoding: String.Encoding) -> Bool](./stringprotocol/getcstring%28_,maxlength,encoding%29.md)
  Converts the `String`’s content to a given encoding and stores them in a buffer.
- [func getLineStart(UnsafeMutablePointer<Self.Index>, end: UnsafeMutablePointer<Self.Index>, contentsEnd: UnsafeMutablePointer<Self.Index>, for: some RangeExpression<String.Index>)](./stringprotocol/getlinestart%28_,end,contentsend,for%29.md)
  Returns by reference the beginning of the first line and the end of the last line touched by the given range.
- [func getParagraphStart(UnsafeMutablePointer<Self.Index>, end: UnsafeMutablePointer<Self.Index>, contentsEnd: UnsafeMutablePointer<Self.Index>, for: some RangeExpression<String.Index>)](./stringprotocol/getparagraphstart%28_,end,contentsend,for%29.md)
  Returns by reference the beginning of the first paragraph and the end of the last paragraph touched by the given range.
- [func hasPrefix(String) -> Bool](./stringprotocol/hasprefix%28_%29.md)
- [func hasSuffix(String) -> Bool](./stringprotocol/hassuffix%28_%29.md)
- [func lengthOfBytes(using: String.Encoding) -> Int](./stringprotocol/lengthofbytes%28using%29.md)
  Returns the number of bytes required to store the `String` in a given encoding.
- [func lineRange(for: some RangeExpression<String.Index>) -> Range<Self.Index>](./stringprotocol/linerange%28for%29.md)
  Returns the range of characters representing the line or lines containing a given range.
- [func linguisticTags<T, R>(in: R, scheme: T, options: NSLinguisticTagger.Options, orthography: NSOrthography?, tokenRanges: UnsafeMutablePointer<[Range<Self.Index>]>?) -> [String]](./stringprotocol/linguistictags%28in,scheme,options,orthography,tokenranges%29.md)
  Returns an array of linguistic tags for the specified range and requested tags within the receiving string.
- [func localizedCaseInsensitiveCompare<T>(T) -> ComparisonResult](./stringprotocol/localizedcaseinsensitivecompare%28_%29.md)
  Compares the string and the given string using a case-insensitive, localized, comparison.
- [func localizedCaseInsensitiveContains<T>(T) -> Bool](./stringprotocol/localizedcaseinsensitivecontains%28_%29.md)
  Returns a Boolean value indicating whether the given string is non-empty and contained within this string by case-insensitive, non-literal search, taking into account the current locale.
- [func localizedCompare<T>(T) -> ComparisonResult](./stringprotocol/localizedcompare%28_%29.md)
  Compares the string and the given string using a localized comparison.
- [func localizedStandardCompare<T>(T) -> ComparisonResult](./stringprotocol/localizedstandardcompare%28_%29.md)
  Compares the string and the given string as sorted by the Finder.
- [func localizedStandardContains<T>(T) -> Bool](./stringprotocol/localizedstandardcontains%28_%29.md)
  Returns a Boolean value indicating whether the string contains the given string, taking the current locale into account.
- [func localizedStandardRange<T>(of: T) -> Range<Self.Index>?](./stringprotocol/localizedstandardrange%28of%29.md)
  Finds and returns the range of the first occurrence of a given string, taking the current locale into account.  Returns `nil` if the string was not found.
- [func lowercased() -> String](./stringprotocol/lowercased%28%29.md)
- [func lowercased(with: Locale?) -> String](./stringprotocol/lowercased%28with%29.md)
  Returns a version of the string with all letters converted to lowercase, taking into account the specified locale.
- [func maximumLengthOfBytes(using: String.Encoding) -> Int](./stringprotocol/maximumlengthofbytes%28using%29.md)
  Returns the maximum number of bytes needed to store the `String` in a given encoding.
- [func padding<T>(toLength: Int, withPad: T, startingAt: Int) -> String](./stringprotocol/padding%28tolength,withpad,startingat%29.md)
  Returns a new string formed from the `String` by either removing characters from the end, or by appending as many occurrences as necessary of a given pad string.
- [func paragraphRange(for: some RangeExpression<String.Index>) -> Range<Self.Index>](./stringprotocol/paragraphrange%28for%29.md)
  Returns the range of characters representing the paragraph or paragraphs containing a given range.
- [func propertyList() -> Any](./stringprotocol/propertylist%28%29.md)
  Parses the `String` as a text representation of a property list, returning an NSString, NSData, NSArray, or NSDictionary object, according to the topmost element.
- [func propertyListFromStringsFileFormat() -> [String : String]](./stringprotocol/propertylistfromstringsfileformat%28%29.md)
  Returns a dictionary object initialized with the keys and values found in the `String`.
- [func range<T>(of: T, options: String.CompareOptions, range: Range<Self.Index>?, locale: Locale?) -> Range<Self.Index>?](./stringprotocol/range%28of,options,range,locale%29.md)
  Finds and returns the range of the first occurrence of a given string within a given range of the `String`, subject to given options, using the specified locale, if any.
- [func rangeOfCharacter(from: CharacterSet, options: String.CompareOptions, range: Range<Self.Index>?) -> Range<Self.Index>?](./stringprotocol/rangeofcharacter%28from,options,range%29.md)
  Finds and returns the range in the `String` of the first character from a given character set found in a given range with given options.
- [func rangeOfComposedCharacterSequence(at: Self.Index) -> Range<Self.Index>](./stringprotocol/rangeofcomposedcharactersequence%28at%29.md)
  Returns the range in the `String` of the composed character sequence located at a given index.
- [func rangeOfComposedCharacterSequences<R>(for: R) -> Range<Self.Index>](./stringprotocol/rangeofcomposedcharactersequences%28for%29.md)
  Returns the range in the string of the composed character sequences for a given range.
- [func replacingCharacters<T, R>(in: R, with: T) -> String](./stringprotocol/replacingcharacters%28in,with%29.md)
  Returns a new string in which the characters in a specified range of the `String` are replaced by a given string.
- [func replacingOccurrences<Target, Replacement>(of: Target, with: Replacement, options: String.CompareOptions, range: Range<Self.Index>?) -> String](./stringprotocol/replacingoccurrences%28of,with,options,range%29.md)
  Returns a new string in which all occurrences of a target string in a specified range of the string are replaced by another given string.
- [func split(separator: String, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Substring]](./stringprotocol/split%28separator,maxsplits,omittingemptysubsequences%29-7mfus.md)
- [func split(separator: Substring, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Substring]](./stringprotocol/split%28separator,maxsplits,omittingemptysubsequences%29-8wzc1.md)
- [func substring(from: Self.Index) -> String](./stringprotocol/substring%28from%29.md)
  Returns a new string containing the characters of the `String` from the one at a given index to the end.
- [func substring(to: Self.Index) -> String](./stringprotocol/substring%28to%29.md)
  Returns a new string containing the characters of the `String` up to, but not including, the one at a given index.
- [func substring(with: Range<Self.Index>) -> String](./stringprotocol/substring%28with%29.md)
  Returns a string object containing the characters of the `String` that lie within a given range.
- [func trimmingCharacters(in: CharacterSet) -> String](./stringprotocol/trimmingcharacters%28in%29.md)
  Returns a new string made by removing from both ends of the `String` characters contained in a given character set.
- [func uppercased() -> String](./stringprotocol/uppercased%28%29.md)
- [func uppercased(with: Locale?) -> String](./stringprotocol/uppercased%28with%29.md)
  Returns a version of the string with all letters converted to uppercase, taking into account the specified locale.
- [func withCString<Result>((UnsafePointer<CChar>) throws -> Result) rethrows -> Result](./stringprotocol/withcstring%28_%29.md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.
- [func withCString<Result, Encoding>(encodedAs: Encoding.Type, (UnsafePointer<Encoding.CodeUnit>) throws -> Result) rethrows -> Result](./stringprotocol/withcstring%28encodedas,_%29.md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.
- [func write(to: URL, atomically: Bool, encoding: String.Encoding) throws](./stringprotocol/write%28to,atomically,encoding%29.md)
  Writes the contents of the `String` to the URL specified by url using the specified encoding.
- [func write<T>(toFile: T, atomically: Bool, encoding: String.Encoding) throws](./stringprotocol/write%28tofile,atomically,encoding%29.md)
  Writes the contents of the `String` to a file at a given path using a given encoding.

## Relationships

### Inherits From
- [BidirectionalCollection](./bidirectionalcollection.md)
- [Collection](./collection.md)
- [Comparable](./comparable.md)
- [CustomStringConvertible](./customstringconvertible.md)
- [Equatable](./equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](./expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringInterpolation](./expressiblebystringinterpolation.md)
- [ExpressibleByStringLiteral](./expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](./expressiblebyunicodescalarliteral.md)
- [Hashable](./hashable.md)
- [LosslessStringConvertible](./losslessstringconvertible.md)
- [Sequence](./sequence.md)
- [TextOutputStream](./textoutputstream.md)
- [TextOutputStreamable](./textoutputstreamable.md)
### Conforming Types
- [String](./string.md)
- [Substring](./substring.md)

## See Also

### Related String Types
- [struct Substring](./substring.md)
  A slice of a string.
- [String.Index](./string/index.md)
  A position of a character or code unit in a string.
- [String.UnicodeScalarView](./string/unicodescalarview.md)
  A view of a string’s contents as a collection of Unicode scalar values.
- [String.UTF16View](./string/utf16view.md)
  A view of a string’s contents as a collection of UTF-16 code units.
- [String.UTF8View](./string/utf8view.md)
  A view of a string’s contents as a collection of UTF-8 code units.
- [String.Iterator](./string/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [String.Encoding](./string/encoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol)*