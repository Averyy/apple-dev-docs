# revertAssetContent(to:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Reverts the asset’s content to its original, choosing which original resource to use as the unadjusted base for all renders.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func revertAssetContent(to choice: PHAsset.OriginalResourceChoice)
```

```objc
- (void) revertAssetContentToOriginalResourceChoice:(PHOriginalResourceChoice) choice;
```

## Discussion

In addition to reverting all adjustments, this selects either the RAW ([`PHAsset.OriginalResourceChoice.raw`](../phasset/originalresourcechoice-swift.enum/raw.md)) or the compressed ([`PHAsset.OriginalResourceChoice.compressed`](../phasset/originalresourcechoice-swift.enum/compressed.md)) resource as the source for all renders. This applies to RAW+JPEG assets only. Using this with other types of assets is not supported.

## Parameters

- `choice`: The original resource to use as the unadjusted base after reverting.

## See Also

### Editing Asset Content
- [var contentEditingOutput: PHContentEditingOutput?](./contenteditingoutput.md)
  The output of an asset content editing session.
- [func revertAssetContentToOriginal()](./revertassetcontenttooriginal%28%29.md)
  Request to revert any edits made to the asset’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetchangerequest/revertassetcontent(to:))*