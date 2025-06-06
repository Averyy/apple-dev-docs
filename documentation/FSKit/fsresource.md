# FSResource

**Framework**: FSKit  
**Kind**: class

An abstract resource a file system uses to provide data for a volume.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSResource
```

#### Overview

`FSResource` is a base class to represent the various possible sources of data for a file system. These range from dedicated storage devices like hard drives and flash storage to network connections, and beyond. Subclasses define behavior specific to a given kind of resource, such as [`FSBlockDeviceResource`](fsblockdeviceresource.md) for disk partition (IOMedia) file systems. These file systems are typical disk file systems such as HFS, APFS, ExFAT, ext2fs, or NTFS.

A resource’s type also determines its life cycle. Resources based on block storage devices come into being when the system probes the media underlying the volumes and container. Other kinds of resources, like those based on URLs, might have different life cycles. For example, a resource based on a `file://` URL might iniitalize when a person uses the “Connect to server” command in the macOS Finder.

##### Proxying Resources

Some resources, like [`FSBlockDeviceResource`](fsblockdeviceresource.md), come in proxy and non-proxy variants. This addresses the issue that opening an external device like `/dev/disk2s1` requires an entitlement. Proxy resources allow unentitled clients of FSKit to describe which disk an [`FSBlockDeviceResource`](fsblockdeviceresource.md) should represent. This allows, for example, the `mount(8)` tool to mount FSKit file systems on block devices when run as root. The tool uses a proxy when executing a command like `mount -t ffs /dev/disk2s1 /some/path`, which prevents leaking privileged resource access.

## Topics

### Creating proxies
- [func makeProxy() -> Self](fsresource/makeproxy.md)
  Creates a proxy object of this resource.
### Revoking the resource
- [func revoke()](fsresource/revoke.md)
  Revokes the resource.
- [var isRevoked: Bool](fsresource/isrevoked.md)
  A Boolean value that indicates whether the resource is revoked.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [FSBlockDeviceResource](fsblockdeviceresource.md)
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

- [class FSBlockDeviceResource](fsblockdeviceresource.md)
  A resource that represents a block storage disk partition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsresource)*