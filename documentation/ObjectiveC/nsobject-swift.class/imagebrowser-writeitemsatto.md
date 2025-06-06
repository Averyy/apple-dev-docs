# imageBrowser(_:writeItemsAt:to:)

**Framework**: Objective-C Runtime  
**Kind**: method

Signals that a drag should begin.

**Availability**:
- macOS ?+

## Declaration

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, writeItemsAt itemIndexes: IndexSet!, to pasteboard: NSPasteboard!) -> Int
```

#### Return Value

The number of items written to the pasteboard.

#### Discussion

This method is optional. It is invoked after Image Kit determines that a drag should begin, but before the drag has been started.

## Parameters

- `aBrowser`: An image browser view.
- `itemIndexes`: The indexes of the items that should be dragged.
- `pasteboard`: The pasteboard to copy the items to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:writeitemsat:to:))*