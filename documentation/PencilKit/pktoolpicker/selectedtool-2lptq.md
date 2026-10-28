# selectedTool

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

The currently selected tool in the tool picker.

**Availability**:
- iOS 13.0+ - Deprecated in 18.0
- iPadOS 13.0+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use [`selectedToolItem`](./selectedtoolitem.md) instead.

## Declaration

```swift
var selectedTool: any PKTool { get set }
```

## Discussion

This is one of the available tools associated with a [`PKCanvasView`](../pkcanvasview.md) that adopt the [`PKTool`](../pktool-swift.protocol.md) protocol.

## See Also

### Deprecated
- [class func shared(for: UIWindow) -> PKToolPicker?](./shared%28for%29.md)
  Returns the tool picker object to use for the specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/selectedtool-2lptq)*