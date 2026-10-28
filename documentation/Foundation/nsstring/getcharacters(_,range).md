# getCharacters(_:range:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) getCharacters:(unichar *) buffer range:(NSRange) range;
```

## Discussion

This method does not add a `NULL` character.

The abstract implementation of this method uses [`character(at:)`](./character%28at%29.md) repeatedly, correctly extracting the characters, though very inefficiently. Subclasses should override it to provide a fast implementation.

You should always use the [`rangeOfComposedCharacterSequence(at:)`](./rangeofcomposedcharactersequence%28at%29.md) or [`rangeOfComposedCharacterSequences(for:)`](./rangeofcomposedcharactersequences%28for%29.md) method to determine character boundaries, so that any surrogate pairs or character clusters are handled correctly.

## Parameters

- `buffer`: Upon return, contains the characters from the receiver. `buffer` must be large enough to contain the characters in the range `aRange` (`aRange.length*sizeof(unichar)`).
- `range`: The range of characters to retrieve. The range must not exceed the bounds of the receiver.

  > ❗ **Important**:  Raises an `NSRangeException` if any part of `aRange` lies beyond the bounds of the receiver.

## See Also

### Getting Characters and Bytes
- [func character(at: Int) -> unichar](./character%28at%29.md)
  Returns the character at a given UTF-16 code unit index.
- [func getBytes(UnsafeMutableRawPointer?, maxLength: Int, usedLength: UnsafeMutablePointer<Int>?, encoding: UInt, options: NSString.EncodingConversionOptions, range: NSRange, remaining: NSRangePointer?) -> Bool](./getbytes%28_,maxlength,usedlength,encoding,options,range,remaining%29.md)
  Gets a given range of characters as bytes in a specified encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/getcharacters(_:range:))*