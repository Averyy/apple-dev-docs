# enumerateSubstrings(in:options:using:)

**Framework**: Foundation  
**Kind**: method

Enumerates the substrings of the specified type in the specified range of the string.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func enumerateSubstrings(in range: NSRange, options opts: NSString.EnumerationOptions = [], using block: @escaping (String?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

If this method is sent to an instance of `NSMutableString`, mutation (deletion, addition, or change) is allowed, as long as it is within `enclosingRange`. After a mutation, the enumeration continues with the range immediately following the processed range, after the length of the processed range is adjusted for the mutation. (The enumerator assumes any change in length occurs in the specified range.)

For example, if the block is called with a range starting at location N, and the block deletes all the characters in the supplied range, the next call will also pass N as the index of the range. This is the case even if mutation of the previous range changes the string in such a way that the following substring would have extended to include the already enumerated range. For example, if the string “Hello World” is enumerated via words, and the block changes “Hello “ to “Hello”, thus forming “HelloWorld”, the next enumeration will return “World” rather than “HelloWorld”.

## Parameters

- `range`: The range within the string to enumerate substrings.
- `opts`: Options specifying types of substrings and enumeration styles.
- `block`: The block takes four arguments:

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
- [func range(of: String, options: NSString.CompareOptions, range: NSRange, locale: Locale?) -> NSRange](nsstring/range(of:options:range:locale:).md)
  Finds and returns the range of the first occurrence of a given string within a given range of the string, subject to given options, using the specified locale, if any.
- [func localizedStandardRange(of: String) -> NSRange](nsstring/localizedstandardrange(of:).md)
  Finds and returns the range of the first occurrence of a given string within the string by performing a case and diacritic insensitive, locale-aware search.
- [func enumerateLines((String, UnsafeMutablePointer<ObjCBool>) -> Void)](nsstring/enumeratelines(_:).md)
  Enumerates all the lines in the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/enumeratesubstrings(in:options:using:))*