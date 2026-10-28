# canPerform(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Returns whether the collection supports the specified editing operation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func canPerform(_ anOperation: PHCollectionEditOperation) -> Bool
```

```objc
- (BOOL) canPerformEditOperation:(PHCollectionEditOperation) anOperation;
```

## Return Value

`true` if the asset supports the specified editing operation; otherwise, `false`.

## Discussion

If an asset collection or collection list supports editing, you can create a [`PHAssetCollectionChangeRequest`](../phassetcollectionchangerequest.md) or [`PHCollectionListChangeRequest`](../phcollectionlistchangerequest.md) object inside a [`PHPhotoLibrary`](../phphotolibrary.md) change block to submit a change.

## Parameters

- `anOperation`: A bit mask of editing operations to be tested.

## See Also

### Determining Collection Capabilities
- [var canContainAssets: Bool](./cancontainassets.md)
  A Boolean value indicating whether the collection can contain assets.
- [var canContainCollections: Bool](./cancontaincollections.md)
  A Boolean value indicating whether the collection can contain other collections.
- [enum PHCollectionEditOperation](../phcollectioneditoperation.md)
  Values identifying possible actions that a collection can support, used by the [`canPerform(_:)`](./canperform%28_%29.md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phcollection/canperform(_:))*