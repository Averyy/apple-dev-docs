# Adopting Swift File Operations

**Framework**: System  
**Role**: Article

Migrate existing C code to Swift, using the file operations provided by the System module.

## Overview

The C functions for file operations map to Swift as follows:

- `close` ⟶ [`close()`](./filedescriptor/close%28%29.md)
- `lseek` ⟶ [`seek(offset:from:)`](./filedescriptor/seek%28offset,from%29.md)  
- `open` ⟶ [`open(_:_:options:permissions:retryOnInterrupt:)`](./filedescriptor/open%28_,_,options,permissions,retryoninterrupt%29-4ql4b.md)
- `pread` ⟶ [`read(fromAbsoluteOffset:into:retryOnInterrupt:)`](./filedescriptor/read%28fromabsoluteoffset,into,retryoninterrupt%29.md)
- `pwrite` ⟶ [`write(toAbsoluteOffset:_:retryOnInterrupt:)`](./filedescriptor/write%28toabsoluteoffset,_,retryoninterrupt%29.md)
- `read` ⟶ [`read(into:retryOnInterrupt:)`](./filedescriptor/read%28into,retryoninterrupt%29.md)
- `write` ⟶ [`write(_:retryOnInterrupt:)`](./filedescriptor/write%28_,retryoninterrupt%29.md)

## See Also

### Adopting System
- [Adopting Swift File Options](./adopting-file-options.md)
  Migrate existing C code to Swift, using the file-operation options provided by the System module.
- [Adopting Swift Error Constants](./adopting-errno.md)
  Migrate existing C code to Swift, using the error constants provided by the System module.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/adopting-file-operations)*