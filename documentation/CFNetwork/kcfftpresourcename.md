# kCFFTPResourceName

**Framework**: CFNetwork  
**Kind**: var

CFDictionary key for getting the CFString containing the name of the FTP resource.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let kCFFTPResourceName: CFString
```

## See Also

- [func CFFTPCreateParsedResourceListing(CFAllocator?, UnsafePointer<UInt8>, CFIndex, UnsafeMutablePointer<Unmanaged<CFDictionary>?>?) -> CFIndex](cfftpcreateparsedresourcelisting(_:_:_:_:).md)
  Parses an FTP listing to a dictionary.
- [let kCFFTPResourceGroup: CFString](kcfftpresourcegroup.md)
  CFDictionary key for getting the CFString containing the name of a group that shares the FTP resource.
- [let kCFFTPResourceLink: CFString](kcfftpresourcelink.md)
  CFDictionary key for getting the CFString containing the symbolic link information. If the item is a symbolic link, the CFString contains the path to the item that the link references.
- [let kCFFTPResourceModDate: CFString](kcfftpresourcemoddate.md)
  CFDictionary key for getting the CFDate containing the last date and time the FTP resource was modified.
- [let kCFFTPResourceMode: CFString](kcfftpresourcemode.md)
  CFDictionary key for getting the CFNumber containing the access permissions, defined in `sys/types.h`, of the FTP resource.
- [let kCFFTPResourceOwner: CFString](kcfftpresourceowner.md)
  CFDictionary key for getting the CFString containing the name of the owner of the FTP resource.
- [let kCFFTPResourceSize: CFString](kcfftpresourcesize.md)
  CFDictionary key for getting the CFNumber containing the size in bytes of the FTP resource.
- [let kCFFTPResourceType: CFString](kcfftpresourcetype.md)
  CFDictionary key for getting the CFNumber containing the type of the FTP resource as defined in `sys/dirent.h`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcename)*