# range(of:options:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Finds and returns the range of the first occurrence of a given string within the string, subject to given options.

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
func range(of searchString: String, options mask: NSString.CompareOptions = []) -> NSRange
```

```objc
- (NSRange) rangeOfString:(NSString *) searchString options:(NSStringCompareOptions) mask;
```

## Return Value

An `NSRange` structure giving the location and length in the receiver of the first occurrence of

## Discussion

`searchString`,

modulo the options in `mask`. Returns `{``NSNotFound``, 0}` if

`searchString`

is not found or is empty (`""`).

## Discussion

Invokes [`range(of:options:range:)`](./range%28of,options,range%29.md) with the options specified by `mask` and the entire extent of the receiver as the range.

`NSString` objects are compared by checking the Unicode canonical equivalence of their code point sequences.  The length of the returned range and that of

`searchString`

may differ if equivalent composed character sequences are matched.

> ❗ **Important**:  When working with text that’s presented to the user, use the [`localizedStandardRange(of:)`](./localizedstandardrange%28of%29.md) method instead.

## Parameters

- `searchString`: The string to search for.
- `mask`: A mask specifying search options. For possible values, see [`NSString.CompareOptions`](./compareoptions.md).

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
- [func rangeOfCharacter(from: CharacterSet, options: NSString.CompareOptions, range: NSRange) -> NSRange](./rangeofcharacter%28from,options,range%29.md)
  Finds and returns the range in the string of the first character from a given character set found in a given range with given options.
- [func range(of: String) -> NSRange](./range%28of%29.md)
  Finds and returns the range of the first occurrence of a given string within the string.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/range(of:options:))*