# imageBrowser(_:cellWasDoubleClickedAt:)

**Framework**: Objective-C Runtime  
**Kind**: method

Performs custom tasks when the user double-clicks an item in the image browser view.

**Availability**:
- macOS ?+

## Declaration

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, cellWasDoubleClickedAt index: Int)
```

#### Discussion

This method signals that the user double-clicked an item in the image browser view. You can implement this method if you want to perform custom tasks at that time.

## Parameters

- `aBrowser`: An image browser view.
- `index`: The index of the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:cellwasdoubleclickedat:))*