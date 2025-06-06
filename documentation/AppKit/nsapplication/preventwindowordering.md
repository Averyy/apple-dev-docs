# preventWindowOrdering()

**Framework**: AppKit  
**Kind**: method

Suppresses the usual window ordering in handling the most recent mouse-down event.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func preventWindowOrdering()
```

#### Discussion

This method is only useful for mouse-down events when you want to prevent the window that receives the event from being ordered to the front.

## See Also

- [func arrangeInFront(Any?)](nsapplication/arrangeinfront(_:).md)
  Arranges windows listed in the Window menu in front of all other windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/preventwindowordering())*