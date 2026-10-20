# FSManageableResourceMaintenanceOperations

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

Maintenance operations for a file system’s resources.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol FSManageableResourceMaintenanceOperations : NSObjectProtocol
```

```objc
@protocol FSManageableResourceMaintenanceOperations <NSObject>
```

#### Overview

This protocol includes operations to check and format a resource for an [`FSUnaryFileSystem`](./fsunaryfilesystem.md). Conform to this protocol if you implement a [`FSUnaryFileSystem`](./fsunaryfilesystem.md) that uses an [`FSBlockDeviceResource`](./fsblockdeviceresource.md).

## Topics

### Checking the file system
- [func startCheck(task: FSTask, options: FSTaskOptions) throws -> Progress](./fsmanageableresourcemaintenanceoperations/startcheck%28task,options%29.md)
  Starts checking the file system with the given options.
### Formatting the file system
- [func startFormat(task: FSTask, options: FSTaskOptions) throws -> Progress](./fsmanageableresourcemaintenanceoperations/startformat%28task,options%29.md)
  Starts formatting the file system with the given options.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsmanageableresourcemaintenanceoperations)*