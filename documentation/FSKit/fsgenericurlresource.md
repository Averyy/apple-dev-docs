# FSGenericURLResource

**Framework**: FSKit  
**Kind**: class

A resource that represents an abstract URL.

**Availability**:
- macOS 26.0+

## Declaration

```swift
class FSGenericURLResource
```

#### Overview

An `FSGenericURLResource` is a completely abstract resource. The only reference to its contents is a single URL, the contents of which are arbitrary. This URL might represent a PCI locator string like `/pci@f0000000/usb@5`, or some sort of network address for a remote file system. FSKit leaves interpretation of the URL and its contents entirely up to your implementation.

Use the `Info.plist` key `FSSupportedSchemes` to provide an array of case-insensitive URL schemes that your implementation supports. The following example shows how a hypothetical `FSGenericURLResource` implementation declares support for the `rsh` and `ssh` URL schemes:

```swift
<key>FSSupportedSchemes</key>
<array>
    <string>rsh</string>
    <string>ssh</string>
</array>
```

## Topics

### Creating a generic URL resource
- [init(url: URL)](fsgenericurlresource/init(url:).md)
  Creates a generic URL resource with the given URL.
### Accessing resource properties
- [var url: URL](fsgenericurlresource/url.md)
  The URL represented by the resource.

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
- [class FSPathURLResource](fspathurlresource.md)
  A resource that represents a path in the system file space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsgenericurlresource)*