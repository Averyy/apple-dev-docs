# NSWindow.BackingStoreType.buffered

**Framework**: AppKit  
**Kind**: case

The window renders all drawing into a display buffer and then flushes it to the screen.

**Availability**:
- macOS ?+

## Declaration

```swift
case buffered
```

#### Discussion

You should use this mode. It supports hardware acceleration, Quartz drawing, and takes advantage of the GPU when possible. It also supports alpha channel drawing, opacity controls, using the compositor.

## See Also

- [NSWindow.BackingStoreType.retained](nswindow/backingstoretype/retained.md)
  The window uses a buffer, but draws directly to the screen where possible and to the buffer for obscured portions.
- [NSWindow.BackingStoreType.nonretained](nswindow/backingstoretype/nonretained.md)
  The window draws directly to the screen without using any buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/backingstoretype/buffered)*