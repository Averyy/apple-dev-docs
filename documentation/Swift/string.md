# String

**Framework**: Swift  
**Kind**: struct

A Unicode string value that is a collection of characters.

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
@frozen
struct String
```

#### Overview

A string is a series of characters, such as `"Swift"`, that forms a collection. Strings in Swift are Unicode correct and locale insensitive, and are designed to be efficient. The `String` type bridges with the Objective-C class `NSString` and offers interoperability with C functions that works with strings.

You can create new strings using string literals or string interpolations. A  is a series of characters enclosed in quotes.

```swift
let greeting = "Welcome!"
```

 are string literals that evaluate any included expressions and convert the results to string form. String interpolations give you an easy way to build a string from multiple pieces. Wrap each expression in a string interpolation in parentheses, prefixed by a backslash.

```swift
let name = "Rosa"
let personalizedGreeting = "Welcome, \(name)!"
// personalizedGreeting == "Welcome, Rosa!"

let price = 2
let number = 3
let cookiePrice = "\(number) cookies: $\(price * number)."
// cookiePrice == "3 cookies: $6."
```

Combine strings using the concatenation operator (`+`).

```swift
let longerGreeting = greeting + " We're glad you're here!"
// longerGreeting == "Welcome! We're glad you're here!"
```

Multiline string literals are enclosed in three double quotation marks (`"""`), with each delimiter on its own line. Indentation is stripped from each line of a multiline string literal to match the indentation of the closing delimiter.

```swift
let banner = """
          __,
         (           o  /) _/_
          `.  , , , ,  //  /
        (___)(_(_/_(_ //_ (__
                     /)
                    (/
        """
```

### Modifying and Comparing Strings

Strings always have value semantics. Modifying a copy of a string leaves the original unaffected.

```swift
var otherGreeting = greeting
otherGreeting += " Have a nice time!"
// otherGreeting == "Welcome! Have a nice time!"

print(greeting)
// Prints "Welcome!"
```

Comparing strings for equality using the equal-to operator (`==`) or a relational operator (like `<` or `>=`) is always performed using Unicode canonical representation. As a result, different representations of a string compare as being equal.

```swift
let cafe1 = "Cafe\u{301}"
let cafe2 = "Café"
print(cafe1 == cafe2)
// Prints "true"
```

The Unicode scalar value `"\u{301}"` modifies the preceding character to include an accent, so `"e\u{301}"` has the same canonical representation as the single Unicode scalar value `"é"`.

Basic string operations are not sensitive to locale settings, ensuring that string comparisons and other operations always have a single, stable result, allowing strings to be used as keys in `Dictionary` instances and for other purposes.

### Accessing String Elements

A string is a collection of , which approximate human-readable characters. Many individual characters, such as “é”, “김”, and “🇮🇳”, can be made up of multiple Unicode scalar values. These scalar values are combined by Unicode’s boundary algorithms into extended grapheme clusters, represented by the Swift `Character` type. Each element of a string is represented by a `Character` instance.

For example, to retrieve the first word of a longer string, you can search for a space and then create a substring from a prefix of the string up to that point:

```swift
let name = "Marie Curie"
let firstSpace = name.firstIndex(of: " ") ?? name.endIndex
let firstName = name[..<firstSpace]
// firstName == "Marie"
```

The `firstName` constant is an instance of the `Substring` type—a type that represents substrings of a string while sharing the original string’s storage. Substrings present the same interface as strings.

```swift
print("\(name)'s first name has \(firstName.count) letters.")
// Prints "Marie Curie's first name has 5 letters."
```

### Accessing a Strings Unicode Representation

If you need to access the contents of a string as encoded in different Unicode encodings, use one of the string’s `unicodeScalars`, `utf16`, or `utf8` properties. Each property provides access to a view of the string as a series of code units, each encoded in a different Unicode encoding.

To demonstrate the different views available for every string, the following examples use this `String` instance:

```swift
let cafe = "Cafe\u{301} du 🌍"
print(cafe)
// Prints "Café du 🌍"
```

The `cafe` string is a collection of the nine characters that are visible when the string is displayed.

```swift
print(cafe.count)
// Prints "9"
print(Array(cafe))
// Prints "["C", "a", "f", "é", " ", "d", "u", " ", "🌍"]"
```

#### Unicode Scalar View

A string’s `unicodeScalars` property is a collection of Unicode scalar values, the 21-bit codes that are the basic unit of Unicode. Each scalar value is represented by a `Unicode.Scalar` instance and is equivalent to a UTF-32 code unit.

```swift
print(cafe.unicodeScalars.count)
// Prints "10"
print(Array(cafe.unicodeScalars))
// Prints "["C", "a", "f", "e", "\u{0301}", " ", "d", "u", " ", "\u{0001F30D}"]"
print(cafe.unicodeScalars.map { $0.value })
// Prints "[67, 97, 102, 101, 769, 32, 100, 117, 32, 127757]"
```

The `unicodeScalars` view’s elements comprise each Unicode scalar value in the `cafe` string. In particular, because `cafe` was declared using the decomposed form of the `"é"` character, `unicodeScalars` contains the scalar values for both the letter `"e"` (101) and the accent character `"´"` (769).

#### Utf 16 View

A string’s `utf16` property is a collection of UTF-16 code units, the 16-bit encoding form of the string’s Unicode scalar values. Each code unit is stored as a `UInt16` instance.

```swift
print(cafe.utf16.count)
// Prints "11"
print(Array(cafe.utf16))
// Prints "[67, 97, 102, 101, 769, 32, 100, 117, 32, 55356, 57101]"
```

The elements of the `utf16` view are the code units for the string when encoded in UTF-16. These elements match those accessed through indexed `NSString` APIs.

```swift
let nscafe = cafe as NSString
print(nscafe.length)
// Prints "11"
print(nscafe.character(at: 3))
// Prints "101"
```

#### Utf 8 View

A string’s `utf8` property is a collection of UTF-8 code units, the 8-bit encoding form of the string’s Unicode scalar values. Each code unit is stored as a `UInt8` instance.

```swift
print(cafe.utf8.count)
// Prints "14"
print(Array(cafe.utf8))
// Prints "[67, 97, 102, 101, 204, 129, 32, 100, 117, 32, 240, 159, 140, 141]"
```

The elements of the `utf8` view are the code units for the string when encoded in UTF-8. This representation matches the one used when `String` instances are passed to C APIs.

