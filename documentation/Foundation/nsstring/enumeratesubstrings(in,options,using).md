# enumerateSubstrings(in:options:using:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) enumerateSubstringsInRange:(NSRange) range options:(NSStringEnumerationOptions) opts usingBlock:(void (^)(NSString *substring, NSRange substringRange, NSRange enclosingRange, BOOL *stop)) block;
```

## Discussion

If this method is sent to an instance of `NSMutableString`, mutation (deletion, addition, or change) is allowed, as long as it is within `enclosingRange`. After a mutation, the enumeration continues with the range immediately following the processed range, after the length of the processed range is adjusted for the mutation. (The enumerator assumes any change in length occurs in the specified range.)

For example, if the block is called with a range starting at location N, and the block deletes all the characters in the supplied range, the next call will also pass N as the index of the range. This is the case even if mutation of the previous range changes the string in such a way that the following substring would have extended to include the already enumerated range. For example, if the string “Hello World” is enumerated via words, and the block changes “Hello “ to “Hello”, thus forming “HelloWorld”, the next enumeration will return “World” rather than “HelloWorld”.

## Parameters

- `range`: The range within the string to enumerate substrings.
- `opts`: Options specifying types of substrings and enumeration styles.
- `block`: The block executed for the enumeration.

  The block takes four arguments:

  - **substring**: The enumerated string.
  - **substringRange**: The range of the enumerated string in the receiver.
  - **enclosingRange**: The range that includes the substring as well as any separator or filler characters that follow. For instance, for lines, `enclosingRange` contains the line terminators. The `enclosingRange` for the first string enumerated also contains any characters that occur before the string. Consecutive enclosing ranges are guaranteed not to overlap, and every single character in the enumerated range is included in one and only one enclosing range.
  - **stop**: A reference to a Boolean value that the block can use to stop the enumeration by setting `*stop = YES`; it should not touch `*stop` otherwise.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/enumeratesubstrings(in:options:using:))*