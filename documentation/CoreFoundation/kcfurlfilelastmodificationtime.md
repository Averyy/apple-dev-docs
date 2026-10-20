# kCFURLFileLastModificationTime

**Framework**: Core Foundation  
**Kind**: var  
**Role**: Global Variable

A `CFDate` object holding the file’s modification time.

**Availability**:
- iOS 2.0+ - Deprecated in 7.0
- iPadOS 2.0+ - Deprecated in 7.0
- Mac Catalyst 2.0+ - Deprecated in 7.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use CFURLCopyResourcePropertyForKey with kCFURLContentModificationDateKey instead.

## Declaration

```swift
let kCFURLFileLastModificationTime: CFString!
```

```c
extern CFStringRef const kCFURLFileLastModificationTime;
```

## See Also

### Constants
- [let kCFURLFileExists: CFString!](./kcfurlfileexists.md)
  A `CFBoolean` object indicating whether the file referred to by a URL exists.
- [let kCFURLFileDirectoryContents: CFString!](./kcfurlfiledirectorycontents.md)
  A `CFArray` object holding `CFURL` objects for the contents of a directory referred to by a URL.
- [let kCFURLFileLength: CFString!](./kcfurlfilelength.md)
  A `CFNumber` object holding the file’s length in bytes.
- [let kCFURLFilePOSIXMode: CFString!](./kcfurlfileposixmode.md)
  A `CFNumber` holding the file’s POSIX mode as given in `/usr/include/sys/stat.h`.
- [let kCFURLFileOwnerID: CFString!](./kcfurlfileownerid.md)
  A `CFNumber` holding the file owner’s UID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfurlfilelastmodificationtime)*