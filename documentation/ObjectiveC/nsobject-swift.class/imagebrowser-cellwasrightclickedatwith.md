# imageBrowser(_:cellWasRightClickedAt:with:)

**Framework**: Objective-C Runtime  
**Kind**: method

Performs custom tasks when the user right-clicks an item in the image browser view.

**Availability**:
- macOS ?+

## Declaration

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, cellWasRightClickedAt index: Int, with event: NSEvent!)
```

#### Discussion

This method signals that the user either right-clicked an item in the browser or left-clicked the item with the Alt key pressed. You can implement this method if you want to perform custom tasks at that time.

## Parameters

- `aBrowser`: An image browser view.
- `index`: The index of the cell.
- `event`: The event that invoked the method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:cellwasrightclickedat:with:))*