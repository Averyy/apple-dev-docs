# CFString

**Framework**: Core Foundation  
**Kind**: class

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CFString
```

#### Overview

CFString provides a suite of efficient string-manipulation and string-conversion functions. It offers seamless Unicode support and facilitates the sharing of data between Cocoa and C-based programs. CFString objects are immutable—use [`CFMutableString`](cfmutablestring.md) to create and manage a string that can be changed after it has been created.

CFString has two primitive functions, [`CFStringGetLength(_:)`](cfstringgetlength(_:).md) and [`CFStringGetCharacterAtIndex(_:_:)`](cfstringgetcharacteratindex(_:_:).md), that provide the basis for all other functions in its interface. The `CFStringGetLength` function returns the total number (in terms of UTF-16 code pairs) of characters in the string. The `CFStringGetCharacterAtIndex` function gives access to each character in the string by index, with index values starting at `0`.

CFString provides functions for finding and comparing strings. It also provides functions for reading numeric values from strings, for combining strings in various ways, and for converting a string to different forms (such as encoding and case changes). A number of functions, for example `CFStringFindWithOptions`, allow you to specify a range over which to operate within a string. The specified range must not exceed the length of the string. Debugging options may help you to catch any errors that arise if a range does exceed a string’s length.

Like other Core Foundation types, you can hash CFStrings using the [`CFHash(_:)`](cfhash(_:).md) function. You should never, though, store a hash value outside of your application and expect it to be useful if you read it back in later (hash values may change between different releases of the operating system).

CFString is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSString`](https://developer.apple.com/documentation/Foundation/NSString). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSString *` parameter, you can pass in a `CFStringRef`, and in a function where you see a `CFStringRef` parameter, you can pass in an NSString instance. This also applies to concrete subclasses of NSString. See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating a CFString
- [func CFStringCreateArrayBySeparatingStrings(CFAllocator!, CFString!, CFString!) -> CFArray!](cfstringcreatearraybyseparatingstrings(_:_:_:).md)
  Creates an array of CFString objects from a single CFString object.
- [func CFStringCreateByCombiningStrings(CFAllocator!, CFArray!, CFString!) -> CFString!](cfstringcreatebycombiningstrings(_:_:_:).md)
  Creates a single string from the individual CFString objects that comprise the elements of an array.
- [func CFStringCreateCopy(CFAllocator!, CFString!) -> CFString!](cfstringcreatecopy(_:_:).md)
  Creates an immutable copy of a string.
- [func CFStringCreateFromExternalRepresentation(CFAllocator!, CFData!, CFStringEncoding) -> CFString!](cfstringcreatefromexternalrepresentation(_:_:_:).md)
  Creates a string from its “external representation.”
- [func CFStringCreateWithBytes(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFStringEncoding, Bool) -> CFString!](cfstringcreatewithbytes(_:_:_:_:_:).md)
  Creates a string from a buffer containing characters in a specified encoding.
- [func CFStringCreateWithBytesNoCopy(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFStringEncoding, Bool, CFAllocator!) -> CFString!](cfstringcreatewithbytesnocopy(_:_:_:_:_:_:).md)
  Creates a string from a buffer, containing characters in a specified encoding, that might serve as the backing store for the new string.
- [func CFStringCreateWithCharacters(CFAllocator!, UnsafePointer<UniChar>!, CFIndex) -> CFString!](cfstringcreatewithcharacters(_:_:_:).md)
  Creates a string from a buffer of Unicode characters.
- [func CFStringCreateWithCharactersNoCopy(CFAllocator!, UnsafePointer<UniChar>!, CFIndex, CFAllocator!) -> CFString!](cfstringcreatewithcharactersnocopy(_:_:_:_:).md)
  Creates a string from a buffer of Unicode characters that might serve as the backing store for the object.
- [func CFStringCreateWithCString(CFAllocator!, UnsafePointer<CChar>!, CFStringEncoding) -> CFString!](cfstringcreatewithcstring(_:_:_:).md)
  Creates an immutable string from a C string.
- [func CFStringCreateWithCStringNoCopy(CFAllocator!, UnsafePointer<CChar>!, CFStringEncoding, CFAllocator!) -> CFString!](cfstringcreatewithcstringnocopy(_:_:_:_:).md)
  Creates a CFString object from an external C string buffer that might serve as the backing store for the object.
- [func CFStringCreateWithFormatAndArguments(CFAllocator!, CFDictionary!, CFString!, CVaListPointer) -> CFString!](cfstringcreatewithformatandarguments(_:_:_:_:).md)
  Creates an immutable string from a formatted string and a variable number of arguments (specified in a parameter of type `va_list`).
- [func CFStringCreateWithPascalString(CFAllocator!, ConstStr255Param!, CFStringEncoding) -> CFString!](cfstringcreatewithpascalstring(_:_:_:).md)
  Creates an immutable CFString object from a Pascal string.
- [func CFStringCreateWithPascalStringNoCopy(CFAllocator!, ConstStr255Param!, CFStringEncoding, CFAllocator!) -> CFString!](cfstringcreatewithpascalstringnocopy(_:_:_:_:).md)
  Creates a CFString object from an external Pascal string buffer that might serve as the backing store for the object.
- [func CFStringCreateWithSubstring(CFAllocator!, CFString!, CFRange) -> CFString!](cfstringcreatewithsubstring(_:_:_:).md)
  Creates an immutable string from a segment (substring) of an existing string.
### Searching Strings
- [func CFStringCreateArrayWithFindResults(CFAllocator!, CFString!, CFString!, CFRange, CFStringCompareFlags) -> CFArray!](cfstringcreatearraywithfindresults(_:_:_:_:_:).md)
  Searches a string for multiple occurrences of a substring and creates an array of ranges identifying the locations of these substrings within the target string.
- [func CFStringFind(CFString!, CFString!, CFStringCompareFlags) -> CFRange](cfstringfind(_:_:_:).md)
  Searches for a substring within a string and, if it is found, yields the range of the substring within the object’s characters.
- [func CFStringFindCharacterFromSet(CFString!, CFCharacterSet!, CFRange, CFStringCompareFlags, UnsafeMutablePointer<CFRange>!) -> Bool](cfstringfindcharacterfromset(_:_:_:_:_:).md)
  Query the range of the first character contained in the specified character set.
- [func CFStringFindWithOptions(CFString!, CFString!, CFRange, CFStringCompareFlags, UnsafeMutablePointer<CFRange>!) -> Bool](cfstringfindwithoptions(_:_:_:_:_:).md)
  Searches for a substring within a range of the characters represented by a string and, if the substring is found, returns its range within the object’s characters.
- [func CFStringFindWithOptionsAndLocale(CFString!, CFString!, CFRange, CFStringCompareFlags, CFLocale!, UnsafeMutablePointer<CFRange>!) -> Bool](cfstringfindwithoptionsandlocale(_:_:_:_:_:_:).md)
  Returns a Boolean value that indicates whether a given string was found in a given source string.
- [func CFStringGetLineBounds(CFString!, CFRange, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!)](cfstringgetlinebounds(_:_:_:_:_:).md)
  Given a range of characters in a string, obtains the line bounds—that is, the indexes of the first character and the final characters of the lines containing the range.
### Comparing Strings
- [func CFStringCompare(CFString!, CFString!, CFStringCompareFlags) -> CFComparisonResult](cfstringcompare(_:_:_:).md)
  Compares one string with another string.
- [func CFStringCompareWithOptions(CFString!, CFString!, CFRange, CFStringCompareFlags) -> CFComparisonResult](cfstringcomparewithoptions(_:_:_:_:).md)
  Compares a range of the characters in one string with that of another string.
- [func CFStringCompareWithOptionsAndLocale(CFString!, CFString!, CFRange, CFStringCompareFlags, CFLocale!) -> CFComparisonResult](cfstringcomparewithoptionsandlocale(_:_:_:_:_:).md)
  Compares a range of the characters in one string with another string using a given locale.
- [func CFStringHasPrefix(CFString!, CFString!) -> Bool](cfstringhasprefix(_:_:).md)
  Determines if the character data of a string begin with a specified sequence of characters.
- [func CFStringHasSuffix(CFString!, CFString!) -> Bool](cfstringhassuffix(_:_:).md)
  Determines if a string ends with a specified sequence of characters.
### Accessing Characters
- [func CFStringCreateExternalRepresentation(CFAllocator!, CFString!, CFStringEncoding, UInt8) -> CFData!](cfstringcreateexternalrepresentation(_:_:_:_:).md)
  Creates an “external representation” of a CFString object, that is, a CFData object.
- [func CFStringGetBytes(CFString!, CFRange, CFStringEncoding, UInt8, Bool, UnsafeMutablePointer<UInt8>!, CFIndex, UnsafeMutablePointer<CFIndex>!) -> CFIndex](cfstringgetbytes(_:_:_:_:_:_:_:_:).md)
  Fetches a range of the characters from a string into a byte buffer after converting the characters to a specified encoding.
- [func CFStringGetCharacterAtIndex(CFString!, CFIndex) -> UniChar](cfstringgetcharacteratindex(_:_:).md)
  Returns the Unicode character at a specified location in a string.
- [func CFStringGetCharacters(CFString!, CFRange, UnsafeMutablePointer<UniChar>!)](cfstringgetcharacters(_:_:_:).md)
  Copies a range of the Unicode characters from a string to a user-provided buffer.
- [func CFStringGetCharactersPtr(CFString!) -> UnsafePointer<UniChar>!](cfstringgetcharactersptr(_:).md)
  Quickly obtains a pointer to the contents of a string as a buffer of Unicode characters.
- [func CFStringGetCharacterFromInlineBuffer(UnsafeMutablePointer<CFStringInlineBuffer>!, CFIndex) -> UniChar](cfstringgetcharacterfrominlinebuffer(_:_:).md)
  Returns the Unicode character at a specific location in an in-line buffer.
- [func CFStringGetCString(CFString!, UnsafeMutablePointer<CChar>!, CFIndex, CFStringEncoding) -> Bool](cfstringgetcstring(_:_:_:_:).md)
  Copies the character contents of a string to a local C string buffer after converting the characters to a given encoding.
- [func CFStringGetCStringPtr(CFString!, CFStringEncoding) -> UnsafePointer<CChar>!](cfstringgetcstringptr(_:_:).md)
  Quickly obtains a pointer to a C-string buffer containing the characters of a string in a given encoding.
- [func CFStringGetLength(CFString!) -> CFIndex](cfstringgetlength(_:).md)
  Returns the number (in terms of UTF-16 code pairs) of Unicode characters in a string.
- [func CFStringGetPascalString(CFString!, StringPtr!, CFIndex, CFStringEncoding) -> Bool](cfstringgetpascalstring(_:_:_:_:).md)
  Copies the character contents of a CFString object to a local Pascal string buffer after converting the characters to a requested encoding.
- [func CFStringGetPascalStringPtr(CFString!, CFStringEncoding) -> ConstStringPtr!](cfstringgetpascalstringptr(_:_:).md)
  Quickly obtains a pointer to a Pascal buffer containing the characters of a string in a given encoding.
- [func CFStringGetRangeOfComposedCharactersAtIndex(CFString!, CFIndex) -> CFRange](cfstringgetrangeofcomposedcharactersatindex(_:_:).md)
  Returns the range of the composed character sequence at a specified index.
- [func CFStringInitInlineBuffer(CFString!, UnsafeMutablePointer<CFStringInlineBuffer>!, CFRange)](cfstringinitinlinebuffer(_:_:_:).md)
  Initializes an in-line buffer to use for efficient access of a CFString object’s characters.
### Working With Hyphenation
- [func CFStringGetHyphenationLocationBeforeIndex(CFString!, CFIndex, CFRange, CFOptionFlags, CFLocale!, UnsafeMutablePointer<UTF32Char>!) -> CFIndex](cfstringgethyphenationlocationbeforeindex(_:_:_:_:_:_:).md)
  Retrieve the first potential hyphenation location found before the specified location.
- [func CFStringIsHyphenationAvailableForLocale(CFLocale!) -> Bool](cfstringishyphenationavailableforlocale(_:).md)
  Returns a Boolean value that indicates whether hyphenation data is available.
### Working With Encodings
- [func CFStringConvertEncodingToIANACharSetName(CFStringEncoding) -> CFString!](cfstringconvertencodingtoianacharsetname(_:).md)
  Returns the name of the IANA registry “charset” that is the closest mapping to a specified string encoding.
- [func CFStringConvertEncodingToNSStringEncoding(CFStringEncoding) -> UInt](cfstringconvertencodingtonsstringencoding(_:).md)
  Returns the Cocoa encoding constant that maps most closely to a given Core Foundation encoding constant.
- [func CFStringConvertEncodingToWindowsCodepage(CFStringEncoding) -> UInt32](cfstringconvertencodingtowindowscodepage(_:).md)
  Returns the Windows codepage identifier that maps most closely to a given Core Foundation encoding constant.
- [func CFStringConvertIANACharSetNameToEncoding(CFString!) -> CFStringEncoding](cfstringconvertianacharsetnametoencoding(_:).md)
  Returns the Core Foundation encoding constant that is the closest mapping to a given IANA registry “charset” name.
- [func CFStringConvertNSStringEncodingToEncoding(UInt) -> CFStringEncoding](cfstringconvertnsstringencodingtoencoding(_:).md)
  Returns the Core Foundation encoding constant that is the closest mapping to a given Cocoa encoding.
- [func CFStringConvertWindowsCodepageToEncoding(UInt32) -> CFStringEncoding](cfstringconvertwindowscodepagetoencoding(_:).md)
  Returns the Core Foundation encoding constant that is the closest mapping to a given Windows codepage identifier.
- [func CFStringGetFastestEncoding(CFString!) -> CFStringEncoding](cfstringgetfastestencoding(_:).md)
  Returns for a CFString object the character encoding that requires the least conversion time.
- [func CFStringGetListOfAvailableEncodings() -> UnsafePointer<CFStringEncoding>!](cfstringgetlistofavailableencodings().md)
  Returns a pointer to a list of string encodings supported by the current system.
- [func CFStringGetMaximumSizeForEncoding(CFIndex, CFStringEncoding) -> CFIndex](cfstringgetmaximumsizeforencoding(_:_:).md)
  Returns the maximum number of bytes a string of a specified length (in Unicode characters) will take up if encoded in a specified encoding.
- [func CFStringGetMostCompatibleMacStringEncoding(CFStringEncoding) -> CFStringEncoding](cfstringgetmostcompatiblemacstringencoding(_:).md)
  Returns the most compatible Mac OS script value for the given input encoding.
- [func CFStringGetNameOfEncoding(CFStringEncoding) -> CFString!](cfstringgetnameofencoding(_:).md)
  Returns the canonical name of a specified string encoding.
- [func CFStringGetSmallestEncoding(CFString!) -> CFStringEncoding](cfstringgetsmallestencoding(_:).md)
  Returns the smallest encoding on the current system for the character contents of a string.
- [func CFStringGetSystemEncoding() -> CFStringEncoding](cfstringgetsystemencoding().md)
  Returns the default encoding used by the operating system when it creates strings.
- [func CFStringIsEncodingAvailable(CFStringEncoding) -> Bool](cfstringisencodingavailable(_:).md)
  Determines whether a given Core Foundation string encoding is available on the current system.
### Getting Numeric Values
- [func CFStringGetDoubleValue(CFString!) -> Double](cfstringgetdoublevalue(_:).md)
  Returns the primary `double` value represented by a string.
- [func CFStringGetIntValue(CFString!) -> Int32](cfstringgetintvalue(_:).md)
  Returns the integer value represented by a string.
### Getting String Properties
- [func CFShowStr(CFString!)](cfshowstr(_:).md)
  Prints the attributes of a string during debugging.
- [func CFStringGetTypeID() -> CFTypeID](cfstringgettypeid().md)
  Returns the type identifier for the CFString opaque type.
### String File System Representations
- [func CFStringCreateWithFileSystemRepresentation(CFAllocator!, UnsafePointer<CChar>!) -> CFString!](cfstringcreatewithfilesystemrepresentation(_:_:).md)
  Creates a CFString from a zero-terminated POSIX file system representation.
- [func CFStringGetFileSystemRepresentation(CFString!, UnsafeMutablePointer<CChar>!, CFIndex) -> Bool](cfstringgetfilesystemrepresentation(_:_:_:).md)
  Extracts the contents of a string as a `NULL`-terminated 8-bit string appropriate for passing to POSIX APIs.
- [func CFStringGetMaximumSizeOfFileSystemRepresentation(CFString!) -> CFIndex](cfstringgetmaximumsizeoffilesystemrepresentation(_:).md)
  Determines the upper bound on the number of bytes required to hold the file system representation of the string.
### Getting Paragraph Bounds
- [func CFStringGetParagraphBounds(CFString!, CFRange, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!, UnsafeMutablePointer<CFIndex>!)](cfstringgetparagraphbounds(_:_:_:_:_:).md)
  Given a range of characters in a string, obtains the paragraph bounds—that is, the indexes of the first character and the final characters of the paragraph(s) containing the range.
### Managing Surrogates
- [func CFStringGetLongCharacterForSurrogatePair(UniChar, UniChar) -> UTF32Char](cfstringgetlongcharacterforsurrogatepair(_:_:).md)
  Returns a UTF-32 character that corresponds to a given pair of UTF-16 surrogate characters.
- [func CFStringGetSurrogatePairForLongCharacter(UTF32Char, UnsafeMutablePointer<UniChar>!) -> Bool](cfstringgetsurrogatepairforlongcharacter(_:_:).md)
  Maps a given UTF-32 character to a pair of UTF-16 surrogate characters.
- [func CFStringIsSurrogateHighCharacter(UniChar) -> Bool](cfstringissurrogatehighcharacter(_:).md)
  Returns a Boolean value that indicates whether a given character is a high character in a surrogate pair.
- [func CFStringIsSurrogateLowCharacter(UniChar) -> Bool](cfstringissurrogatelowcharacter(_:).md)
  Returns a Boolean value that indicates whether a given character is a low character in a surrogate pair.
### Data Types
- [typealias CFStringEncoding](cfstringencoding.md)
  An integer type for constants used to specify supported string encodings in various CFString functions.
- [enum CFStringEncodings](cfstringencodings.md)
  Index type for constants used to specify external string encodings.
- [struct CFStringCompareFlags](cfstringcompareflags.md)
  A [`CFOptionFlags`](cfoptionflags.md) type for specifying options for string comparison .
- [struct CFStringInlineBuffer](cfstringinlinebuffer.md)
  Defines the buffer and related fields used for in-line buffer access of characters in CFString objects.
### Constants
- [String Comparison Flags](string-comparison-flags.md)
  Flags that specify how string comparisons are performed.
- [enum CFStringBuiltInEncodings](cfstringbuiltinencodings.md)
  Encodings that are built-in on all platforms on which macOS runs.
- [Invalid String Encoding Flag](invalid-string-encoding-flag.md)
  Special value returned from functions to indicate a string encoding that is not supported or recognized by CFString.
- [External String Encodings](external-string-encodings.md)
  `CFStringEncoding` constants for encodings that may be supported by CFString.

## Relationships

### Inherited By
- [CFMutableString](cfmutablestring.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Property List Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [Data Formatting Guide for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDataFormatting/Articles/CFDataFormatting.html#//apple_ref/doc/uid/10000176i)
- [String Programming Guide for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstring)*