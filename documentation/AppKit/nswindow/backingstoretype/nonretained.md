# NSWindow.BackingStoreType.nonretained

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

The window draws directly to the screen without using any buffer.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13 (renamed: NSWindow.BackingStoreType.buffered)

## Declaration

```swift
case nonretained
```

```c
NSBackingStoreNonretained
```

## Discussion

You should not use this mode. It exists primarily for use in the original Classic Blue Box. It does not support Quartz drawing, alpha blending, or opacity. Moreover, it does not support hardware acceleration, and interferes with system-wide display acceleration. If you use this mode, your application must manage visibility region clipping itself, and manage repainting on visibility changes.

## See Also

### Constants
- [NSWindow.BackingStoreType.buffered](./buffered.md)
  The window renders all drawing into a display buffer and then flushes it to the screen.
- [NSWindow.BackingStoreType.retained](./retained.md)
  The window uses a buffer, but draws directly to the screen where possible and to the buffer for obscured portions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/backingstoretype/nonretained)*