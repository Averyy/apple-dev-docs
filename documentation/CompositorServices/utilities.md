# Utilities

**Framework**: Compositor Services  
**Role**: API Collection

Common types and utilities to manage your app’s rendering process.

## Overview

Use these functions to manage timing in your app’s render loop.

## Topics

### Putting the current thread to sleep
- [cp_time_wait_until](./cp_time_wait_until.md)
  Blocks the current thread until the specified time.
### Converting time values
- [cp_time_to_cf_time_interval](./cp_time_to_cf_time_interval.md)
  Converts a Mach absolute time value to a Core Foundation time value.
- [cp_time_t](./cp_time_t.md)
  A Mach absolute time clock value.
### Retaining and releasing types
- [cp_retain](./cp_retain.md)
  Increments the reference count of the specified object.
- [cp_release](./cp_release.md)
  Decrements the reference count of the specified object.

## See Also

### Render-loop setup
- [Layer renderer](./layer-renderer.md)
  A type that provides the Metal types and timing information you need to draw your content.
- [Frames](./frames.md)
  A type that represents a single frame of content, manages the pace of animations, and provides access to the drawable environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/utilities)*