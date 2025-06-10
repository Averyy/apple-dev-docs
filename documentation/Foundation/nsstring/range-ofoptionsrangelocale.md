# range(of:options:range:locale:)

**Framework**: Foundation  
**Kind**: method

Finds and returns the range of the first occurrence of a given string within a given range of the string, subject to given options, using the specified locale, if any.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func range(of searchString: String, options mask: NSString.CompareOptions = [], range rangeOfReceiverToSearch: NSRange, locale: Locale?) -> NSRange
```

#### Return Value

An [`NSRange`](nsrange-c.struct.md) structure giving the location and length in the receiver of `aString` within `aRange` in the receiver, modulo the options in `mask`. The range returned is relative to the start of the string, not to the passed-in range. Returns `{``NSNotFound``, 0}` if `aString` is not found or is empty (`""`).

#### Discussion

`NSString` objects are compared by checking the Unicode canonical equivalence of their code point sequences.  The length of the returned range and that of `aString` may differ if equivalent composed character sequences are matched.

> ❗ **Important**:  When working with text that’s presented to the user, use the [`localizedStandardRange(of:)`](nsstring/localizedstandardrange(of:).md) method instead.

##### Special Considerations

This method detects all invalid ranges (including those with negative lengths). For applications linked against macOS 10.6 and later, this error causes an exception; for applications linked against earlier releases, this error causes a warning, which is displayed just once per application execution.

## Parameters

- `searchString`: The string for which to search.
- `mask`: A mask specifying search options. The following options may be specified by combining them with the C bitwise   operator:  ,  ,  , and  . See   for details on these options.
- `rangeOfReceiverToSearch`: Raises an   if   is invalid.
- `locale`: The locale argument affects the equality checking algorithm. For example, for the Turkish locale, case-insensitive compare matches “I” to “ı” ( ), not the normal “i” character.

## See Also

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
- [func localizedStandardRange(of: String) -> NSRange](nsstring/localizedstandardrange(of:).md)
  Finds and returns the range of the first occurrence of a given string within the string by performing a case and diacritic insensitive, locale-aware search.
- [func enumerateLines((String, UnsafeMutablePointer<ObjCBool>) -> Void)](nsstring/enumeratelines(_:).md)
  Enumerates all the lines in the string.
- [func enumerateSubstrings(in: NSRange, options: NSString.EnumerationOptions, using: (String?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nsstring/enumeratesubstrings(in:options:using:).md)
  Enumerates the substrings of the specified type in the specified range of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/range(of:options:range:locale:))*