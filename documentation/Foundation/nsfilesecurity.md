# NSFileSecurity

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

A stub class that encapsulates security information about a file.

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
class NSFileSecurity
```

```objc
@interface NSFileSecurity : NSObject
```

## Overview

[`NSFileSecurity`](./nsfilesecurity.md) contains no methods of its own. Instead, it is transparently bridged to [`CFFileSecurity`](../CoreFoundation/cffilesecurity.md).

## Topics

### Initializers
- [init?(coder: NSCoder)](./nsfilesecurity/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)

## See Also

### Managed file access
- [class FileHandle](./filehandle.md)
  An object-oriented wrapper for a file descriptor.
- [class NSFileVersion](./nsfileversion.md)
  A snapshot of a file at a specific point in time.
- [class FileWrapper](./filewrapper.md)
  A representation of a node (a file, directory, or symbolic link) in the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilesecurity)*