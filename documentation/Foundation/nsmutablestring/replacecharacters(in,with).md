# replaceCharacters(in:with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Replaces the characters from `range` with those in `aString`.

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
func replaceCharacters(in range: NSRange, with aString: String)
```

```objc
- (void) replaceCharactersInRange:(NSRange) range withString:(NSString *) aString;
```

## Discussion

This method treats the length of the string as a valid range value that returns an empty string.

## Parameters

- `range`: The range of characters to replace. `range` must not exceed the bounds of the receiver.

  > ❗ **Important**:  Raises an `NSRangeException` if any part of `range` lies beyond the end of the receiver.
- `aString`: The string with which to replace the characters in `range`. `aString` must not be `nil`.

## See Also

### Modifying a String
- [func append(String)](./append%28_%29.md)
  Adds to the end of the receiver the characters of a given string.
- [func applyTransform(StringTransform, reverse: Bool, range: NSRange, updatedRange: NSRangePointer?) -> Bool](./applytransform%28_,reverse,range,updatedrange%29.md)
  Transliterates the receiver by applying a specified ICU string transform.
- [func deleteCharacters(in: NSRange)](./deletecharacters%28in%29.md)
  Removes from the receiver the characters in a given range.
- [func insert(String, at: Int)](./insert%28_,at%29.md)
  Inserts into the receiver the characters of a given string at a given location.
- [func replaceOccurrences(of: String, with: String, options: NSString.CompareOptions, range: NSRange) -> Int](./replaceoccurrences%28of,with,options,range%29.md)
  Replaces all occurrences of a given string in a given range with another given string, returning the number of replacements.
- [func setString(String)](./setstring%28_%29.md)
  Replaces the characters of the receiver with those in a given string.
- [- appendFormat:](./appendformat_.md)
  Adds a constructed string to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablestring/replacecharacters(in:with:))*