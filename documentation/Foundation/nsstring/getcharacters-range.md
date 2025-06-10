# getCharacters(_:range:)

**Framework**: Foundation  
**Kind**: method

Copies characters from a given range in the receiver into a given buffer.

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
func getCharacters(_ buffer: UnsafeMutablePointer<unichar>, range: NSRange)
```

#### Discussion

This method does not add a `NULL` character.

The abstract implementation of this method uses [`character(at:)`](nsstring/character(at:).md) repeatedly, correctly extracting the characters, though very inefficiently. Subclasses should override it to provide a fast implementation.

You should always use the [`rangeOfComposedCharacterSequence(at:)`](nsstring/rangeofcomposedcharactersequence(at:).md) or [`rangeOfComposedCharacterSequences(for:)`](nsstring/rangeofcomposedcharactersequences(for:).md) method to determine character boundaries, so that any surrogate pairs or character clusters are handled correctly.

## Parameters

- `buffer`: Upon return, contains the characters from the receiver.   must be large enough to contain the characters in the range   ( ).
- `range`: The range of characters to retrieve. The range must not exceed the bounds of the receiver.

## See Also

- [func character(at: Int) -> unichar](nsstring/character(at:).md)
  Returns the character at a given UTF-16 code unit index.
- [func getBytes(UnsafeMutableRawPointer?, maxLength: Int, usedLength: UnsafeMutablePointer<Int>?, encoding: UInt, options: NSString.EncodingConversionOptions, range: NSRange, remaining: NSRangePointer?) -> Bool](nsstring/getbytes(_:maxlength:usedlength:encoding:options:range:remaining:).md)
  Gets a given range of characters as bytes in a specified encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/getcharacters(_:range:))*