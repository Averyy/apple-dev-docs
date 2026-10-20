# lpvOutBuffer

**Framework**: Force Feedback  
**Kind**: property  
**Role**: Instance Property

Buffer in which the operation’s output data is returned.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
var lpvOutBuffer: UnsafeMutableRawPointer!
```

```c
void * lpvOutBuffer;
```

## See Also

### Instance Properties
- [var cbInBuffer: DWORD](./cbinbuffer.md)
  Specifies the size, in bytes, of the **lpvInBuffer** buffer.
- [var cbOutBuffer: DWORD](./cboutbuffer.md)
  On entry, specifies the size, in bytes, of the **lpvOutBuffer** buffer. On exit, specifies the number of bytes actually produced by the command.
- [var dwCommand: DWORD](./dwcommand.md)
  Specifies a plugIn specific command number. Contact the hardware vendor for a list of valid commands and their parameters.
- [var dwSize: DWORD](./dwsize.md)
  Size, in bytes, of this structure. This member must be initialized before the structure is used.
- [var lpvInBuffer: UnsafeMutableRawPointer!](./lpvinbuffer.md)
  Buffer containing the data required to perform the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffeffescape/lpvoutbuffer)*