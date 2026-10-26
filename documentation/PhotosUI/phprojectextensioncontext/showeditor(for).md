# showEditor(for:)

**Framework**: PhotosUI  
**Kind**: method  
**Role**: Instance Method

Invokes the built-in photo editor for the given asset.

**Availability**:
- macOS 10.14+

## Declaration

```swift
func showEditor(for asset: PHAsset)
```

```objc
- (void) showEditorForAsset:(PHAsset *) asset;
```

#### Discussion

To be notified when assets are edited, the extension should observe library changes by implementing the [`PHPhotoLibraryChangeObserver`](https://developer.apple.com/documentation/photos/phphotolibrarychangeobserver) protocol.

## Parameters

- `asset`: The asset to edit.

## See Also

### Updating Assets
- [func updatedProjectInfo(from: PHProjectInfo?, completion: (PHProjectInfo?) -> Void) -> Progress](./updatedprojectinfo%28from,completion%29.md)
  Creates an updated [`PHProjectInfo`](../phprojectinfo.md) instance from existing project information and current assets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phprojectextensioncontext/showeditor(for:))*