```swift
let cLength = strlen(cafe)
print(cLength)
// Prints "14"
```

### Measuring the Length of a String

When you need to know the length of a string, you must first consider what you’ll use the length for. Are you measuring the number of characters that will be displayed on the screen, or are you measuring the amount of storage needed for the string in a particular encoding? A single string can have greatly differing lengths when measured by its different views.

For example, an ASCII character like the capital letter  is represented by a single element in each of its four views. The Unicode scalar value of  is `65`, which is small enough to fit in a single code unit in both UTF-16 and UTF-8.

```swift
let capitalA = "A"
print(capitalA.count)
// Prints "1"
print(capitalA.unicodeScalars.count)
// Prints "1"
print(capitalA.utf16.count)
// Prints "1"
print(capitalA.utf8.count)
// Prints "1"
```

On the other hand, an emoji flag character is constructed from a pair of Unicode scalar values, like `"\u{1F1F5}"` and `"\u{1F1F7}"`. Each of these scalar values, in turn, is too large to fit into a single UTF-16 or UTF-8 code unit. As a result, each view of the string `"🇵🇷"` reports a different length.

```swift
let flag = "🇵🇷"
print(flag.count)
// Prints "1"
print(flag.unicodeScalars.count)
// Prints "2"
print(flag.utf16.count)
// Prints "4"
print(flag.utf8.count)
// Prints "8"
```

To check whether a string is empty, use its `isEmpty` property instead of comparing the length of one of the views to `0`. Unlike with `isEmpty`, calculating a view’s `count` property requires iterating through the elements of the string.

### Accessing String View Elements

To find individual elements of a string, use the appropriate view for your task. For example, to retrieve the first word of a longer string, you can search the string for a space and then create a new string from a prefix of the string up to that point.

```swift
let name = "Marie Curie"
let firstSpace = name.firstIndex(of: " ") ?? name.endIndex
let firstName = name[..<firstSpace]
print(firstName)
// Prints "Marie"
```

Strings and their views share indices, so you can access the UTF-8 view of the `name` string using the same `firstSpace` index.

```swift
print(Array(name.utf8[..<firstSpace]))
// Prints "[77, 97, 114, 105, 101]"
```

Note that an index into one view may not have an exact corresponding position in another view. For example, the `flag` string declared above comprises a single character, but is composed of eight code units when encoded as UTF-8. The following code creates constants for the first and second positions in the `flag.utf8` view. Accessing the `utf8` view with these indices yields the first and second code UTF-8 units.

```swift
let firstCodeUnit = flag.startIndex
let secondCodeUnit = flag.utf8.index(after: firstCodeUnit)
// flag.utf8[firstCodeUnit] == 240
// flag.utf8[secondCodeUnit] == 159
```

When used to access the elements of the `flag` string itself, however, the `secondCodeUnit` index does not correspond to the position of a specific character. Instead of only accessing the specific UTF-8 code unit, that index is treated as the position of the character at the index’s encoded offset. In the case of `secondCodeUnit`, that character is still the flag itself.

```swift
// flag[firstCodeUnit] == "🇵🇷"
// flag[secondCodeUnit] == "🇵🇷"
```

If you need to validate that an index from one string’s view corresponds with an exact position in another view, use the index’s `samePosition(in:)` method or the `init(_:within:)` initializer.

```swift
if let exactIndex = secondCodeUnit.samePosition(in: flag) {
    print(flag[exactIndex])
} else {
    print("No exact match for this position.")
}
// Prints "No exact match for this position."
```

### Performance Optimizations

Although strings in Swift have value semantics, strings use a copy-on-write strategy to store their data in a buffer. This buffer can then be shared by different copies of a string. A string’s data is only copied lazily, upon mutation, when more than one string instance is using the same buffer. Therefore, the first in any sequence of mutating operations may cost O() time and space.

When a string’s contiguous storage fills up, a new buffer must be allocated and data must be moved to the new storage. String buffers use an exponential growth strategy that makes appending to a string a constant time operation when averaged over many append operations.

### Bridging Between String and Nsstring

Any `String` instance can be bridged to `NSString` using the type-cast operator (`as`), and any `String` instance that originates in Objective-C may use an `NSString` instance as its storage. Because any arbitrary subclass of `NSString` can become a `String` instance, there are no guarantees about representation or efficiency when a `String` instance is backed by `NSString` storage. Because `NSString` is immutable, it is just as though the storage was shared by a copy. The first in any sequence of mutating operations causes elements to be copied into unique, contiguous storage which may cost O() time and space, where  is the length of the string’s encoded representation (or more, if the underlying `NSString` has unusual performance characteristics).

For more information about the Unicode terms used in this discussion, see the [`Unicode.org glossary`](https://developer.apple.comhttp://www.unicode.org/glossary/). In particular, this discussion mentions [`extended grapheme clusters`](https://developer.apple.comhttp://www.unicode.org/glossary/#extended_grapheme_cluster), [`Unicode scalar values`](https://developer.apple.comhttp://www.unicode.org/glossary/#unicode_scalar_value), and [`canonical equivalence`](https://developer.apple.comhttp://www.unicode.org/glossary/#canonical_equivalent).

## Topics

### Creating a String
- [init(decoding: FilePath)](string/init(decoding:)-nm7v.md)
  Creates a string by interpreting the file path’s content as UTF-8 on Unix and UTF-16 on Windows.
- [init()](string/init.md)
  Creates an empty string.
- [init(Character)](string/init(_:)-8v3fo.md)
  Creates a string containing the given character.
- [init<S>(S)](string/init(_:)-8og6g.md)
  Creates a new string containing the characters in the given sequence.
- [init<S>(S)](string/init(_:)-1ip93.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init<S>(S)](string/init(_:)-50pwi.md)
  Creates a new string containing the characters in the given sequence.
- [init(Substring)](string/init(_:)-14lv5.md)
  Creates a new string from the given substring.
- [init(repeating: String, count: Int)](string/init(repeating:count:)-23xjt.md)
  Creates a new string representing the given string repeated the specified number of times.
- [init(repeating: Character, count: Int)](string/init(repeating:count:)-11bpi.md)
  Creates a string representing the given character repeated the specified number of times.
- [init(unsafeUninitializedCapacity: Int, initializingUTF8With: (UnsafeMutableBufferPointer<UInt8>) throws -> Int) rethrows](string/init(unsafeuninitializedcapacity:initializingutf8with:).md)
  Creates a new string with the specified capacity in UTF-8 code units, and then calls the given closure with a buffer covering the string’s uninitialized memory.
### Inspecting a String
- [var isEmpty: Bool](string/isempty.md)
  A Boolean value indicating whether a string has no characters.
- [var count: Int](string/count.md)
  The number of characters in a string.
### Creating a String from Unicode Data
- [init(Unicode.Scalar)](string/init(_:)-8ay23.md)
- [init?(data: Data, encoding: String.Encoding)](string/init(data:encoding:).md)
  Returns a `String` initialized by converting given `data` into Unicode characters using a given `encoding`.
- [init?(validatingUTF8: UnsafePointer<CChar>)](string/init(validatingutf8:)-208fn.md)
  Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
- [init?<Encoding>(validating: some Sequence, as: Encoding.Type)](string/init(validating:as:)-84qr9.md)
  Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init?<Encoding>(validating: some Sequence<Int8>, as: Encoding.Type)](string/init(validating:as:)-5cw2c.md)
  Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init?(utf8String: [CChar])](string/init(utf8string:)-8qmaq.md)
  Creates a string by copying the data from a given null-terminated array of UTF8-encoded bytes.
