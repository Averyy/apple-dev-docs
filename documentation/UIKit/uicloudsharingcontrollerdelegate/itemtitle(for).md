# itemTitle(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the delegate for the title to display on the invitation screen.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func itemTitle(for csc: UICloudSharingController) -> String?
```

```objc
- (NSString *) itemTitleForCloudSharingController:(UICloudSharingController *) csc;
```

## Discussion

Implement this method to provide a meaningful title to the [`UICloudSharingController`](../uicloudsharingcontroller.md) invitation screen.

[`itemTitle(for:)`](./itemtitle%28for%29.md) is called only when creating a new share. For an existing share, the title is retrieved from the share using the [`CKShareTitleKey`](../../CloudKit/cksharetitlekey-9yavd.md) key, which is set when a new share is saved.

**Swift**:

```swift
func itemTitle(for csc: UICloudSharingController) -> String? {
  return "Untitled"
}
```

**Objective-C**:

```objc
- (nullable NSString *)itemTitleForCloudSharingController:(UICloudSharingController *)csc
{
  return @"Untitled";
}
```

## See Also

### Configuring the view controller
- [func itemType(for: UICloudSharingController) -> String?](./itemtype%28for%29.md)
  Asks the delegate for the Uniform Type Identifier (UTI) of the item.
- [func itemThumbnailData(for: UICloudSharingController) -> Data?](./itemthumbnaildata%28for%29.md)
  Asks the delegate for the thumbnail image data to display on the invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/itemtitle(for:))*