# lpvInBuffer

**Framework**: Force Feedback  
**Kind**: property  
**Role**: Instance Property

Buffer containing the data required to perform the operation.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
var lpvInBuffer: UnsafeMutableRawPointer!
```

```c
void * lpvInBuffer;
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
- [var lpvOutBuffer: UnsafeMutableRawPointer!](./lpvoutbuffer.md)
  Buffer in which the operation’s output data is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffeffescape/lpvinbuffer)*