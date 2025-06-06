# PKToolPickerObserver

**Framework**: PencilKit  
**Kind**: protocol

An interface you use to detect when the user changes the selected tools and drawing characteristics of a tool picker object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol PKToolPickerObserver : NSObjectProtocol
```

#### Overview

Implement the methods of [`PKToolPickerObserver`](pktoolpickerobserver.md) to detect when the user changes the configuration of a [`PKToolPicker`](pktoolpicker.md) view. Each time the user changes the selected tool or other drawing characteristics, the tool picker notifies any registered observers. You use these notifications to update the configuration of the underlying canvas.

To register an observer with a tool picker, call the [`addObserver(_:)`](pktoolpicker/addobserver(_:).md) method of the [`PKToolPicker`](pktoolpicker.md) object.

## Topics

### Detecting tool configuration changes
- [func toolPickerSelectedToolItemDidChange(PKToolPicker)](pktoolpickerobserver/toolpickerselectedtoolitemdidchange(_:).md)
  Tells the observer when a person selects a new tool item.
- [func toolPickerIsRulerActiveDidChange(PKToolPicker)](pktoolpickerobserver/toolpickerisruleractivedidchange(_:).md)
  Tells the observer when a person shows or hides the ruler.
### Monitoring visibility changes
- [func toolPickerVisibilityDidChange(PKToolPicker)](pktoolpickerobserver/toolpickervisibilitydidchange(_:).md)
  Tells the observer when a person shows or hides the tool picker.
- [func toolPickerFramesObscuredDidChange(PKToolPicker)](pktoolpickerobserver/toolpickerframesobscureddidchange(_:).md)
  Tells the observer when the area that the tool picker obscures changes.
### Deprecated
- [func toolPickerSelectedToolDidChange(PKToolPicker)](pktoolpickerobserver/toolpickerselectedtooldidchange(_:).md)
  Tells the observer when a person selects a new tool.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [PKCanvasView](pkcanvasview.md)

## See Also

- [func addObserver(any PKToolPickerObserver)](pktoolpicker/addobserver(_:).md)
  Adds the specified object to the list of objects to notify when the picker configuration changes.
- [func removeObserver(any PKToolPickerObserver)](pktoolpicker/removeobserver(_:).md)
  Removes the specified object from the list of objects to notify when the picker configuration changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickerobserver)*