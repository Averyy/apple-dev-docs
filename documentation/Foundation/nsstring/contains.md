# contains(_:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether the string contains a given string by performing a case-sensitive, locale-unaware search.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func contains(_ str: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver contains `str`, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Calling this method is equivalent to calling [`range(of:options:)`](nsstring/range(of:options:).md) with no options.

> ❗ **Important**:  When working with text that’s presented to the user, use [`localizedStandardContains(_:)`](nsstring/localizedstandardcontains(_:).md) or [`localizedCaseInsensitiveContains(_:)`](nsstring/localizedcaseinsensitivecontains(_:).md) instead.

## Parameters

- `str`: The string to search for. This value must not be  .

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/contains(_:))*