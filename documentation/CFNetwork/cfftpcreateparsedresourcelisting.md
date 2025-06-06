# CFFTPCreateParsedResourceListing(_:_:_:_:)

**Framework**: CFNetwork  
**Kind**: func

Parses an FTP listing to a dictionary.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CFFTPCreateParsedResourceListing(_ alloc: CFAllocator?, _ buffer: UnsafePointer<UInt8>, _ bufferLength: CFIndex, _ parsed: UnsafeMutablePointer<Unmanaged<CFDictionary>?>?) -> CFIndex
```

#### Return Value

The number of bytes parsed, `0` if no bytes were available for parsing, or `-1` if parsing failed.

#### Discussion

This function examines the contents of buffer as an FTP directory listing and parses into a CFDictionary the information for a single file or folder. The CFDictionary is returned in the `parsed` parameter, and the number of bytes used from buffer is returned.

## Parameters

- `alloc`: The allocator to use to allocate memory for the dictionary. Pass   or kCFAllocatorDefault to use the current default allocator.
- `buffer`: A pointer to a buffer holding zero or more lines of resource listing.
- `bufferLength`: The length in bytes of the buffer pointed to by  .
- `parsed`: Upon return, contains a dictionary containing the parsed resource information. If parsing fails, a   pointer is returned.

## See Also

- [let kCFFTPResourceGroup: CFString](kcfftpresourcegroup.md)
  CFDictionary key for getting the CFString containing the name of a group that shares the FTP resource.
- [let kCFFTPResourceLink: CFString](kcfftpresourcelink.md)
  CFDictionary key for getting the CFString containing the symbolic link information. If the item is a symbolic link, the CFString contains the path to the item that the link references.
- [let kCFFTPResourceModDate: CFString](kcfftpresourcemoddate.md)
  CFDictionary key for getting the CFDate containing the last date and time the FTP resource was modified.
- [let kCFFTPResourceMode: CFString](kcfftpresourcemode.md)
  CFDictionary key for getting the CFNumber containing the access permissions, defined in `sys/types.h`, of the FTP resource.
- [let kCFFTPResourceName: CFString](kcfftpresourcename.md)
  CFDictionary key for getting the CFString containing the name of the FTP resource.
- [let kCFFTPResourceOwner: CFString](kcfftpresourceowner.md)
  CFDictionary key for getting the CFString containing the name of the owner of the FTP resource.
- [let kCFFTPResourceSize: CFString](kcfftpresourcesize.md)
  CFDictionary key for getting the CFNumber containing the size in bytes of the FTP resource.
- [let kCFFTPResourceType: CFString](kcfftpresourcetype.md)
  CFDictionary key for getting the CFNumber containing the type of the FTP resource as defined in `sys/dirent.h`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfftpcreateparsedresourcelisting(_:_:_:_:))*