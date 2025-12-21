# shouldCloseWithWindow

**Framework**: Quick Look UI  
**Kind**: property

A Boolean value that determines whether the preview should close when its window closes.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var shouldCloseWithWindow: Bool { get set }
```

#### Discussion

The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), which means that the preview automatically closes when its window closes. If you set this property to [`false`](https://developer.apple.com/documentation/Swift/false), close the preview by calling the [`close()`](qlpreviewview/close().md) method when finished with it. Once you close a [`QLPreviewView`](qlpreviewview.md), it won’t accept any more preview items.

## See Also

- [func close()](qlpreviewview/close.md)
  Closes the view, releasing the current preview item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewview/shouldclosewithwindow)*