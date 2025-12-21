# allocWithZone:

**Framework**: Foundation

Returns an instance of the `NSMachPort` class.

#### Overview

For backward compatibility on Mach, doc:nsport/1807189-allocwithzone returns an instance of the `NSMachPort` class when sent to the `NSPort` class. Otherwise, it returns an instance of a concrete subclass that can be used for messaging between threads or processes on the local machine, or, in the case of `NSSocketPort`, between processes on separate machines.

## See Also

- [Threading Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [Distributed Objects Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/1807189-allocwithzone)*