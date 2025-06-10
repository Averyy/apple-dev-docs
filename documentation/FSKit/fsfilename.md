# FSFileName

**Framework**: FSKit  
**Kind**: class

The name of a file, expressed as a data buffer.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSFileName
```

#### Overview

`FSFileName` is the class that carries filenames from the kernel to `FSModule` instances, and carries names back to the kernel as part of directory enumeration.

A filename is usually a valid UTF-8 sequence, but can be an arbitrary byte sequence that doesn’t conform to that format. As a result, the [`data`](fsfilename/data.md) property always contains a value, but the [`string`](fsfilename/string.md) property may be empty. An `FSModule` can receive an `FSFileName` that isn’t valid UTF-8 in two cases:

1. A program passes erroneous data to a system call. The `FSModule` treats this situation as an error.
2. An `FSModule` lacks the character encoding used for a file name. This situation occurs because some file system formats consider a filename to be an arbitrary “bag of bytes,” and leave character encoding up to the operating system. Without encoding information, the `FSModule` can only pass back the names it finds on disk. In this case, the behavior of upper layers such as [`FileManager`](https://developer.apple.com/documentation/Foundation/FileManager) is unspecified. However, the `FSModule` must support looking up such names and using them as the source name of rename operations. The `FSModule` must also be able to support filenames that are derivatives of filenames returned from directory enumeration. Derivative filenames include Apple Double filenames (`"._Name"`), and editor backup filenames.

> ❗ **Important**: Don’t subclass this class.

## Topics

### Creating a filename
- [convenience init(bytes: UnsafeBufferPointer<CChar>)](fsfilename/init(bytes:).md)
- [convenience init(cString: UnsafeBufferPointer<CChar>)](fsfilename/init(cstring:).md)
- [convenience init(data: Data)](fsfilename/init(data:).md)
  Creates a filename by copying a character sequence data object.
- [convenience init(string: String)](fsfilename/init(string:).md)
  Creates a filename by copying a character sequence from a string instance.
### Accessing filename properties
- [var data: Data](fsfilename/data.md)
  The byte sequence of the filename, as a data object.
- [var string: String?](fsfilename/string.md)
  The filename, represented as a Unicode string.
- [var debugDescription: String](fsfilename/debugdescription.md)
  The filename, represented as a potentially lossy conversion to a string.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class FSUnaryFileSystem](fsunaryfilesystem.md)
  An abstract base class for implementing a minimal file system.
- [protocol FSFileSystemBase](fsfilesystembase.md)
  A protocol containing functionality supplied by FSKit to file system implementations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilename)*