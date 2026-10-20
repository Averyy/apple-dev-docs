# FSSyncFlags.wait

**Framework**: FSKit  
**Kind**: case  
**Role**: Case

A flag for synchronized I/O with file-integrity completion.

**Availability**:
- macOS 15.4+

## Declaration

```swift
case wait
```

```c
FSSyncFlagsWait
```

## See Also

### Declaring synchronization behaviors
- [FSSyncFlags.noWait](./nowait.md)
  A flag for synchronized I/O that starts I/O but doesn’t wait for it.
- [FSSyncFlags.dWait](./dwait.md)
  A flag for synchronized I/O with data-integrity completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fssyncflags/wait)*