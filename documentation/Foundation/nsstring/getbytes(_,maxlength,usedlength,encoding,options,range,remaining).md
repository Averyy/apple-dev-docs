# getBytes(_:maxLength:usedLength:encoding:options:range:remaining:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) getBytes:(void *) buffer maxLength:(NSUInteger) maxBufferCount usedLength:(NSUInteger *) usedBufferCount encoding:(NSStringEncoding) encoding options:(NSStringEncodingConversionOptions) options range:(NSRange) range remainingRange:(NSRangePointer) leftover;
```

#### Return Value

[`true`](../../Swift/true.md) if some characters were converted, otherwise [`false`](../../Swift/false.md).

#### Discussion

Conversion might stop when the buffer fills, but it might also stop when the conversion isn’t possible due to the chosen encoding.

## Parameters

- `buffer`: A buffer into which to store the bytes from the receiver. The returned bytes are *not* `NULL`-terminated.
- `maxBufferCount`: The maximum number of bytes to write to `buffer`.
- `usedBufferCount`: The number of bytes used from `buffer`. Pass `NULL` if you do not need this value.
- `encoding`: The encoding to use for the returned bytes. For possible values, see [`NSStringEncoding`](../nsstringencoding.md).
- `options`: A mask to specify options to use for converting the receiver’s contents to `encoding` (if conversion is necessary).
- `range`: The range of characters in the receiver to get.
- `leftover`: The remaining range. Pass `NULL` If you do not need this value.

## See Also

### Getting Characters and Bytes
- [func character(at: Int) -> unichar](./character%28at%29.md)
  Returns the character at a given UTF-16 code unit index.
- [func getCharacters(UnsafeMutablePointer<unichar>, range: NSRange)](./getcharacters%28_,range%29.md)
  Copies characters from a given range in the receiver into a given buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/getbytes(_:maxlength:usedlength:encoding:options:range:remaining:))*