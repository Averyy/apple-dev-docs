# FSPathURLResource

**Framework**: FSKit  
**Kind**: class

A resource that represents a path in the system file space.

**Availability**:
- macOS 26.0+

## Declaration

```swift
class FSPathURLResource
```

#### Overview

The URL passed to `FSPathURLResource` may be a security-scoped URL. If the URL is a security-scoped URL, FSKit transports it intact from a client application to your extension.

## Topics

### Creating a path URL resource
- [init(url: URL, writable: Bool)](fspathurlresource/init(url:writable:).md)
  Creates a path URL resource.
### Accessing resource properties
- [var url: URL](fspathurlresource/url.md)
  The URL represented by the resource.
- [var isWritable: Bool](fspathurlresource/iswritable.md)
  A Boolean value that indicates whether the file system supports writing to the contents of the path URL.

## Relationships

### Inherits From
- [FSResource](fsresource.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class FSResource](fsresource.md)
  An abstract resource a file system uses to provide data for a volume.
- [class FSBlockDeviceResource](fsblockdeviceresource.md)
  A resource that represents a block storage disk partition.
- [class FSGenericURLResource](fsgenericurlresource.md)
  A resource that represents an abstract URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fspathurlresource)*