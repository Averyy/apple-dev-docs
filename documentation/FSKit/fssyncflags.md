# FSSyncFlags

**Framework**: FSKit  
**Kind**: enum

Behavior flags for use with synchronization calls.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum FSSyncFlags
```

#### Overview

These values are based on flags defined in `mount.h`. Since there are system-defined flags that are valid in the kernel but not in FSKit, this type defines its members as options rather than use an enumeration.

## Topics

### Declaring synchronization behaviors
- [FSSyncFlags.wait](fssyncflags/wait.md)
  A flag for synchronized I/O with file-integrity completion.
- [FSSyncFlags.noWait](fssyncflags/nowait.md)
  A flag for synchronized I/O that starts I/O but doesn’t wait for it.
- [FSSyncFlags.dWait](fssyncflags/dwait.md)
  A flag for synchronized I/O with data-integrity completion.
### Initializers
- [init?(rawValue: Int)](fssyncflags/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func synchronize(flags: FSSyncFlags, replyHandler: ((any Error)?) -> Void)](fsvolume/operations/synchronize(flags:replyhandler:).md)
  Synchronizes the volume with its underlying resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fssyncflags)*