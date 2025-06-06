# NSWindow.BackingStoreType.nonretained

**Framework**: AppKit  
**Kind**: case

The window draws directly to the screen without using any buffer.

**Availability**:
- macOS 10.0+

## Declaration

```swift
case nonretained
```

#### Discussion

You should not use this mode. It exists primarily for use in the original Classic Blue Box. It does not support Quartz drawing, alpha blending, or opacity. Moreover, it does not support hardware acceleration, and interferes with system-wide display acceleration. If you use this mode, your application must manage visibility region clipping itself, and manage repainting on visibility changes.

## See Also

- [NSWindow.BackingStoreType.retained](nswindow/backingstoretype/retained.md)
  The window uses a buffer, but draws directly to the screen where possible and to the buffer for obscured portions.
- [NSWindow.BackingStoreType.buffered](nswindow/backingstoretype/buffered.md)
  The window renders all drawing into a display buffer and then flushes it to the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/backingstoretype/nonretained)*