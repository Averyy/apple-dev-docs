# Darwin Notification API

**Framework**: Darwin Notify  
**Role**: API Collection

##### Overview

###### Included Headers

- <sys/cdefs.h>
- <stdint.h>
- <mach/message.h>
- <Availability.h>
- <dispatch/dispatch.h>

## Topics

### Miscellaneous
- [func notify_cancel(Int32) -> UInt32](./notify_cancel%28_%29.md)
- [func notify_check(Int32, UnsafeMutablePointer<Int32>!) -> UInt32](./notify_check%28_,_%29.md)
- [func notify_get_state(Int32, UnsafeMutablePointer<UInt64>!) -> UInt32](./notify_get_state%28_,_%29.md)
- [func notify_post(UnsafePointer<CChar>!) -> UInt32](./notify_post%28_%29.md)
- [func notify_register_check(UnsafePointer<CChar>!, UnsafeMutablePointer<Int32>!) -> UInt32](./notify_register_check%28_,_%29.md)
- [func notify_register_dispatch(UnsafePointer<CChar>!, UnsafeMutablePointer<Int32>!, dispatch_queue_t!, notify_handler_t!) -> UInt32](./notify_register_dispatch%28_,_,_,_%29.md)
  Request notification delivery to a dispatch queue.
- [func notify_register_mach_port(UnsafePointer<CChar>!, UnsafeMutablePointer<mach_port_t>!, Int32, UnsafeMutablePointer<Int32>!) -> UInt32](./notify_register_mach_port%28_,_,_,_%29.md)
- [func notify_register_signal(UnsafePointer<CChar>!, Int32, UnsafeMutablePointer<Int32>!) -> UInt32](./notify_register_signal%28_,_,_%29.md)
- [func notify_resume(Int32) -> UInt32](./notify_resume%28_%29.md)
- [func notify_set_state(Int32, UInt64) -> UInt32](./notify_set_state%28_,_%29.md)
- [func notify_suspend(Int32) -> UInt32](./notify_suspend%28_%29.md)
### Constants
- [Status Codes](./status-codes.md)
- [Miscellaneous Defines](./miscellaneous-defines.md)

## See Also

### Reference
- [DarwinNotify Functions](./darwinnotify-functions.md)
- [DarwinNotify Data Types](./darwinnotify-data-types.md)
- [DarwinNotify Macros](./darwinnotify-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/darwinnotify/darwin-notification-api)*