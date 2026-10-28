# CGWindowBackingType.backingStoreBuffered

**Framework**: Core Graphics  
**Kind**: case  
**Role**: Case

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
case backingStoreBuffered
```

```c
kCGBackingStoreBuffered
```

## Discussion

The window draws into a display buffer and then flushes that buffer to the screen.

You should typically use this mode. It supports hardware acceleration, Quartz drawing, and takes advantage of the GPU when possible. It also supports alpha channel drawing, opacity controls, using the compositor.

## See Also

### Constants
- [CGWindowBackingType.backingStoreNonretained](./backingstorenonretained.md)
- [CGWindowBackingType.backingStoreRetained](./backingstoreretained.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowbackingtype/backingstorebuffered)*