# collectionView(_:shouldSpringLoadItemAt:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Determines whether the spring-loading interaction effect is displayed for the specified item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, shouldSpringLoadItemAt indexPath: IndexPath, with context: any UISpringLoadedInteractionContext) -> Bool
```

```objc
- (BOOL) collectionView:(UICollectionView *) collectionView shouldSpringLoadItemAtIndexPath:(NSIndexPath *) indexPath withContext:(id<UISpringLoadedInteractionContext>) context;
```

#### Return Value

[`true`](../../Swift/true.md) to apply the spring-loading behavior for the item or [`false`](../../Swift/false.md) to suppress the behavior altogether.

#### Discussion

If you do not implement this method, the collection view assumes a return value of [`true`](../../Swift/true.md).

## Parameters

- `collectionView`: The collection view object notifying you of the interaction.
- `indexPath`: The index path of the item for which the spring-loading behavior applies.
- `context`: A context object containing information about the item and view on which to display the spring-loading interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate/collectionview(_:shouldspringloaditemat:with:))*