# character(at:)

**Framework**: Foundation  
**Kind**: method

Returns the character at a given UTF-16 code unit index.

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
func character(at index: Int) -> unichar
```

#### Return Value

The character at the array position given by `index`.

#### Discussion

You should always use the [`rangeOfComposedCharacterSequence(at:)`](nsstring/rangeofcomposedcharactersequence(at:).md) or [`rangeOfComposedCharacterSequences(for:)`](nsstring/rangeofcomposedcharactersequences(for:).md) method to determine character boundaries, so that any surrogate pairs or character clusters are handled correctly.

## Parameters

- `index`: The index of the character to retrieve.

## See Also

- [func getCharacters(UnsafeMutablePointer<unichar>, range: NSRange)](nsstring/getcharacters(_:range:).md)
  Copies characters from a given range in the receiver into a given buffer.
- [func getBytes(UnsafeMutableRawPointer?, maxLength: Int, usedLength: UnsafeMutablePointer<Int>?, encoding: UInt, options: NSString.EncodingConversionOptions, range: NSRange, remaining: NSRangePointer?) -> Bool](nsstring/getbytes(_:maxlength:usedlength:encoding:options:range:remaining:).md)
  Gets a given range of characters as bytes in a specified encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/character(at:))*