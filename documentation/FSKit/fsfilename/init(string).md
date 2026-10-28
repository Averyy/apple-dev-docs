# init(string:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Creates a filename by copying a character sequence from a string instance.

**Availability**:
- macOS 15.4+

## Declaration

```swift
convenience init(string name: String)
```

```objc
- (instancetype) initWithString:(NSString *) name;
```

## Discussion

This initializer copies the UTF-8 representation of the characters in `string`. If `string` contains a `NUL` character, the sequence terminates.

## Parameters

- `name`: The string containing the character sequence to use for the filename.

## See Also

### Creating a filename
- [convenience init(bytes: UnsafeBufferPointer<CChar>)](./init%28bytes%29.md)
- [convenience init(cString: UnsafeBufferPointer<CChar>)](./init%28cstring%29.md)
- [convenience init(data: Data)](./init%28data%29.md)
  Creates a filename by copying a character sequence data object.
- [- initWithBytes:length:](./initwithbytes_length_.md)
  Initializes a file name by copying a character sequence from a byte array.
- [+ nameWithBytes:length:](./namewithbytes_length_.md)
  Creates a filename by copying a character sequence from a byte array.
- [- initWithCString:](./initwithcstring_.md)
  Initializes a filename from a null-terminated character sequence.
- [+ nameWithCString:](./namewithcstring_.md)
  Creates a filename from a null-terminated character sequence.
- [+ nameWithData:](./namewithdata_.md)
  Creates a filename by copying a character sequence data object.
- [+ nameWithString:](./namewithstring_.md)
  Creates a filename by copying a character sequence from a string instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilename/init(string:))*