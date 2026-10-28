# allocWithZone:

**Framework**: Foundation  
**Role**: Article

Returns an instance of the `NSMachPort` class.

## Overview

For backward compatibility on Mach, [allocWithZone:](./nsport-allocwithzone.md) returns an instance of the `NSMachPort` class when sent to the `NSPort` class. Otherwise, it returns an instance of a concrete subclass that can be used for messaging between threads or processes on the local machine, or, in the case of `NSSocketPort`, between processes on separate machines.

## See Also

### Related Documentation
- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [Distributed Objects Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)
### Creating instances
- [+ port](./nsport/port.md)
  Creates and returns a new `NSPort` object capable of both sending and receiving messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsport-allocwithzone)*