- [init?(utf8String: UnsafePointer<CChar>)](string/init(utf8string:)-3mcco.md)
  Creates a string by copying the data from a given null-terminated C array of UTF8-encoded bytes.
- [init(utf16CodeUnits: UnsafePointer<unichar>, count: Int)](string/init(utf16codeunits:count:).md)
  Creates a new string that contains the specified number of characters from the given C array of Unicode characters.
- [init(utf16CodeUnitsNoCopy: UnsafePointer<unichar>, count: Int, freeWhenDone: Bool)](string/init(utf16codeunitsnocopy:count:freewhendone:).md)
  Creates a new string that contains the specified number of characters from the given C array of UTF-16 code units.
- [init<C, Encoding>(decoding: C, as: Encoding.Type)](string/init(decoding:as:).md)
  Creates a string from the given Unicode code units in the specified encoding.
### Creating a String Using Formats
- [init(format: String, any CVarArg...)](string/init(format:_:).md)
  Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted.
- [init(format: String, arguments: [any CVarArg])](string/init(format:arguments:).md)
  Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.
- [init(format: String, locale: Locale?, any CVarArg...)](string/init(format:locale:_:).md)
  Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.
- [init(format: String, locale: Locale?, arguments: [any CVarArg])](string/init(format:locale:arguments:).md)
  Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.
- [static func localizedStringWithFormat(String, any CVarArg...) -> String](string/localizedstringwithformat(_:_:).md)
  Returns a string created by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.
