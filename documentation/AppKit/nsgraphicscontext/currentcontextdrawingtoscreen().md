# currentContextDrawingToScreen()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the current context is drawing to the screen.

**Availability**:
- macOS

## Declaration

```swift
class func currentContextDrawingToScreen() -> Bool
```

```objc
+ (BOOL) currentContextDrawingToScreen;
```

## Return Value

[`true`](../../Swift/true.md) if the current context is drawing to the screen, otherwise [`false`](../../Swift/false.md).

## Discussion

This convenience method is equivalent to sending [`isDrawingToScreen`](./isdrawingtoscreen.md) to the result of [`current`](./current.md).

## See Also

### Testing the Drawing Destination
- [var isDrawingToScreen: Bool](./isdrawingtoscreen.md)
  A Boolean value that indicates whether the drawing destination is the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/currentcontextdrawingtoscreen())*