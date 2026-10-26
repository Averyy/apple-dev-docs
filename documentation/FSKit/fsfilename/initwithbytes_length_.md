# initWithBytes:length:

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Initializes a file name by copying a character sequence from a byte array.

**Availability**:
- macOS 15.4+

## Declaration

```objc
- (instancetype) initWithBytes:(const char *) bytes length:(NSUInteger) length;
```

#### Discussion

> **Note**: This initializer is unavailable in Swift. Use [`init(data:)`](./init%28data%29.md) or [`init(string:)`](./init%28string%29.md) instead.

- bytes: A pointer to the character data to copy, up to a maximum of `length`. The sequence terminates if a `NUL` character exists prior to `length`.
- length: The size of the `bytes` array.

## See Also

### Creating a filename
- [+ nameWithBytes:length:](./namewithbytes_length_.md)
  Creates a filename by copying a character sequence from a byte array.
- [- initWithCString:](./initwithcstring_.md)
  Initializes a filename from a null-terminated character sequence.
- [+ nameWithCString:](./namewithcstring_.md)
  Creates a filename from a null-terminated character sequence.
- [convenience init(data: Data)](./init%28data%29.md)
  Creates a filename by copying a character sequence data object.
- [+ nameWithData:](./namewithdata_.md)
  Creates a filename by copying a character sequence data object.
- [convenience init(string: String)](./init%28string%29.md)
  Creates a filename by copying a character sequence from a string instance.
- [+ nameWithString:](./namewithstring_.md)
  Creates a filename by copying a character sequence from a string instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilename/initwithbytes:length:)*