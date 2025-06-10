# getBytes(_:maxLength:usedLength:encoding:options:range:remaining:)

**Framework**: Foundation  
**Kind**: method

Gets a given range of characters as bytes in a specified encoding.

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
func getBytes(_ buffer: UnsafeMutableRawPointer?, maxLength maxBufferCount: Int, usedLength usedBufferCount: UnsafeMutablePointer<Int>?, encoding: UInt, options: NSString.EncodingConversionOptions = [], range: NSRange, remaining leftover: NSRangePointer?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if some characters were converted, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Conversion might stop when the buffer fills, but it might also stop when the conversion isn’t possible due to the chosen encoding.

## Parameters

- `buffer`: A buffer into which to store the bytes from the receiver. The returned bytes are    -terminated.
- `maxBufferCount`: The maximum number of bytes to write to  .
- `usedBufferCount`: The number of bytes used from  . Pass   if you do not need this value.
- `encoding`: The encoding to use for the returned bytes. For possible values, see  .
- `options`: A mask to specify options to use for converting the receiver’s contents to   (if conversion is necessary).
- `range`: The range of characters in the receiver to get.
- `leftover`: The remaining range. Pass   If you do not need this value.

## See Also

- [func character(at: Int) -> unichar](nsstring/character(at:).md)
  Returns the character at a given UTF-16 code unit index.
- [func getCharacters(UnsafeMutablePointer<unichar>, range: NSRange)](nsstring/getcharacters(_:range:).md)
  Copies characters from a given range in the receiver into a given buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/getbytes(_:maxlength:usedlength:encoding:options:range:remaining:))*