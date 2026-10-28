# setIsMiniaturized(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the window’s miniaturized state to the value you specify.

**Availability**:
- macOS

## Declaration

```swift
func setIsMiniaturized(_ flag: Bool)
```

```objc
- (void) setIsMiniaturized:(BOOL) flag;
```

## Discussion

Depending on the current miniaturized state and the value of `flag`, the window may minimize to the Dock or expand from the Dock.

## See Also

### Setting Scripting Attributes
- [func setIsVisible(Bool)](./setisvisible%28_%29.md)
  Sets the window’s visible state to the value you specify.
- [func setIsZoomed(Bool)](./setiszoomed%28_%29.md)
  Sets the window’s zoomed state to the value you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/setisminiaturized(_:))*