### Creating a Localized String
- [init(localized: String.LocalizationValue, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](string/init(localized:table:bundle:locale:comment:).md)
  Creates a localized string from an interpolated string.
- [init(localized: String.LocalizationValue, options: String.LocalizationOptions, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](string/init(localized:options:table:bundle:locale:comment:).md)
  Creates a localized string from an interpolated string, applying the specified options.
- [String.LocalizationValue](string/localizationvalue.md)
  A reference to a localizable string, with optional string interpolation.
- [String.LocalizationOptions](string/localizationoptions.md)
  Options to apply when initializing a localized string.
- [init(localized: StaticString, defaultValue: String.LocalizationValue, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](string/init(localized:defaultvalue:table:bundle:locale:comment:).md)
  Creates a localized string from an arbitrary static string key.
- [init(localized: StaticString, defaultValue: String.LocalizationValue, options: String.LocalizationOptions, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](string/init(localized:defaultvalue:options:table:bundle:locale:comment:).md)
  Creates a localized string from an arbitrary static string key, applying the specified options.
- [init(localized: LocalizedStringResource)](string/init(localized:).md)
  Creates a localized string from a localized string resource.
- [init(localized: LocalizedStringResource, options: String.LocalizationOptions)](string/init(localized:options:).md)
  Creates a localized string from a localized string resource, applying the specified options.
### Converting Numeric Values
- [init<T>(T, radix: Int, uppercase: Bool)](string/init(_:radix:uppercase:).md)
  Creates a string representing the given value in base 10, or some other specified base.
### Converting a C String
- [init?<S>(bytes: S, encoding: String.Encoding)](string/init(bytes:encoding:).md)
  Creates a new string equivalent to the given bytes interpreted in the specified encoding. Note: This API does not interpret embedded nulls as termination of the string. Use `String?(validatingCString:)` instead for null-terminated C strings.
- [init?(bytesNoCopy: UnsafeMutableRawPointer, length: Int, encoding: String.Encoding, freeWhenDone: Bool)](string/init(bytesnocopy:length:encoding:freewhendone:).md)
  Creates a new string that contains the specified number of bytes from the given buffer, interpreted in the specified encoding, and optionally frees the buffer.
- [init?(validatingCString: UnsafePointer<CChar>)](string/init(validatingcstring:)-992vo.md)
  Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
- [init?(validatingCString: [CChar])](string/init(validatingcstring:)-98wra.md)
  Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given array.
- [init(cString: UnsafePointer<CChar>)](string/init(cstring:)-2p84k.md)
  Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init(cString: UnsafePointer<UInt8>)](string/init(cstring:)-6kr8s.md)
  Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init?(cString: [CChar], encoding: String.Encoding)](string/init(cstring:encoding:)-3h7bc.md)
  Produces a string by copying the null-terminated bytes in a given array, interpreted according to a given encoding.
- [init?(cString: UnsafePointer<CChar>, encoding: String.Encoding)](string/init(cstring:encoding:)-3qgzd.md)
  Produces a string by copying the null-terminated bytes in a given C array, interpreted according to a given encoding.
- [init<Encoding>(decodingCString: [Encoding.CodeUnit], as: Encoding.Type)](string/init(decodingcstring:as:)-8way7.md)
  Creates a new string by copying the null-terminated sequence of code units referenced by the given array.
- [static func decodeCString<Encoding>(UnsafePointer<Encoding.CodeUnit>?, as: Encoding.Type, repairingInvalidCodeUnits: Bool) -> (result: String, repairsMade: Bool)?](string/decodecstring(_:as:repairinginvalidcodeunits:)-46n2p.md)
  Creates a new string by copying the null-terminated data referenced by the given pointer using the specified encoding.
### Converting Other Types to Strings
- [init<T>(T)](string/init(_:)-1ywfq.md)
  Creates an instance from the description of a given `LosslessStringConvertible` instance.
- [init<Subject>(describing: Subject)](string/init(describing:)-588wb.md)
  Creates a string representing the given value.
- [init<Subject>(describing: Subject)](string/init(describing:)-hsqw.md)
  Creates a string representing the given value.
- [init<Subject>(describing: Subject)](string/init(describing:)-6ttci.md)
  Creates a string representing the given value.
- [init<Subject>(describing: Subject)](string/init(describing:)-67ncf.md)
  Creates a string representing the given value.
- [init<Subject>(reflecting: Subject)](string/init(reflecting:).md)
  Creates a string with a detailed representation of the given value, suitable for debugging.
### Creating a String from a File or URL
- [init(contentsOf: URL) throws](string/init(contentsof:).md)
- [init(contentsOf: URL, encoding: String.Encoding) throws](string/init(contentsof:encoding:).md)
  Produces a string created by reading data from a given URL interpreted using a given encoding.
- [init(contentsOf: URL, usedEncoding: inout String.Encoding) throws](string/init(contentsof:usedencoding:).md)
  Produces a string created by reading data from a given URL and returns by reference the encoding used to interpret the data.
- [init(contentsOfFile: String) throws](string/init(contentsoffile:).md)
- [init(contentsOfFile: String, encoding: String.Encoding) throws](string/init(contentsoffile:encoding:).md)
  Produces a string created by reading data from the file at a given path interpreted using a given encoding.
- [init(contentsOfFile: String, usedEncoding: inout String.Encoding) throws](string/init(contentsoffile:usedencoding:).md)
  Produces a string created by reading data from the file at a given path and returns by reference the encoding used to interpret the file.
### Writing to a File or URL
- [func write(String)](string/write(_:).md)
  Appends the given string to this string.
- [func write<Target>(to: inout Target)](string/write(to:).md)
  Writes the string into the given output stream.
### Appending Strings and Characters
- [func append(String)](string/append(_:)-4xa8f.md)
  Appends the given string to this string.
- [func append(Character)](string/append(_:)-4xi3j.md)
  Appends the given character to the string.
- [func append(contentsOf: String)](string/append(contentsof:)-oxek.md)
- [func append(contentsOf: Substring)](string/append(contentsof:)-9vb4t.md)
- [func append<S>(contentsOf: S)](string/append(contentsof:)-7est5.md)
  Appends the characters in the given sequence to the string.
- [func append<S>(contentsOf: S)](string/append(contentsof:)-9foms.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func reserveCapacity(Int)](string/reservecapacity(_:).md)
  Reserves enough space in the string’s underlying storage to store the specified number of ASCII characters.
- [static func + (String, String) -> String](string/+(_:_:).md)
- [static func += (inout String, String)](string/+=(_:_:).md)
- [static func + <Other>(Other, Self) -> Self](string/+(_:_:)-6h59y.md)
  Creates a new collection by concatenating the elements of a sequence and a collection.
- [static func + <Other>(Self, Other) -> Self](string/+(_:_:)-n329.md)
  Creates a new collection by concatenating the elements of a collection and a sequence.
- [static func + <Other>(Self, Other) -> Self](string/+(_:_:)-9fm57.md)
  Creates a new collection by concatenating the elements of two collections.
- [static func += <Other>(inout Self, Other)](string/+=(_:_:)-676gx.md)
  Appends the elements of a sequence to a range-replaceable collection.
### Inserting Characters
- [func insert(Character, at: String.Index)](string/insert(_:at:).md)
  Inserts a new character at the specified position.
- [func insert(Self.Element, at: Self.Index)](string/insert(_:at:)-88yqh.md)
  Inserts a new element into the collection at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](string/insert(contentsof:at:)-rdu9.md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func insert<S>(contentsOf: S, at: String.Index)](string/insert(contentsof:at:).md)
  Inserts a collection of characters at the specified position.
### Replacing Substrings
- [func replaceSubrange<C>(Range<String.Index>, with: C)](string/replacesubrange(_:with:).md)
  Replaces the text within the specified bounds with the given characters.
- [func replaceSubrange<C, R>(R, with: C)](string/replacesubrange(_:with:)-72947.md)
  Replaces the specified subrange of elements with the given collection.
### Removing Substrings
- [func remove(at: String.Index) -> Character](string/remove(at:).md)
  Removes and returns the character at the specified position.
- [func remove(at: Self.Index) -> Self.Element](string/remove(at:)-5g0wm.md)
  Removes and returns the element at the specified position.
- [func removeAll(keepingCapacity: Bool)](string/removeall(keepingcapacity:).md)
  Replaces this string with the empty string.
- [func removeAll(where: (Self.Element) throws -> Bool) rethrows](string/removeall(where:).md)
  Removes all the elements that satisfy the given predicate.
- [func removeFirst() -> Self.Element](string/removefirst.md)
  Removes and returns the first element of the collection.
- [func removeFirst(Int)](string/removefirst(_:).md)
  Removes the specified number of elements from the beginning of the collection.
- [func removeLast() -> Self.Element](string/removelast.md)
  Removes and returns the last element of the collection.
- [func removeLast(Int)](string/removelast(_:).md)
  Removes the specified number of elements from the end of the collection.
- [func removeSubrange(Range<String.Index>)](string/removesubrange(_:).md)
  Removes the characters in the given range.
- [func removeSubrange(Range<Self.Index>)](string/removesubrange(_:)-8maxn.md)
  Removes the elements in the specified subrange from the collection.
- [func removeSubrange<R>(R)](string/removesubrange(_:)-9twng.md)
  Removes the elements in the specified subrange from the collection.
- [func filter((Self.Element) throws -> Bool) rethrows -> Self](string/filter(_:).md)
  Returns a new collection of the same type containing, in order, the elements of the original collection that satisfy the given predicate.
- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](string/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](string/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func dropLast(Int) -> Self.SubSequence](string/droplast(_:).md)
  Returns a subsequence containing all but the specified number of final elements.
- [func popLast() -> Self.Element?](string/poplast.md)
  Removes and returns the last element of the collection.
### Changing Case
- [func lowercased() -> String](string/lowercased.md)
  Returns a lowercase version of the string.
