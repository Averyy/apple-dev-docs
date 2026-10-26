# fillBuffer:range:value:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a command that fills a buffer with a constant value for each byte.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) fillBuffer:(id<MTLBuffer>) buffer range:(NSRange) range value:(uint8_t) value;
```

## Parameters

- `buffer`: A [`MTLBuffer`](../mtlbuffer.md) instance for which this command assigns each byte in a range to a value.
- `range`: A range of bytes within `buffer` the command assigns value to. When calling this method, pass in a range with a length greater than `0`.
- `value`: The value to write to each byte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/fillbuffer:range:value:)*