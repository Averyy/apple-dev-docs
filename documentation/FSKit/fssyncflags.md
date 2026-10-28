# FSSyncFlags

**Framework**: FSKit  
**Kind**: enum  
**Role**: Enumeration

Behavior flags for use with synchronization calls.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum FSSyncFlags
```

```c
enum FSSyncFlags : NSInteger;
```

## Overview

These values are based on flags defined in `mount.h`. Since there are system-defined flags that are valid in the kernel but not in FSKit, this type defines its members as options rather than use an enumeration.

## Topics

### Declaring synchronization behaviors
- [FSSyncFlags.wait](./fssyncflags/wait.md)
  A flag for synchronized I/O with file-integrity completion.
- [FSSyncFlags.noWait](./fssyncflags/nowait.md)
  A flag for synchronized I/O that starts I/O but doesn’t wait for it.
- [FSSyncFlags.dWait](./fssyncflags/dwait.md)
  A flag for synchronized I/O with data-integrity completion.
### Initializers
- [init?(rawValue: Int)](./fssyncflags/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Performing synchronization
- [func synchronize(flags: FSSyncFlags, replyHandler: ((any Error)?) -> Void)](./fsvolume/handler/synchronize%28flags,replyhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fssyncflags)*