- [func uppercased() -> String](string/uppercased.md)
  Returns an uppercase version of the string.
### Comparing Strings Using Operators
- [static func == (String, String) -> Bool](string/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func == <RHS>(Self, RHS) -> Bool](string/==(_:_:)-8kzxf.md)
- [static func != (Self, Self) -> Bool](string/!=(_:_:)-1bb05.md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func != <RHS>(Self, RHS) -> Bool](string/!=(_:_:)-frzf.md)
- [static func ~= (String, Substring) -> Bool](string/~=(_:_:).md)
### Comparing Characters
- [func elementsEqual<OtherSequence>(OtherSequence) -> Bool](string/elementsequal(_:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [func elementsEqual<OtherSequence>(OtherSequence, by: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool](string/elementsequal(_:by:).md)
  Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [func starts<PossiblePrefix>(with: PossiblePrefix) -> Bool](string/starts(with:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [func starts<PossiblePrefix>(with: PossiblePrefix, by: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool](string/starts(with:by:).md)
  Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence) -> Bool](string/lexicographicallyprecedes(_:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [func lexicographicallyPrecedes<OtherSequence>(OtherSequence, by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Bool](string/lexicographicallyprecedes(_:by:).md)
  Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.
### Creating and Applying Differences
- [func applying(CollectionDifference<Self.Element>) -> Self?](string/applying(_:).md)
  Applies the given difference to this collection.
- [func difference<C>(from: C) -> CollectionDifference<Self.Element>](string/difference(from:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection.
- [func difference<C>(from: C, by: (C.Element, Self.Element) -> Bool) -> CollectionDifference<Self.Element>](string/difference(from:by:).md)
  Returns the difference needed to produce this collection’s ordered elements from the given collection, using the given predicate as an equivalence test.
### Finding Substrings
- [func hasPrefix(String) -> Bool](string/hasprefix(_:).md)
- [func hasSuffix(String) -> Bool](string/hassuffix(_:).md)
### Finding Characters
- [func contains(Self.Element) -> Bool](string/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](string/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](string/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func first(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](string/first(where:).md)
  Returns the first element of the sequence that satisfies the given predicate.
- [func firstIndex(of: Self.Element) -> Self.Index?](string/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](string/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](string/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](string/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](string/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func max() -> Self.Element?](string/max.md)
  Returns the maximum element in the sequence.
- [func max<T>(T, T) -> T](string/max(_:_:).md)
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](string/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.
- [func min() -> Self.Element?](string/min.md)
  Returns the minimum element in the sequence.
- [func min<T>(T, T) -> T](string/min(_:_:).md)
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](string/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
### Getting Substrings
- [subscript(Range<String.Index>) -> Substring](string/subscript(_:)-2so14.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript<R>(R) -> Self.SubSequence](string/subscript(_:)-4h7s3.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](string/subscript(_:)-4al9c.md)
- [func prefix(Int) -> Self.SubSequence](string/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](string/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](string/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](string/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(Int) -> Self.SubSequence](string/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](string/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
### Splitting a String
- [func split(separator: Self.Element, maxSplits: Int, omittingEmptySubsequences: Bool) -> [Self.SubSequence]](string/split(separator:maxsplits:omittingemptysubsequences:).md)
  Returns the longest possible subsequences of the collection, in order, around elements equal to the given element.
- [func split(maxSplits: Int, omittingEmptySubsequences: Bool, whereSeparator: (Self.Element) throws -> Bool) rethrows -> [Self.SubSequence]](string/split(maxsplits:omittingemptysubsequences:whereseparator:).md)
  Returns the longest possible subsequences of the collection, in order, that don’t contain elements satisfying the given predicate.
### Getting Characters and Bytes
- [subscript(String.Index) -> Character](string/subscript(_:)-lc0v.md)
  Accesses the character at the given position.
- [var first: Self.Element?](string/first.md)
  The first element of the collection.
- [var last: Self.Element?](string/last.md)
  The last element of the collection.
- [func randomElement() -> Self.Element?](string/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](string/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.
### Working with Encodings
- [static var availableStringEncodings: [String.Encoding]](string/availablestringencodings.md)
  An array of the encodings that strings support in the application’s environment.
- [static var defaultCStringEncoding: String.Encoding](string/defaultcstringencoding.md)
  The C-string encoding assumed for any method accepting a C string as an argument.
- [static func localizedName(of: String.Encoding) -> String](string/localizedname(of:).md)
  Returns a human-readable string giving the name of the specified encoding.
- [var isContiguousUTF8: Bool](string/iscontiguousutf8.md)
  Returns whether this string is capable of providing access to validly-encoded UTF-8 contents in contiguous memory in O(1) time.
- [func makeContiguousUTF8()](string/makecontiguousutf8.md)
  If this string is not contiguous, make it so. If this mutates the string, it will invalidate any pre-existing indices.
- [func withUTF8<R>((UnsafeBufferPointer<UInt8>) throws -> R) rethrows -> R](string/withutf8(_:).md)
  Runs `body` over the content of this string in contiguous memory. If this string is not contiguous, this will first make it contiguous, which will also speed up subsequent access. If this mutates the string, it will invalidate any pre-existing indices.
### Working with String Views
- [var unicodeScalars: String.UnicodeScalarView](string/unicodescalars.md)
  The string’s value represented as a collection of Unicode scalar values.
- [init(String.UnicodeScalarView)](string/init(_:)-2t931.md)
  Creates a string corresponding to the given collection of Unicode scalars.
- [init(Substring.UnicodeScalarView)](string/init(_:)-11jx3.md)
  Creates a String having the given content.
- [var utf16: String.UTF16View](string/utf16.md)
  A UTF-16 encoding of `self`.
- [init(String.UTF16View)](string/init(_:)-wbcx.md)
  Creates a string corresponding to the given sequence of UTF-16 code units.
- [init?(Substring.UTF16View)](string/init(_:)-expd.md)
  Creates a String having the given content.
- [var utf8: String.UTF8View](string/utf8.md)
  A UTF-8 encoding of `self`.
- [init(String.UTF8View)](string/init(_:)-6sprj.md)
  Creates a string corresponding to the given sequence of UTF-8 code units.
- [init?(Substring.UTF8View)](string/init(_:)-83bub.md)
  Creates a String having the given content.
### Transforming a String’s Characters
- [func compactMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](string/compactmap(_:).md)
  Returns an array containing the non-`nil` results of calling the given transformation with each element of this sequence.
- [func flatMap<SegmentOfResult>((Self.Element) throws -> SegmentOfResult) rethrows -> [SegmentOfResult.Element]](string/flatmap(_:)-i3m9.md)
  Returns an array containing the concatenated results of calling the given transformation with each element of this sequence.
- [func flatMap<ElementOfResult>((Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]](string/flatmap(_:)-6chuq.md)
- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](string/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [func reduce<Result>(into: Result, (inout Result, Self.Element) throws -> ()) rethrows -> Result](string/reduce(into:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.
- [var lazy: LazySequence<Self>](string/lazy.md)
  A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.
### Iterating over a String’s Characters
- [func forEach((Self.Element) throws -> Void) rethrows](string/foreach(_:).md)
  Calls the given closure on each element in the sequence in the same order as a `for`-`in` loop.
- [func enumerated() -> EnumeratedSequence<Self>](string/enumerated.md)
  Returns a sequence of pairs (, ), where  represents a consecutive integer starting at zero and  represents an element of the sequence.
- [func makeIterator() -> String.Iterator](string/makeiterator.md)
  Returns an iterator over the elements of the collection.
- [var underestimatedCount: Int](string/underestimatedcount.md)
  A value less than or equal to the number of elements in the collection.
### Reordering a String’s Characters
- [func sorted() -> [Self.Element]](string/sorted.md)
  Returns the elements of the sequence, sorted.
- [func sorted(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> [Self.Element]](string/sorted(by:).md)
  Returns the elements of the sequence, sorted using the given predicate as the comparison between elements.
- [func reversed() -> ReversedCollection<Self>](string/reversed.md)
  Returns a view presenting the elements of the collection in reverse order.
- [func shuffled() -> [Self.Element]](string/shuffled.md)
  Returns the elements of the sequence, shuffled.
- [func shuffled<T>(using: inout T) -> [Self.Element]](string/shuffled(using:).md)
  Returns the elements of the sequence, shuffled using the given generator as a source for randomness.
### Getting C Strings
- [var utf8CString: ContiguousArray<CChar>](string/utf8cstring.md)
  A contiguously stored null-terminated UTF-8 representation of the string.
- [func withCString<Result>((UnsafePointer<Int8>) throws -> Result) rethrows -> Result](string/withcstring(_:).md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of UTF-8 code units.
- [func withCString<Result, TargetEncoding>(encodedAs: TargetEncoding.Type, (UnsafePointer<TargetEncoding.CodeUnit>) throws -> Result) rethrows -> Result](string/withcstring(encodedas:_:).md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated sequence of code units.
### Working with Paths
- [init(FilePath)](string/init(_:)-3a5mh.md)
- [init?(validatingUTF8: FilePath)](string/init(validatingutf8:)-6i0in.md)
### Manipulating Indices
- [var startIndex: String.Index](string/startindex.md)
  The position of the first character in a nonempty string.
- [var endIndex: String.Index](string/endindex.md)
  A string’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [func index(after: String.Index) -> String.Index](string/index(after:).md)
  Returns the position immediately after the given index.
- [func formIndex(after: inout Self.Index)](string/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(before: String.Index) -> String.Index](string/index(before:).md)
  Returns the position immediately before the given index.
- [func formIndex(before: inout Self.Index)](string/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(String.Index, offsetBy: Int) -> String.Index](string/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(String.Index, offsetBy: Int, limitedBy: String.Index) -> String.Index?](string/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func formIndex(inout Self.Index, offsetBy: Int)](string/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](string/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func distance(from: String.Index, to: String.Index) -> Int](string/distance(from:to:).md)
  Returns the distance between two indices.
- [var indices: DefaultIndices<Self>](string/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.
### Creating a Range Expression
- [static func ... (Self, Self) -> ClosedRange<Self>](string/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
- [static func ... (Self) -> PartialRangeThrough<Self>](string/'...(_:)-4mm4o.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self) -> PartialRangeFrom<Self>](string/'...(_:)-6ct5g.md)
  Returns a partial range extending upward from a lower bound.
### Encoding and Decoding
- [func encode(to: any Encoder) throws](string/encode(to:).md)
  Encodes this value into the given encoder.
- [init(from: any Decoder) throws](string/init(from:)-qki5.md)
  Creates a new instance by decoding from the given decoder.
### Describing a String
- [var description: String](string/description.md)
  The value of this string.
- [var debugDescription: String](string/debugdescription.md)
  A representation of the string that is suitable for debugging.
- [var customMirror: Mirror](string/custommirror.md)
  A mirror that reflects the `String` instance.
- [var hashValue: Int](string/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](string/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Using a String as a Data Value
- [init?(from: MLDataValue)](string/init(from:)-gcys.md)
  Creates an instance of the conforming type from a data value.
- [var dataValue: MLDataValue](string/datavalue.md)
  The value of the conforming type’s instance wrapped in a data value.
- [var identifierValue: MLDataValue](string/identifiervalue.md)
  The value of the unique identifier wrapped in a data value.
- [static var dataValueType: MLDataValue.ValueType](string/datavaluetype.md)
  The underlying type the conforming type uses when it wraps itself in a data value.
### Infrequently Used Functionality
- [func index(of: Self.Element) -> Self.Index?](string/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [init(NSString)](string/init(_:)-5a5lw.md)
- [init(stringInterpolation: DefaultStringInterpolation)](string/init(stringinterpolation:).md)
  Creates a new instance from an interpolated string literal.
- [init(stringLiteral: String)](string/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
- [init(unicodeScalarLiteral: Self.ExtendedGraphemeClusterLiteralType)](string/init(unicodescalarliteral:).md)
- [init(extendedGraphemeClusterLiteral: Self.StringLiteralType)](string/init(extendedgraphemeclusterliteral:).md)
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](string/customplaygroundquicklook.md)
  A custom playground Quick Look for the `String` instance.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](string/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.
### Reference Types
- [class NSString](../Foundation/NSString.md)
  A static, plain-text Unicode string object.
- [class NSMutableString](../Foundation/NSMutableString.md)
  A dynamic plain-text Unicode string object.
### Related String Types
- [struct Substring](substring.md)
  A slice of a string.
- [protocol StringProtocol](stringprotocol.md)
  A type that can represent a string as a collection of characters.
- [String.Index](string/index.md)
  A position of a character or code unit in a string.
- [String.UnicodeScalarView](string/unicodescalarview.md)
  A view of a string’s contents as a collection of Unicode scalar values.
- [String.UTF16View](string/utf16view.md)
  A view of a string’s contents as a collection of UTF-16 code units.
- [String.UTF8View](string/utf8view.md)
  A view of a string’s contents as a collection of UTF-8 code units.
- [String.Iterator](string/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [String.Encoding](string/encoding.md)
### Structures
- [String.Comparator](string/comparator.md)
  A `String` comparison performed using the given comparison options and locale.
- [String.IntentInputOptions](string/intentinputoptions.md)
- [String.StandardComparator](string/standardcomparator.md)
  Compares `String`s using one of a fixed set of standard comparison algorithms.
### Initializers
- [init(URL.Template.VariableName)](string/init(_:)-1oup7.md)
- [init(Slice<AttributedString.CharacterView>)](string/init(_:)-5ruqx.md)
- [init(cString: inout CChar)](string/init(cstring:)-1gatt.md)
- [init(cString: inout UInt8)](string/init(cstring:)-295hy.md)
- [init(cString: [UInt8])](string/init(cstring:)-472zs.md)
  Creates a new string by copying the null-terminated UTF-8 data referenced by the given array.
- [init(cString: [CChar])](string/init(cstring:)-54awj.md)
  Creates a new string by copying the null-terminated UTF-8 data referenced by the given array.
- [init(cString: String)](string/init(cstring:)-cgw2.md)
- [init?(cString: inout CChar, encoding: String.Encoding)](string/init(cstring:encoding:)-358mb.md)
- [init?(cString: String, encoding: String.Encoding)](string/init(cstring:encoding:)-4ydt6.md)
- [init(copying: UTF8Span)](string/init(copying:).md)
- [init(decoding: FilePath.Root)](string/init(decoding:)-364r2.md)
  On Unix, creates the string `"/"`
- [init(decoding: FilePath.Component)](string/init(decoding:)-9xh58.md)
  Creates a string by interpreting the path component’s content as UTF-8 on Unix and UTF-16 on Windows.
- [init<Encoding>(decodingCString: String, as: Encoding.Type)](string/init(decodingcstring:as:)-2zmjc.md)
- [init<Encoding>(decodingCString: inout Encoding.CodeUnit, as: Encoding.Type)](string/init(decodingcstring:as:)-534rp.md)
- [init(describingForTest: some Any)](string/init(describingfortest:).md)
  Initialize this instance so that it can be presented in a test’s output.
- [init(platformString: String)](string/init(platformstring:)-341sr.md)
- [init(platformString: inout CInterop.PlatformChar)](string/init(platformstring:)-36ydz.md)
- [init(platformString: UnsafePointer<CInterop.PlatformChar>)](string/init(platformstring:)-5j2y3.md)
  Creates a string by interpreting the null-terminated platform string as UTF-8 on Unix and UTF-16 on Windows.
- [init(platformString: [CInterop.PlatformChar])](string/init(platformstring:)-7hjry.md)
  Creates a string by interpreting the null-terminated platform string as UTF-8 on Unix and UTF-16 on Windows.
- [init?(utf8String: String)](string/init(utf8string:)-5v4k8.md)
- [init?(utf8String: inout CChar)](string/init(utf8string:)-7t980.md)
- [init?(validating: FilePath.Root)](string/init(validating:)-6r2j9.md)
  On Unix, creates the string `"/"`
- [init?(validating: FilePath.Component)](string/init(validating:)-95n8b.md)
  Creates a string from a path component, validating its contents as UTF-8 on Unix and UTF-16 on Windows.
- [init?(validating: FilePath)](string/init(validating:)-9dx2b.md)
  Creates a string from a file path, validating its contents as UTF-8 on Unix and UTF-16 on Windows.
- [init?(validatingCString: inout CChar)](string/init(validatingcstring:)-1x5p0.md)
- [init?(validatingCString: String)](string/init(validatingcstring:)-7gjlg.md)
- [init?(validatingPlatformString: UnsafePointer<CInterop.PlatformChar>)](string/init(validatingplatformstring:)-2920w.md)
  Creates a string by interpreting the null-terminated platform string as UTF-8 on Unix and UTF-16 on Windows.
- [init?(validatingPlatformString: inout CInterop.PlatformChar)](string/init(validatingplatformstring:)-8x1kn.md)
- [init?(validatingPlatformString: [CInterop.PlatformChar])](string/init(validatingplatformstring:)-91z6f.md)
  Creates a string by interpreting the null-terminated platform string as UTF-8 on Unix and UTF-16 on Windows.
- [init?(validatingPlatformString: String)](string/init(validatingplatformstring:)-go44.md)
- [init?(validatingUTF8: [CChar])](string/init(validatingutf8:)-2m5lb.md)
  Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given array.
- [init?(validatingUTF8: inout CChar)](string/init(validatingutf8:)-2o7g5.md)
- [init?(validatingUTF8: String)](string/init(validatingutf8:)-8awk3.md)
### Instance Properties
- [var characters: String](string/characters.md)
  A view of the string’s contents as a collection of characters.
- [var utf8Span: UTF8Span](string/utf8span.md)
### Instance Methods
- [func data(using: String.Encoding, allowLossyConversion: Bool) -> Data?](string/data(using:allowlossyconversion:).md)
- [func withMutableCharacters<R>((inout String) -> R) -> R](string/withmutablecharacters(_:).md)
  Applies the given closure to a mutable view of the string’s characters.
- [func withPlatformString<Result>((UnsafePointer<CInterop.PlatformChar>) throws -> Result) rethrows -> Result](string/withplatformstring(_:).md)
  Calls the given closure with a pointer to the contents of the string, represented as a null-terminated platform string.
### Type Aliases
- [typealias CharacterView](string/characterview.md)
  A view of a string’s contents as a collection of characters.
- [typealias CompareOptions](string/compareoptions.md)
- [typealias EncodingConversionOptions](string/encodingconversionoptions.md)
- [typealias EnumerationOptions](string/enumerationoptions.md)
- [typealias IndexDistance](string/indexdistance.md)
  A type that represents the number of steps between two `String.Index` values, where one value is reachable from the other.
- [typealias Output](string/output.md)
- [typealias Specification](string/specification.md)
- [typealias UnicodeScalarIndex](string/unicodescalarindex.md)
  The index type for a string’s `unicodeScalars` view.
- [typealias UnwrappedType](string/unwrappedtype.md)
- [typealias ValueType](string/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](string/defaultresolverspecification.md)
### Type Methods
- [static func decodeCString<Encoding>(inout Encoding.CodeUnit, as: Encoding.Type, repairingInvalidCodeUnits: Bool) -> (result: String, repairsMade: Bool)?](string/decodecstring(_:as:repairinginvalidcodeunits:)-2l7u6.md)
- [static func decodeCString<Encoding>([Encoding.CodeUnit], as: Encoding.Type, repairingInvalidCodeUnits: Bool) -> (result: String, repairsMade: Bool)?](string/decodecstring(_:as:repairinginvalidcodeunits:)-3mvvy.md)
- [static func decodeCString<Encoding>(String, as: Encoding.Type, repairingInvalidCodeUnits: Bool) -> (result: String, repairsMade: Bool)?](string/decodecstring(_:as:repairinginvalidcodeunits:)-9pdmv.md)
### Default Implementations
- [Attachable Implementations](string/attachable-implementations.md)
- [BidirectionalCollection Implementations](string/bidirectionalcollection-implementations.md)
- [CodingKeyRepresentable Implementations](string/codingkeyrepresentable-implementations.md)
- [Collection Implementations](string/collection-implementations.md)
- [Comparable Implementations](string/comparable-implementations.md)
- [ConvertibleFromGeneratedContent Implementations](string/convertiblefromgeneratedcontent-implementations.md)
- [ConvertibleToGeneratedContent Implementations](string/convertibletogeneratedcontent-implementations.md)
- [CustomDebugStringConvertible Implementations](string/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](string/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](string/customstringconvertible-implementations.md)
- [CustomTestStringConvertible Implementations](string/customteststringconvertible-implementations.md)
- [CustomURLRepresentationParameterConvertible Implementations](string/customurlrepresentationparameterconvertible-implementations.md)
- [Decodable Implementations](string/decodable-implementations.md)
- [Encodable Implementations](string/encodable-implementations.md)
- [EntityIdentifierConvertible Implementations](string/entityidentifierconvertible-implementations.md)
- [Equatable Implementations](string/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](string/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringInterpolation Implementations](string/expressiblebystringinterpolation-implementations.md)
- [ExpressibleByStringLiteral Implementations](string/expressiblebystringliteral-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](string/expressiblebyunicodescalarliteral-implementations.md)
- [Generable Implementations](string/generable-implementations.md)
- [Hashable Implementations](string/hashable-implementations.md)
- [InstructionsRepresentable Implementations](string/instructionsrepresentable-implementations.md)
- [LosslessStringConvertible Implementations](string/losslessstringconvertible-implementations.md)
- [MLDataValueConvertible Implementations](string/mldatavalueconvertible-implementations.md)
- [MLIdentifier Implementations](string/mlidentifier-implementations.md)
- [PromptRepresentable Implementations](string/promptrepresentable-implementations.md)
- [RangeReplaceableCollection Implementations](string/rangereplaceablecollection-implementations.md)
- [RegexComponent Implementations](string/regexcomponent-implementations.md)
- [Sequence Implementations](string/sequence-implementations.md)
- [StringProtocol Implementations](string/stringprotocol-implementations.md)
- [TextOutputStream Implementations](string/textoutputstream-implementations.md)
- [TextOutputStreamable Implementations](string/textoutputstreamable-implementations.md)
- [Transferable Implementations](string/transferable-implementations.md)

## Relationships

### Conforms To
- [Attachable](../Testing/Attachable.md)
- [BidirectionalCollection](bidirectionalcollection.md)
- [BindableData](../RealityKit/BindableData.md)
- [CKRecordValueProtocol](../CloudKit/CKRecordValueProtocol.md)
- [CVarArg](cvararg.md)
- [CodingKeyRepresentable](codingkeyrepresentable.md)
- [Collection](collection.md)
- [Comparable](comparable.md)
- [ConvertibleFromGeneratedContent](../FoundationModels/ConvertibleFromGeneratedContent.md)
- [ConvertibleToGeneratedContent](../FoundationModels/ConvertibleToGeneratedContent.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [CustomTestStringConvertible](../Testing/CustomTestStringConvertible.md)
- [CustomURLRepresentationParameterConvertible](../AppIntents/CustomURLRepresentationParameterConvertible.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [EntityIdentifierConvertible](../AppIntents/EntityIdentifierConvertible.md)
- [Equatable](equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md)
- [ExpressibleByStringLiteral](expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md)
- [Generable](../FoundationModels/Generable.md)
- [Hashable](hashable.md)
- [InstructionsRepresentable](../FoundationModels/InstructionsRepresentable.md)
- [LosslessStringConvertible](losslessstringconvertible.md)
- [MLDataValueConvertible](../CreateML/MLDataValueConvertible.md)
- [MLIdentifier](../CreateML/MLIdentifier.md)
- [MirrorPath](mirrorpath.md)
- [MusicLibraryRequestFilterValueEquatable](../MusicKit/MusicLibraryRequestFilterValueEquatable.md)
- [PDFObjectType](../CoreGraphics/PDFObjectType.md)
- [Plottable](../Charts/Plottable.md)
- [PrimitivePlottableProtocol](../Charts/PrimitivePlottableProtocol.md)
- [PromptRepresentable](../FoundationModels/PromptRepresentable.md)
- [RangeReplaceableCollection](rangereplaceablecollection.md)
- [RegexComponent](regexcomponent.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [Sequence](sequence.md)
- [StringProtocol](stringprotocol.md)
- [TextOutputStream](textoutputstream.md)
- [TextOutputStreamable](textoutputstreamable.md)
- [Transferable](../CoreTransferable/Transferable.md)

## See Also

- [struct Int](int.md)
  A signed integer value type.
- [struct Double](double.md)
  A double-precision, floating-point value type.
- [struct Array](array.md)
  An ordered, random-access collection.
- [struct Dictionary](dictionary.md)
  A collection whose elements are key-value pairs.
- [Swift Standard Library](swift-standard-library.md)
  Solve complex problems and write high-performance, readable code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string)*