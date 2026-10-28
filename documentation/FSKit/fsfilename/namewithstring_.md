# nameWithString:

**Framework**: FSKit  
**Kind**: method  
**Role**: Type Method

Creates a filename by copying a character sequence from a string instance.

**Availability**:
- macOS 15.4+

## Declaration

```objc
+ (instancetype) nameWithString:(NSString *) name;
```

## Discussion

This initializer copies the UTF-8 representation of the characters in `string`. If `string` contains a `NUL` character, the sequence terminates.

## Parameters

- `name`: The string containing the character sequence to use for the filename.

## See Also

### Creating a filename
- [- initWithBytes:length:](./initwithbytes_length_.md)
  Initializes a file name by copying a character sequence from a byte array.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilename/namewithstring:)*