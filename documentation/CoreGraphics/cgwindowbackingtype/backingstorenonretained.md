# CGWindowBackingType.backingStoreNonretained

**Framework**: Core Graphics  
**Kind**: case

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
case backingStoreNonretained
```

#### Discussion

The window draws directly to the screen without using any buffer.

You should typically not use this mode. It exists primarily for use in the original Classic Blue Box. It does not support Quartz drawing, alpha blending, or opacity. Moreover, it does not support hardware acceleration, and interferes with system-wide display acceleration. If you use this mode, your application must manage visibility region clipping itself, and manage repainting on visibility changes.

## See Also

- [CGWindowBackingType.backingStoreBuffered](cgwindowbackingtype/backingstorebuffered.md)
- [CGWindowBackingType.backingStoreRetained](cgwindowbackingtype/backingstoreretained.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowbackingtype/backingstorenonretained)*