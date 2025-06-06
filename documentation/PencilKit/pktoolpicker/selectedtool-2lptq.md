# selectedTool

**Framework**: PencilKit  
**Kind**: property

The currently selected tool in the tool picker.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
var selectedTool: any PKTool { get set }
```

#### Discussion

This is one of the available tools associated with a [`PKCanvasView`](pkcanvasview.md) that adopt the [`PKTool`](pktool-swift.protocol.md) protocol.

## See Also

- [class func shared(for: UIWindow) -> PKToolPicker?](pktoolpicker/shared(for:).md)
  Returns the tool picker object to use for the specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/selectedtool-2lptq)*