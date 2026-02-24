# preparingThumbnail(of:)

**Framework**: UIKit  
**Kind**: method

Returns a new thumbnail image at the specified size.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func preparingThumbnail(of size: CGSize) -> UIImage?
```

#### Return Value

A new thumbnail image. Returns `nil` if the original image isn’t backed by a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) or if the image data is corrupt or malformed.

#### Discussion

When displaying an image in a [`UIImageView`](uiimageview.md), you can use the view’s [`contentMode`](uiview/contentmode-swift.property.md) property to clip or scale the image automatically. But when the native image size is much larger than the bounds of the view, decoding the full size image creates unnecessary memory overhead. By creating a thumbnail image at a specified size with this method, you avoid the overhead of decoding the image at its full size.

**Swift**:

```swift
func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
    guard let cell = collectionView.dequeueReusableCell(withReuseIdentifier: cellIdentifier, for: indexPath) as? ItemCell else {
        fatalError("Unexpected type for cell. Check configuration.")
    }
        
    let item = items[indexPath.item]
    cell.nameLabel?.text = item.name
    let thumbnail = item.image.preparingThumbnail(of: thumbnailSize)
    cell.thumbnailImageView?.image = thumbnail
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
    UIImage *thumbnail = [item.image imageByPreparingThumbnailOfSize:self.thumbnailSize];
    itemCell.thumbnailImageView.image = thumbnail;
    return cell;
}
```

## Parameters

- `size`: The desired size of the thumbnail.

## See Also

- [func preparingForDisplay() -> UIImage?](uiimage/preparingfordisplay.md)
  Decodes an image synchronously and provides a new one for display in views and animations.
- [func prepareForDisplay(completionHandler: (UIImage?) -> Void)](uiimage/preparefordisplay(completionhandler:).md)
  Decodes an image asynchronously and provides a new one for display in views and animations.
- [func prepareThumbnail(of: CGSize, completionHandler: (UIImage?) -> Void)](uiimage/preparethumbnail(of:completionhandler:).md)
  Creates a thumbnail image at the specified size asynchronously on a background thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/preparingthumbnail(of:))*