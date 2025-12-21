# updateWindowsRunLoopOrdering

**Framework**: AppKit  
**Kind**: property

Run-loop message priority for handling window updates.

**Availability**:
- macOS ?+

## Declaration

```swift
class var updateWindowsRunLoopOrdering: Int { get }
```

#### Discussion

This constant is used by the [`RunLoop`](https://developer.apple.com/documentation/Foundation/RunLoop) method [`perform(_:target:argument:order:modes:)`](https://developer.apple.com/documentation/Foundation/RunLoop/perform(_:target:argument:order:modes:)).

## See Also

- [class var displayWindowRunLoopOrdering: Int](nsapplication/displaywindowrunloopordering.md)
  The priority at which windows are displayed.
- [class var resetCursorRectsRunLoopOrdering: Int](nsapplication/resetcursorrectsrunloopordering.md)
  The priority at which cursor rects are reset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/updatewindowsrunloopordering)*