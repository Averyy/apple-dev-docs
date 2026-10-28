# prepareThumbnail(of:completionHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates a thumbnail image at the specified size asynchronously on a background thread.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func prepareThumbnail(of size: CGSize, completionHandler: @escaping @Sendable (UIImage?) -> Void)
```

```swift
func byPreparingThumbnail(ofSize size: CGSize) async -> UIImage?
```

```objc
- (void) prepareThumbnailOfSize:(CGSize) size completionHandler:(void (^)(UIImage *)) completionHandler;
```

## Discussion

When displaying an image in a [`UIImageView`](../uiimageview.md), you can use the view’s [`contentMode`](../uiview/contentmode-swift.property.md) property to clip or scale the image automatically. But when the native image size is much larger than the bounds of the view, decoding the full size image creates unnecessary memory overhead. By creating a thumbnail image at a specified size with this method, you avoid the overhead of decoding the image at its full size.

This method asynchronously creates the thumbnail image on a background thread and calls the completion handler on that thread. If your app updates the UI in the completion handler, schedule the UI update on the main thread.

**Swift**:

```swift
func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
    guard let cell = collectionView.dequeueReusableCell(withReuseIdentifier: cellIdentifier, for: indexPath) as? ItemCell else {
        fatalError("Unexpected type for cell. Check configuration.")
    }
        
    let item = items[indexPath.item]
    cell.nameLabel?.text = item.name
    item.image.prepareThumbnail(of: thumbnailSize) { thumbnail in
        DispatchQueue.main.async {
            cell.thumbnailImageView?.image = thumbnail
        }
    }
    return cell
}
```

**Objective-C**:

```objc
- (UICollectionViewCell *)collectionView:(UICollectionView *)collectionView cellForItemAtIndexPath:(NSIndexPath *)indexPath {
    UICollectionViewCell *cell = [collectionView dequeueReusableCellWithReuseIdentifier:self.cellIdentifier forIndexPath:indexPath];
    NSAssert([cell isKindOfClass:[ItemCell class]], @"Unexpected type for cell. Check configuration.\n");
    
    Item *item = self.items[indexPath.row];
    ItemCell *itemCell = (ItemCell *)cell;
    itemCell.nameLabel.text = item.name;
    [item.image prepareThumbnailOfSize:self.thumbnailSize completionHandler:^(UIImage *thumbnail) {
        dispatch_async(dispatch_get_main_queue(), ^{
            itemCell.thumbnailImageView.image = thumbnail;
        });
    }];
    return cell;
}
```

## Parameters

- `size`: The desired size of the thumbnail.
- `completionHandler`: The completion handler to call when the thumbnail is ready. The handler executes on a background thread.

  The completion handler takes the following parameters:

  - **`thumbnail`**: A new thumbnail image. This parameter is `nil` if the original image isn’t backed by a [`CGImage`](../../CoreGraphics/cgimage.md) or if the image data is corrupt or malformed.

## See Also

### Loading images for display
- [func preparingForDisplay() -> UIImage?](./preparingfordisplay%28%29.md)
  Decodes an image synchronously and provides a new one for display in views and animations.
- [func prepareForDisplay(completionHandler: (UIImage?) -> Void)](./preparefordisplay%28completionhandler%29.md)
  Decodes an image asynchronously and provides a new one for display in views and animations.
- [func preparingThumbnail(of: CGSize) -> UIImage?](./preparingthumbnail%28of%29.md)
  Returns a new thumbnail image at the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/preparethumbnail(of:completionhandler:))*