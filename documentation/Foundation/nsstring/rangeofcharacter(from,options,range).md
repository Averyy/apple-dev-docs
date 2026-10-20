# rangeOfCharacter(from:options:range:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Finds and returns the range in the string of the first character from a given character set found in a given range with given options.

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
func rangeOfCharacter(from searchSet: CharacterSet, options mask: NSString.CompareOptions = [], range rangeOfReceiverToSearch: NSRange) -> NSRange
```

```objc
- (NSRange) rangeOfCharacterFromSet:(NSCharacterSet *) searchSet options:(NSStringCompareOptions) mask range:(NSRange) rangeOfReceiverToSearch;
```

#### Return Value

The range in the receiver of the first character found from `aSet` within `aRange`. Returns a range of `{``NSNotFound``, 0}` if none of the characters in `aSet` are found.

#### Discussion

This method does not perform any Unicode normalization on the receiver, so canonically equivalent forms will not be matched. For example, searching the string “strüdel”—containing the decomposed characters “`u`” (`U+0075 LATIN SMALL LETTER U`) and “`¨`” (`U+0308 COMBINING DIAERESIS`)—with a character set containing the precomposed character “`ü`” (`U+00FC LATIN SMALL LETTER U WITH DIAERESIS`) would return the range `{``NSNotFound``, 0}`, because none of the characters in the set are found.

## Parameters

- `searchSet`: A character set. This value must not be `nil`.

  Raises an `NSInvalidArgumentException` if `aSet` is `nil`.
- `mask`: A mask specifying search options. The following options may be specified by combining them with the C bitwise `OR` operator: [`anchored`](./compareoptions/anchored.md), [`backwards`](./compareoptions/backwards.md).
- `rangeOfReceiverToSearch`: The range in which to search. `aRange` must not exceed the bounds of the receiver.

  Raises an [`rangeException`](../nsexceptionname/rangeexception.md) if `aRange` is invalid.

## See Also

### Finding Characters and Substrings
- [func contains(String) -> Bool](./contains%28_%29.md)
  Returns a Boolean value indicating whether the string contains a given string by performing a case-sensitive, locale-unaware search.
- [func localizedCaseInsensitiveContains(String) -> Bool](./localizedcaseinsensitivecontains%28_%29.md)
  Returns a Boolean value indicating whether the string contains a given string by performing a case-insensitive, locale-aware search.
- [func localizedStandardContains(String) -> Bool](./localizedstandardcontains%28_%29.md)
  Returns a Boolean value indicating whether the string contains a given string by performing a case and diacritic insensitive, locale-aware search.
- [func rangeOfCharacter(from: CharacterSet) -> NSRange](./rangeofcharacter%28from%29.md)
  Finds and returns the range in the string of the first character from a given character set.
- [func rangeOfCharacter(from: CharacterSet, options: NSString.CompareOptions) -> NSRange](./rangeofcharacter%28from,options%29.md)
  Finds and returns the range in the string of the first character, using given options, from a given character set.
- [func range(of: String) -> NSRange](./range%28of%29.md)
  Finds and returns the range of the first occurrence of a given string within the string.
- [func range(of: String, options: NSString.CompareOptions) -> NSRange](./range%28of,options%29.md)
  Finds and returns the range of the first occurrence of a given string within the string, subject to given options.
- [func range(of: String, options: NSString.CompareOptions, range: NSRange) -> NSRange](./range%28of,options,range%29.md)
  Finds and returns the range of the first occurrence of a given string, within the given range of the string, subject to given options.
- [func range(of: String, options: NSString.CompareOptions, range: NSRange, locale: Locale?) -> NSRange](./range%28of,options,range,locale%29.md)
  Finds and returns the range of the first occurrence of a given string within a given range of the string, subject to given options, using the specified locale, if any.
- [func localizedStandardRange(of: String) -> NSRange](./localizedstandardrange%28of%29.md)
  Finds and returns the range of the first occurrence of a given string within the string by performing a case and diacritic insensitive, locale-aware search.
- [func enumerateLines((String, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratelines%28_%29.md)
  Enumerates all the lines in the string.
- [func enumerateSubstrings(in: NSRange, options: NSString.EnumerationOptions, using: (String?, NSRange, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratesubstrings%28in,options,using%29.md)
  Enumerates the substrings of the specified type in the specified range of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/rangeofcharacter(from:options:range:))*