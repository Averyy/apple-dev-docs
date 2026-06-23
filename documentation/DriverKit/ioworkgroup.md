# IOWorkGroup

**Framework**: DriverKit  
**Kind**: class

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IOWorkGroup;
```

#### Overview

Workgroups allow multiple threads to coordinate activities for realtime operations.

Applications that open user clients to a DriverKit driver can send a workgroup to use in the driver.

The application will have to first create an workgroup object. The application then should copy the workgroup port with os_workgroup_copy_port(). To send the workgroup port to the driver, use:

const char * name = “Work Group Name”; // This must match the name the driver used in IOWorkGroup::Create(). kern_return_t ret = IOConnectTrap3(connect, // user client connection (io_connect_t) 1, // specifies event link configuration trap (uintptr_t)name, (uintptr_t)strlen(name), (uintptr_t)wgPort // port from os_workgroup_copy_port );

Once the workgroup port has been sent to the driver, the driver should be notified with a user-defined external method or other existing signaling mechanism.

## Topics

### Instance Methods
- [GetTokenSize](ioworkgroup/gettokensize.md)
- [Invalidate](ioworkgroup/invalidate.md)
- [Join](ioworkgroup/join.md)
- [Leave](ioworkgroup/leave.md)
- [free](ioworkgroup/free.md)
- [init](ioworkgroup/init.md)
### Type Methods
- [Create](ioworkgroup/create.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioworkgroup)*