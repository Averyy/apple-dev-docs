# shared(for:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Type Method

Returns the tool picker object to use for the specified window.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0
- iPadOS 13.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Create individual instances of the tool picker using [`init()`](./init%28%29.md) or [`init(toolItems:)`](./init%28toolitems%29.md) instead.

## Declaration

```swift
class func shared(for window: UIWindow) -> PKToolPicker?
```

```objc
+ (PKToolPicker *) sharedToolPickerForWindow:(UIWindow *) window;
```

## Return Value

The tool picker associated with the window, or `nil` if an error occurred.

## Discussion

Call this method when you want to retrieve the tool picker assigned to one of your app’s windows. If the specified window doesn’t yet have a tool picker, this method creates and associates it with that window.

## Parameters

- `window`: A window of your app.

## See Also

### Deprecated
- [var selectedTool: any PKTool](./selectedtool-2lptq.md)
  The currently selected tool in the tool picker.
- [selectedTool](./selectedtool-93ikc.md)
  The currently selected tool in the tool picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/shared(for:))*