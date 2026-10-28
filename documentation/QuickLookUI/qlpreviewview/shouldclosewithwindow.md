# shouldCloseWithWindow

**Framework**: Quick Look UI  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the preview should close when its window closes.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var shouldCloseWithWindow: Bool { get set }
```

```objc
@property BOOL shouldCloseWithWindow;
```

## Discussion

The default value of this property is [`true`](../../Swift/true.md), which means that the preview automatically closes when its window closes. If you set this property to [`false`](../../Swift/false.md), close the preview by calling the [`close()`](./close%28%29.md) method when finished with it. Once you close a [`QLPreviewView`](../qlpreviewview.md), it won’t accept any more preview items.

## See Also

### Closing a Preview
- [func close()](./close%28%29.md)
  Closes the view, releasing the current preview item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewview/shouldclosewithwindow)*