# Adopting Swift File Operations

**Framework**: System

Migrate existing C code to Swift, using the file operations provided by the System module.

#### Overview

The C functions for file operations map to Swift as follows:

- `close` ⟶ [`close()`](filedescriptor/close().md)
- `lseek` ⟶ [`seek(offset:from:)`](filedescriptor/seek(offset:from:).md)  
- `open` ⟶ [`open(_:_:options:permissions:retryOnInterrupt:)`](filedescriptor/open(_:_:options:permissions:retryoninterrupt:)-4ql4b.md)
- `pread` ⟶ [`read(fromAbsoluteOffset:into:retryOnInterrupt:)`](filedescriptor/read(fromabsoluteoffset:into:retryoninterrupt:).md)
- `pwrite` ⟶ [`write(toAbsoluteOffset:_:retryOnInterrupt:)`](filedescriptor/write(toabsoluteoffset:_:retryoninterrupt:).md)
- `read` ⟶ [`read(into:retryOnInterrupt:)`](filedescriptor/read(into:retryoninterrupt:).md)
- `write` ⟶ [`write(_:retryOnInterrupt:)`](filedescriptor/write(_:retryoninterrupt:).md)

## See Also

- [Adopting Swift File Options](adopting-file-options.md)
  Migrate existing C code to Swift, using the file-operation options provided by the System module.
- [Adopting Swift Error Constants](adopting-errno.md)
  Migrate existing C code to Swift, using the error constants provided by the System module.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/adopting-file-operations)*