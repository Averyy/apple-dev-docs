# updateWindowsRunLoopOrdering

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Run-loop message priority for handling window updates.

**Availability**:
- macOS

## Declaration

```swift
class var updateWindowsRunLoopOrdering: Int { get }
```

```c
NSUpdateWindowsRunLoopOrdering
```

## Discussion

This constant is used by the [`RunLoop`](../../Foundation/runloop.md) method [`perform(_:target:argument:order:modes:)`](../../Foundation/runloop/perform%28_,target,argument,order,modes%29.md).

## See Also

### Managing Run Loops
- [class var displayWindowRunLoopOrdering: Int](./displaywindowrunloopordering.md)
  The priority at which windows are displayed.
- [class var resetCursorRectsRunLoopOrdering: Int](./resetcursorrectsrunloopordering.md)
  The priority at which cursor rects are reset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/updatewindowsrunloopordering)*