# IOEventLink

**Framework**: DriverKit  
**Kind**: class

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
class IOEventLink;
```

#### Overview

IOEventLink allows for fast IPC, suitable for realtime applications.

Applications that open user clients to a DriverKit driver can set up an eventlink for fast signaling.

To configure an eventlink, the application will have to first create an eventlink object with os_eventlink_create() (see <os/eventlink_private.h>). The application then has to extract the remote eventlink port with os_eventlink_extract_remote_port(). To send the remote eventlink port to the driver, use:

const char * name = “Event Link Name”; // This must match the name the driver used in IOEventLink::Create(). kern_return_t ret = IOConnectTrap3(connect, // user client connection (io_connect_t) 0, // specifies event link configuration trap (uintptr_t)name, (uintptr_t)strlen(name), (uintptr_t)remotePort // port from os_eventlink_extract_remote_port );

Once the remote eventlink port has been sent to the driver, the driver should be notified with a user-defined external method or other existing signaling mechanism. The driver should handle this by activating the IOEventLink with Activate().

## Topics

### Instance Methods
- [Activate](ioeventlink/activate.md)
- [Associate](ioeventlink/associate.md)
- [Cancel](ioeventlink/cancel.md)
- [Disassociate](ioeventlink/disassociate.md)
- [Invalidate](ioeventlink/invalidate.md)
- [Signal](ioeventlink/signal.md)
- [SignalAndWait](ioeventlink/signalandwait.md)
- [SignalAndWaitUntil](ioeventlink/signalandwaituntil.md)
- [Wait](ioeventlink/wait.md)
- [WaitUntil](ioeventlink/waituntil.md)
- [free](ioeventlink/free.md)
- [init](ioeventlink/init.md)
### Type Methods
- [Create](ioeventlink/create.md)

## Relationships

### Inherits From
- [OSObject](osobject.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioeventlink)*