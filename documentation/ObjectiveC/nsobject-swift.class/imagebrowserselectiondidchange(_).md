# imageBrowserSelectionDidChange(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Performs custom tasks when the selection changes.

**Availability**:
- macOS

## Declaration

```swift
func imageBrowserSelectionDidChange(_ aBrowser: IKImageBrowserView!)
```

```objc
- (void) imageBrowserSelectionDidChange:(IKImageBrowserView *) aBrowser;
```

## Discussion

This method signals that the user changes the selection in the image browser view. You can implement this method if you want to perform custom tasks at that time.

## Parameters

- `aBrowser`: An image browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowserselectiondidchange(_:))*