# imageBrowser(_:backgroundWasRightClickedWith:)

**Framework**: Objective-C Runtime  
**Kind**: method

Performs custom tasks when the user right-clicks the image browser view background.

**Availability**:
- macOS ?+

## Declaration

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, backgroundWasRightClickedWith event: NSEvent!)
```

#### Discussion

This method signals  that the user either right-clicked the background or left-clicked it with the Alt key pressed. You can implement this method if you want to perform custom tasks at that time.

## Parameters

- `aBrowser`: An image browser view.
- `event`: The event that invoked the method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:backgroundwasrightclickedwith:))*