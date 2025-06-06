# Adopting Swift File Options

**Framework**: System

Migrate existing C code to Swift, using the file-operation options provided by the System module.

#### Overview

The C options for how to open a file map to Swift as follows:

- `O_RDONLY` ⟶ [`readOnly`](filedescriptor/accessmode/readonly.md)
- `O_WRONLY` ⟶ [`writeOnly`](filedescriptor/accessmode/writeonly.md)
- `O_RDWR` ⟶ [`readWrite`](filedescriptor/accessmode/readwrite.md)

The C constants for specifying options when opening a file map to Swift as follows:

- `O_NONBLOCK` ⟶ [`nonBlocking`](filedescriptor/openoptions/nonblocking.md)
- `O_APPEND` ⟶ [`append`](filedescriptor/openoptions/append.md)
- `O_CREAT` ⟶ [`create`](filedescriptor/openoptions/create.md)
- `O_TRUNC` ⟶ [`truncate`](filedescriptor/openoptions/truncate.md)
- `O_EXCL` ⟶ [`exclusiveCreate`](filedescriptor/openoptions/exclusivecreate.md)
- `O_SHLOCK` ⟶ [`sharedLock`](filedescriptor/openoptions/sharedlock.md)
- `O_EXLOCK` ⟶ [`exclusiveLock`](filedescriptor/openoptions/exclusivelock.md)
- `O_NOFOLLOW` ⟶ [`noFollow`](filedescriptor/openoptions/nofollow.md)
- `O_SYMLINK` ⟶ [`symlink`](filedescriptor/openoptions/symlink.md)
- `O_EVTONLY` ⟶ [`eventOnly`](filedescriptor/openoptions/eventonly.md)
- `O_CLOEXEC` ⟶ [`closeOnExec`](filedescriptor/openoptions/closeonexec.md)

The C constants for specify seek offsets map to Swift as follows:

- `SEEK_SET` ⟶ [`start`](filedescriptor/seekorigin/start.md)
- `SEEK_CUR` ⟶ [`current`](filedescriptor/seekorigin/current.md)
- `SEEK_END` ⟶ [`end`](filedescriptor/seekorigin/end.md)
- `SEEK_HOLE` ⟶ [`nextHole`](filedescriptor/seekorigin/nexthole.md)
- `SEEK_DATA` ⟶ [`nextData`](filedescriptor/seekorigin/nextdata.md)

## See Also

- [Adopting Swift File Operations](adopting-file-operations.md)
  Migrate existing C code to Swift, using the file operations provided by the System module.
- [Adopting Swift Error Constants](adopting-errno.md)
  Migrate existing C code to Swift, using the error constants provided by the System module.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/adopting-file-options)*