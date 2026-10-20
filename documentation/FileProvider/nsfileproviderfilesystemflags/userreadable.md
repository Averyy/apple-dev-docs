# userReadable

**Framework**: File Provider  
**Kind**: property  
**Role**: Type Property

The user can read the item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static var userReadable: NSFileProviderFileSystemFlags { get }
```

```c
NSFileProviderFileSystemUserReadable
```

## See Also

### Flags
- [static var userWritable: NSFileProviderFileSystemFlags](./userwritable.md)
  The user can modify the item.
- [static var userExecutable: NSFileProviderFileSystemFlags](./userexecutable.md)
  The user can execute the item.
- [static var hidden: NSFileProviderFileSystemFlags](./hidden.md)
  By default, the system hides the item when the user views the file system.
- [static var pathExtensionHidden: NSFileProviderFileSystemFlags](./pathextensionhidden.md)
  By default, the system hides the item’s extension when showing its filename.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderfilesystemflags/userreadable)*