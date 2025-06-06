# NSWindow.BackingStoreType.retained

**Framework**: AppKit  
**Kind**: case

The window uses a buffer, but draws directly to the screen where possible and to the buffer for obscured portions.

**Availability**:
- macOS 10.0+

## Declaration

```swift
case retained
```

#### Discussion

You should not use this mode. It combines the limitations of `NSBackingStoreNonretained` with the memory use of `NSBackingStoreBuffered`. The original NeXTSTEP implementation was an interesting compromise that worked well with fast memory mapped framebuffers on the CPU bus—something that hasn’t been in general use since around 1994. These tend to have performance problems.

In macOS 10.5 and later, requests for retained windows will result in the window system creating a buffered window, as that better matches actual use.

## See Also

- [NSWindow.BackingStoreType.nonretained](nswindow/backingstoretype/nonretained.md)
  The window draws directly to the screen without using any buffer.
- [NSWindow.BackingStoreType.buffered](nswindow/backingstoretype/buffered.md)
  The window renders all drawing into a display buffer and then flushes it to the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/backingstoretype/retained)*