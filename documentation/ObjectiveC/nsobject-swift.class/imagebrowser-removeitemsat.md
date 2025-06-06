# imageBrowser(_:removeItemsAt:)

**Framework**: Objective-C Runtime  
**Kind**: method

Signals that a remove operation should be applied to the specified items.

**Availability**:
- macOS ?+

## Declaration

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, removeItemsAt indexes: IndexSet!)
```

#### Discussion

This method is optional. It is invoked by the image browser after  Image Kit determines  that a remove operation should be applied. In response, the data source should update itself by removing the specified items.

## Parameters

- `aBrowser`: An image browser view.
- `indexes`: The indexes of the items that should be removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:removeitemsat:))*