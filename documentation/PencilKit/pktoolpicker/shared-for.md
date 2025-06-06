# shared(for:)

**Framework**: PencilKit  
**Kind**: method

Returns the tool picker object to use for the specified window.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class func shared(for window: UIWindow) -> PKToolPicker?
```

#### Return Value

The tool picker associated with the window, or `nil` if an error occurred.

#### Discussion

Call this method when you want to retrieve the tool picker assigned to one of your app’s windows. If the specified window doesn’t yet have a tool picker, this method creates and associates it with that window.

## Parameters

- `window`: A window of your app.

## See Also

- [var selectedTool: any PKTool](pktoolpicker/selectedtool-2lptq.md)
  The currently selected tool in the tool picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/shared(for:))*