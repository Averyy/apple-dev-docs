# Common Mode Flag

**Framework**: Core Foundation

A run loop pseudo-mode that manages objects monitored in the “common” modes.

#### Overview

Run loops never run in this mode. This pseudo-mode is used only as a special set of sources, timers, and observers that is shared by other modes. See Managing Observers for more details.

## Topics

### Constants
- [static let commonModes: CFRunLoopMode!](cfrunloopmode/commonmodes.md)
  Objects added to a run loop using this value as the mode are monitored by all run loop modes that have been declared as a member of the set of “common” modes with [`CFRunLoopAddCommonMode(_:_:)`](cfrunloopaddcommonmode(_:_:).md).

## See Also

- [CFRunLoopRunInMode Exit Codes](cfrunloopruninmode_exit_codes.md)
  Return codes for `CFRunLoopRunInMode`, identifying the reason the run loop exited.
- [Default Run Loop Mode](default-run-loop-mode.md)
  Default run loop mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/common-mode-flag)*