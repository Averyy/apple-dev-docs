# FSPathURLResource

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

A resource that represents a path in the system file space.

**Availability**:
- macOS 26.0+

## Declaration

```swift
class FSPathURLResource
```

```objc
@interface FSPathURLResource : FSResource
```

#### Overview

The URL passed to `FSPathURLResource` may be a security-scoped URL. If the URL is a security-scoped URL, FSKit transports it intact from a client application to your extension.

## Topics

### Creating a path URL resource
- [init(url: URL, writable: Bool)](./fspathurlresource/init%28url,writable%29-2l10q.md)
  Creates a path URL resource.
### Accessing resource properties
- [var url: URL](./fspathurlresource/url.md)
  The URL represented by the resource.
- [var isWritable: Bool](./fspathurlresource/iswritable.md)
  A Boolean value that indicates whether the file system supports writing to the contents of the path URL.
### Initializers
- [init(URL: URL, writable: Bool)](./fspathurlresource/init%28url,writable%29-52fco.md)

## Relationships

### Inherits From
- [FSResource](./fsresource.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Resources
- [class FSResource](./fsresource.md)
  An abstract resource a file system uses to provide data for a volume.
- [class FSBlockDeviceResource](./fsblockdeviceresource.md)
  A resource that represents a block storage disk partition.
- [class FSGenericURLResource](./fsgenericurlresource.md)
  A resource that represents an abstract URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fspathurlresource)*