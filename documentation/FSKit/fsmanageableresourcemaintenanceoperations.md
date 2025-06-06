# FSManageableResourceMaintenanceOperations

**Framework**: FSKit  
**Kind**: protocol

Maintenance operations for a file system’s resources.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol FSManageableResourceMaintenanceOperations : NSObjectProtocol
```

#### Overview

This protocol includes operations to check and format a resource for an [`FSUnaryFileSystem`](fsunaryfilesystem.md). Conform to this protocol if you implement a [`FSUnaryFileSystem`](fsunaryfilesystem.md) that uses an [`FSBlockDeviceResource`](fsblockdeviceresource.md).

## Topics

### Checking the file system
- [func startCheck(task: FSTask, options: FSTaskOptions) throws -> Progress](fsmanageableresourcemaintenanceoperations/startcheck(task:options:).md)
  Starts checking the file system with the given options.
### Formatting the file system
- [func startFormat(task: FSTask, options: FSTaskOptions) throws -> Progress](fsmanageableresourcemaintenanceoperations/startformat(task:options:).md)
  Starts formatting the file system with the given options.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmanageableresourcemaintenanceoperations)*