# character(at:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (unichar) characterAtIndex:(NSUInteger) index;
```

#### Return Value

The character at the array position given by `index`.

#### Discussion

You should always use the [`rangeOfComposedCharacterSequence(at:)`](./rangeofcomposedcharactersequence%28at%29.md) or [`rangeOfComposedCharacterSequences(for:)`](./rangeofcomposedcharactersequences%28for%29.md) method to determine character boundaries, so that any surrogate pairs or character clusters are handled correctly.

## Parameters

- `index`: The index of the character to retrieve.

  > ❗ **Important**:  Raises an `NSRangeException` if `index` lies beyond the end of the receiver.

## See Also

### Getting Characters and Bytes
- [func getCharacters(UnsafeMutablePointer<unichar>, range: NSRange)](./getcharacters%28_,range%29.md)
  Copies characters from a given range in the receiver into a given buffer.
- [func getBytes(UnsafeMutableRawPointer?, maxLength: Int, usedLength: UnsafeMutablePointer<Int>?, encoding: UInt, options: NSString.EncodingConversionOptions, range: NSRange, remaining: NSRangePointer?) -> Bool](./getbytes%28_,maxlength,usedlength,encoding,options,range,remaining%29.md)
  Gets a given range of characters as bytes in a specified encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/character(at:))*