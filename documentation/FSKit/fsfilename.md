# FSFileName

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The name of a file, expressed as a data buffer.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSFileName
```

```objc
@interface FSFileName : NSObject
```

## Overview

`FSFileName` is the class that carries filenames from the kernel to `FSModule` instances, and carries names back to the kernel as part of directory enumeration.

A filename is usually a valid UTF-8 sequence, but can be an arbitrary byte sequence that doesn’t conform to that format. As a result, the [`data`](./fsfilename/data.md) property always contains a value, but the [`string`](./fsfilename/string.md) property may be empty. An `FSModule` can receive an `FSFileName` that isn’t valid UTF-8 in two cases:

1. A program passes erroneous data to a system call. The `FSModule` treats this situation as an error.
2. An `FSModule` lacks the character encoding used for a file name. This situation occurs because some file system formats consider a filename to be an arbitrary “bag of bytes,” and leave character encoding up to the operating system. Without encoding information, the `FSModule` can only pass back the names it finds on disk. In this case, the behavior of upper layers such as [`FileManager`](../Foundation/filemanager.md) is unspecified. However, the `FSModule` must support looking up such names and using them as the source name of rename operations. The `FSModule` must also be able to support filenames that are derivatives of filenames returned from directory enumeration. Derivative filenames include Apple Double filenames (`"._Name"`), and editor backup filenames.

> ❗ **Important**: Don’t subclass this class.

## Topics

### Creating a filename
- [convenience init(bytes: UnsafeBufferPointer<CChar>)](./fsfilename/init%28bytes%29.md)
- [convenience init(cString: UnsafeBufferPointer<CChar>)](./fsfilename/init%28cstring%29.md)
- [convenience init(data: Data)](./fsfilename/init%28data%29.md)
  Creates a filename by copying a character sequence data object.
- [convenience init(string: String)](./fsfilename/init%28string%29.md)
  Creates a filename by copying a character sequence from a string instance.
- [- initWithBytes:length:](./fsfilename/initwithbytes_length_.md)
  Initializes a file name by copying a character sequence from a byte array.
- [+ nameWithBytes:length:](./fsfilename/namewithbytes_length_.md)
  Creates a filename by copying a character sequence from a byte array.
- [- initWithCString:](./fsfilename/initwithcstring_.md)
  Initializes a filename from a null-terminated character sequence.
- [+ nameWithCString:](./fsfilename/namewithcstring_.md)
  Creates a filename from a null-terminated character sequence.
- [+ nameWithData:](./fsfilename/namewithdata_.md)
  Creates a filename by copying a character sequence data object.
- [+ nameWithString:](./fsfilename/namewithstring_.md)
  Creates a filename by copying a character sequence from a string instance.
### Accessing filename properties
- [var data: Data](./fsfilename/data.md)
  The byte sequence of the filename, as a data object.
- [var string: String?](./fsfilename/string.md)
  The filename, represented as a Unicode string.
- [var debugDescription: String](./fsfilename/debugdescription.md)
  The filename, represented as a potentially lossy conversion to a string.
### Initializers
- [init?(coder: NSCoder)](./fsfilename/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### File systems
- [class FSUnaryFileSystem](./fsunaryfilesystem.md)
  An abstract base class for implementing a minimal file system.
- [protocol FSFileSystemBase](./fsfilesystembase.md)
  A protocol containing functionality supplied by FSKit to file system implementations.
- [FSFileSystem](./fsfilesystem.md)
  An abstract base class for implementing a full-featured file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilename)*