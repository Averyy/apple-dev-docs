# dwSize

**Framework**: Force Feedback  
**Kind**: property

Size, in bytes, of this structure. This member must be initialized before the structure is used.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
var dwSize: DWORD
```

## See Also

- [var cbInBuffer: DWORD](ffeffescape/cbinbuffer.md)
  Specifies the size, in bytes, of the  buffer.
- [var cbOutBuffer: DWORD](ffeffescape/cboutbuffer.md)
  On entry, specifies the size, in bytes, of the  buffer. On exit, specifies the number of bytes actually produced by the command.
- [var dwCommand: DWORD](ffeffescape/dwcommand.md)
  Specifies a plugIn specific command number. Contact the hardware vendor for a list of valid commands and their parameters.
- [var lpvInBuffer: UnsafeMutableRawPointer!](ffeffescape/lpvinbuffer.md)
  Buffer containing the data required to perform the operation.
- [var lpvOutBuffer: UnsafeMutableRawPointer!](ffeffescape/lpvoutbuffer.md)
  Buffer in which the operation’s output data is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffeffescape/dwsize)*