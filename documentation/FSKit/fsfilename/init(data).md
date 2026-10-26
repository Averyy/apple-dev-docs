# init(data:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Creates a filename by copying a character sequence data object.

**Availability**:
- macOS 15.4+

## Declaration

```swift
convenience init(data name: Data)
```

```objc
- (instancetype) initWithData:(NSData *) name;
```

#### Discussion

This initializer copies up to `name.length` characters of the sequence pointed to by `bytes`.

## Parameters

- `name`: The data object containing the character sequence to use for the filename. The sequence terminates if a `NUL` character exists prior to `name.length`.

## See Also

### Creating a filename
- [convenience init(bytes: UnsafeBufferPointer<CChar>)](./init%28bytes%29.md)
- [convenience init(cString: UnsafeBufferPointer<CChar>)](./init%28cstring%29.md)
- [convenience init(string: String)](./init%28string%29.md)
  Creates a filename by copying a character sequence from a string instance.
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

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilename/init(data:))*