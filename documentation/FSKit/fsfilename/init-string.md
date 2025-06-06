# init(string:)

**Framework**: FSKit  
**Kind**: init

Creates a filename by copying a character sequence from a string instance.

**Availability**:
- macOS 15.4+

## Declaration

```swift
convenience init(string name: String)
```

#### Discussion

This initializer copies the UTF-8 representation of the characters in `string`. If `string` contains a `NUL` character, the sequence terminates.

## Parameters

- `name`: The string containing the character sequence to use for the filename.

## See Also

- [convenience init(bytes: UnsafeBufferPointer<CChar>)](fsfilename/init(bytes:).md)
- [convenience init(cString: UnsafeBufferPointer<CChar>)](fsfilename/init(cstring:).md)
- [convenience init(data: Data)](fsfilename/init(data:).md)
  Creates a filename by copying a character sequence data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilename/init(string:))*