# setIsMiniaturized(_:)

**Framework**: AppKit  
**Kind**: method

Sets the window’s miniaturized state to the value you specify.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setIsMiniaturized(_ flag: Bool)
```

#### Discussion

Depending on the current miniaturized state and the value of `flag`, the window may minimize to the Dock or expand from the Dock.

## See Also

- [func setIsVisible(Bool)](nswindow/setisvisible(_:).md)
  Sets the window’s visible state to the value you specify.
- [func setIsZoomed(Bool)](nswindow/setiszoomed(_:).md)
  Sets the window’s zoomed state to the value you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/setisminiaturized(_:))*