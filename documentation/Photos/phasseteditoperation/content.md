# PHAssetEditOperation.content

**Framework**: Photos  
**Kind**: case  
**Role**: Case

The asset’s photo or video content can be edited.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
case content
```

```c
PHAssetEditOperationContent
```

## Discussion

To begin the process of editing an asset, use the [`requestContentEditingInput(with:completionHandler:)`](../phasset/requestcontenteditinginput%28with,completionhandler%29.md) method.

## See Also

### Constants
- [PHAssetEditOperation.delete](./delete.md)
  The asset can be deleted from the photo library.
- [PHAssetEditOperation.properties](./properties.md)
  The asset’s metadata properties can be edited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasseteditoperation/content)*