# revertAssetContentToOriginal()

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Request to revert any edits made to the asset’s content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func revertAssetContentToOriginal()
```

```objc
- (void) revertAssetContentToOriginal;
```

#### Discussion

When an asset has been edited, Photos stores multiple versions of the asset: the original version of the asset as it was first captured or imported, and the input and output of the most recent edit. (You work with asset versions when requesting to edit an asset’s content—see [`PHContentEditingInputRequestOptions`](../phcontenteditinginputrequestoptions.md).) Call this method to revert to the original version of the asset, discarding all edits.

> ❗ **Important**:  This request fails if original content for the asset is not available on the current device (for example, if iCloud Photo Library is enabled and the user has edited the asset on a different device). Use [`PHAssetResourceManager`](../phassetresourcemanager.md) to ensure that original asset content is downloaded to the current device before making this request.

## See Also

### Editing Asset Content
- [var contentEditingOutput: PHContentEditingOutput?](./contenteditingoutput.md)
  The output of an asset content editing session.
- [func revertAssetContent(to: PHAsset.OriginalResourceChoice)](./revertassetcontent%28to%29.md)
  Reverts the asset’s content to its original, choosing which original resource to use as the unadjusted base for all renders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetchangerequest/revertassetcontenttooriginal())*