# close()

**Framework**: Quick Look UI  
**Kind**: method

Closes the view, releasing the current preview item.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func close()
```

#### Discussion

Once a [`QLPreviewView`](qlpreviewview.md) is closed, it won’t accept any more preview items. You only need to call this method if [`shouldCloseWithWindow`](qlpreviewview/shouldclosewithwindow.md) is set to [`false`](https://developer.apple.com/documentation/Swift/false). If you don’t close a [`QLPreviewView`](qlpreviewview.md) when you are done using it, your app will leak memory.

## See Also

- [var shouldCloseWithWindow: Bool](qlpreviewview/shouldclosewithwindow.md)
  A Boolean value that determines whether the preview should close when its window closes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewview/close())*