# kCFURLTotalFileAllocatedSizeKey

**Framework**: Core Foundation  
**Kind**: var

Key for the total allocated size of the file in bytes, returned as a `CFNumber` object. This includes the size of any file metadata.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCFURLTotalFileAllocatedSizeKey: CFString!
```

## See Also

- [let kCFURLFileAllocatedSizeKey: CFString!](kcfurlfileallocatedsizekey.md)
  Key for the total size allocated on disk for the file, returned as an `CFNumber` object.
- [let kCFURLFileSizeKey: CFString!](kcfurlfilesizekey.md)
  Key for the file’s size in bytes, returned as a `CFNumber` object.
- [let kCFURLIsAliasFileKey: CFString!](kcfurlisaliasfilekey.md)
  Key for determining whether the file is an alias, returned as a `CFBoolean` object.
- [let kCFURLIsMountTriggerKey: CFString!](kcfurlismounttriggerkey.md)
  Key for determining whether the URL is a file system trigger directory, returned as a `CFBoolean` object. Traversing or opening a file system trigger directory causes an attempt to mount a file system on the directory.
- [let kCFURLTotalFileSizeKey: CFString!](kcfurltotalfilesizekey.md)
  Key for the total displayable size of the file in bytes, returned as a `CFNumber` object. This includes the size of any file metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfurltotalfileallocatedsizekey)*