# default

**Framework**: Foundation  
**Kind**: property

The shared file manager object for the process.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var `default`: FileManager { get }
```

#### Discussion

This method always represents the same file manager object. If you plan to use a delegate with the file manager to receive notifications about the completion of file-based operations, you should create a new instance of [`FileManager`](filemanager.md) rather than using the shared object.

## See Also

- [convenience init(authorization: NSWorkspace.Authorization)](filemanager/init(authorization:).md)
  Initializes a file manager object that is authorized to perform privileged file system operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/default)*