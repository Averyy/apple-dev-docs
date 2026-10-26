# initWithCString:

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Initializes a filename from a null-terminated character sequence.

**Availability**:
- macOS 15.4+

## Declaration

```objc
- (instancetype) initWithCString:(const char *) name;
```

#### Discussion

> **Note**: This initializer is unavailable in Swift. Use [`init(data:)`](./init%28data%29.md) or [`init(string:)`](./init%28string%29.md) instead.

## Parameters

- `name`: A pointer to a C string.

## See Also

### Creating a filename
- [- initWithBytes:length:](./initwithbytes_length_.md)
  Initializes a file name by copying a character sequence from a byte array.
- [+ nameWithBytes:length:](./namewithbytes_length_.md)
  Creates a filename by copying a character sequence from a byte array.
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

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilename/initwithcstring:)*