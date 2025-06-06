# imageBrowser(_:itemAt:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns an object for the item in an image browser view that corresponds to the specified index.

**Availability**:
- macOS ?+

## Declaration

```swift
func imageBrowser(_ aBrowser: IKImageBrowserView!, itemAt index: Int) -> Any!
```

#### Return Value

An `IKImageBrowserItem` object.

#### Discussion

Your data source must implement this method. The returned object must implement the required methods of the IKImageBrowserItem protocol.

## Parameters

- `aBrowser`: An image browser view.
- `index`: The index of the item you want to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/imagebrowser(_:itemat:))*