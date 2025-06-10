# replaceCharacters(in:with:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

This method treats the length of the string as a valid range value that returns an empty string.

## Parameters

- `range`: The range of characters to replace.   must not exceed the bounds of the receiver.
- `aString`: The string with which to replace the characters in  .   must not be  .

## See Also

- [func append(String)](nsmutablestring/append(_:).md)
  Adds to the end of the receiver the characters of a given string.
- [func applyTransform(StringTransform, reverse: Bool, range: NSRange, updatedRange: NSRangePointer?) -> Bool](nsmutablestring/applytransform(_:reverse:range:updatedrange:).md)
  Transliterates the receiver by applying a specified ICU string transform.
- [func deleteCharacters(in: NSRange)](nsmutablestring/deletecharacters(in:).md)
  Removes from the receiver the characters in a given range.
- [func insert(String, at: Int)](nsmutablestring/insert(_:at:).md)
  Inserts into the receiver the characters of a given string at a given location.
- [func replaceOccurrences(of: String, with: String, options: NSString.CompareOptions, range: NSRange) -> Int](nsmutablestring/replaceoccurrences(of:with:options:range:).md)
  Replaces all occurrences of a given string in a given range with another given string, returning the number of replacements.
- [func setString(String)](nsmutablestring/setstring(_:).md)
  Replaces the characters of the receiver with those in a given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablestring/replacecharacters(in:with:))*