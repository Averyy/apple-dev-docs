# itemThumbnailData(for:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the thumbnail image data to display on the invitation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func itemThumbnailData(for csc: UICloudSharingController) -> Data?
```

#### Discussion

Implement this method to return image data representing the shared recording. Returning `nil` tells the [`UICloudSharingController`](uicloudsharingcontroller.md) instance to display the generic image. Not implementing this method is the same as returning `nil`.

[`itemThumbnailData(for:)`](uicloudsharingcontrollerdelegate/itemthumbnaildata(for:).md) is called only when creating a new share. For an existing share, the thumbnail image is retrieved from the share using the [`CKShareThumbnailImageDataKey`](https://developer.apple.com/documentation/CloudKit/CKShareThumbnailImageDataKey-1rxdx) key.

The following code shows an example of retrieving the image data from a data set stored in an asset catalog found in the main bundle.

```swift
- (nullable NSData *)itemThumbnailDataForCloudSharingController:(UICloudSharingController *)csc
{  
  NSDataAsset *icon = [[NSDataAsset alloc] initWithName:@"thumbnail"];
  return [icon data];
}
```

## See Also

- [func itemTitle(for: UICloudSharingController) -> String?](uicloudsharingcontrollerdelegate/itemtitle(for:).md)
  Asks the delegate for the title to display on the invitation screen.
- [func itemType(for: UICloudSharingController) -> String?](uicloudsharingcontrollerdelegate/itemtype(for:).md)
  Asks the delegate for the Uniform Type Identifier (UTI) of the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/itemthumbnaildata(for:))*