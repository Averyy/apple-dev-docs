# contentEditingOutput

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The output of an asset content editing session.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var contentEditingOutput: PHContentEditingOutput? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) PHContentEditingOutput * contentEditingOutput;
```

## Mentions

- [Editing Asset Content](../../PhotoKit/editing-asset-content.md)
- [Requesting Changes to the Photo Library](../../PhotoKit/requesting-changes-to-the-photo-library.md)

## Discussion

To edit an asset’s image or video content, you must first begin a content editing session with the asset’s [`requestContentEditingInput(with:completionHandler:)`](../phasset/requestcontenteditinginput%28with,completionhandler%29.md) method. You commit a content edit by setting the [`contentEditingOutput`](./contenteditingoutput.md) property of a change request within a change block. For more information about asset content editing, see [`PHAsset`](../phasset.md).

## See Also

### Editing Asset Content
- [func revertAssetContentToOriginal()](./revertassetcontenttooriginal%28%29.md)
  Request to revert any edits made to the asset’s content.
- [func revertAssetContent(to: PHAsset.OriginalResourceChoice)](./revertassetcontent%28to%29.md)
  Reverts the asset’s content to its original, choosing which original resource to use as the unadjusted base for all renders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetchangerequest/contenteditingoutput)*