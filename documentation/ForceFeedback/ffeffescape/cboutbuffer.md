# cbOutBuffer

**Framework**: Force Feedback  
**Kind**: property  
**Role**: Instance Property

On entry, specifies the size, in bytes, of the **lpvOutBuffer** buffer. On exit, specifies the number of bytes actually produced by the command.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
var cbOutBuffer: DWORD
```

```c
DWORD cbOutBuffer;
```

## See Also

### Instance Properties
- [var cbInBuffer: DWORD](./cbinbuffer.md)
  Specifies the size, in bytes, of the **lpvInBuffer** buffer.
- [var dwCommand: DWORD](./dwcommand.md)
  Specifies a plugIn specific command number. Contact the hardware vendor for a list of valid commands and their parameters.
- [var dwSize: DWORD](./dwsize.md)
  Size, in bytes, of this structure. This member must be initialized before the structure is used.
- [var lpvInBuffer: UnsafeMutableRawPointer!](./lpvinbuffer.md)
  Buffer containing the data required to perform the operation.
- [var lpvOutBuffer: UnsafeMutableRawPointer!](./lpvoutbuffer.md)
  Buffer in which the operation’s output data is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffeffescape/cboutbuffer)*