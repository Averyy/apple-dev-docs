# NSWindow.BackingStoreType.buffered

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The window renders all drawing into a display buffer and then flushes it to the screen.

**Availability**:
- macOS

## Declaration

```swift
case buffered
```

```c
NSBackingStoreBuffered
```

#### Discussion

You should use this mode. It supports hardware acceleration, Quartz drawing, and takes advantage of the GPU when possible. It also supports alpha channel drawing, opacity controls, using the compositor.

## See Also

### Constants
- [NSWindow.BackingStoreType.retained](./retained.md)
  The window uses a buffer, but draws directly to the screen where possible and to the buffer for obscured portions.
- [NSWindow.BackingStoreType.nonretained](./nonretained.md)
  The window draws directly to the screen without using any buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/backingstoretype/buffered)*