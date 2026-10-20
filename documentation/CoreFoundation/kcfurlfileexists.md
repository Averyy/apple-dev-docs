# kCFURLFileExists

**Framework**: Core Foundation  
**Kind**: var  
**Role**: Global Variable

A `CFBoolean` object indicating whether the file referred to by a URL exists.

**Availability**:
- iOS 2.0+ - Deprecated in 7.0
- iPadOS 2.0+ - Deprecated in 7.0
- Mac Catalyst 2.0+ - Deprecated in 7.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use CFURLResourceIsReachable instead.

## Declaration

```swift
let kCFURLFileExists: CFString!
```

```c
extern CFStringRef const kCFURLFileExists;
```

## See Also

### Constants
- [let kCFURLFileDirectoryContents: CFString!](./kcfurlfiledirectorycontents.md)
  A `CFArray` object holding `CFURL` objects for the contents of a directory referred to by a URL.
- [let kCFURLFileLength: CFString!](./kcfurlfilelength.md)
  A `CFNumber` object holding the file’s length in bytes.
- [let kCFURLFileLastModificationTime: CFString!](./kcfurlfilelastmodificationtime.md)
  A `CFDate` object holding the file’s modification time.
- [let kCFURLFilePOSIXMode: CFString!](./kcfurlfileposixmode.md)
  A `CFNumber` holding the file’s POSIX mode as given in `/usr/include/sys/stat.h`.
- [let kCFURLFileOwnerID: CFString!](./kcfurlfileownerid.md)
  A `CFNumber` holding the file owner’s UID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfurlfileexists)*