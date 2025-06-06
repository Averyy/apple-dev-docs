# init(data:)

**Framework**: FSKit  
**Kind**: init

Creates a filename by copying a character sequence data object.

**Availability**:
- macOS 15.4+

## Declaration

```swift
convenience init(data name: Data)
```

#### Discussion

This initializer copies up to `name.length` characters of the sequence pointed to by `bytes`.

## Parameters

- `name`: The data object containing the character sequence to use for the filename. The sequence terminates if a   character exists prior to  .

## See Also

- [convenience init(bytes: UnsafeBufferPointer<CChar>)](fsfilename/init(bytes:).md)
- [convenience init(cString: UnsafeBufferPointer<CChar>)](fsfilename/init(cstring:).md)
- [convenience init(string: String)](fsfilename/init(string:).md)
  Creates a filename by copying a character sequence from a string instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilename/init(data:))*