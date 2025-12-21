# itemTitle(for:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Asks the delegate for the title to display on the invitation screen.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func itemTitle(for csc: UICloudSharingController) -> String?
```

#### Discussion

Implement this method to provide a meaningful title to the [`UICloudSharingController`](uicloudsharingcontroller.md) invitation screen.

[`itemTitle(for:)`](uicloudsharingcontrollerdelegate/itemtitle(for:).md) is called only when creating a new share. For an existing share, the title is retrieved from the share using the [`CKShareTitleKey`](https://developer.apple.com/documentation/CloudKit/CKShareTitleKey-9yavd) key, which is set when a new share is saved.

## See Also

- [func itemType(for: UICloudSharingController) -> String?](uicloudsharingcontrollerdelegate/itemtype(for:).md)
  Asks the delegate for the Uniform Type Identifier (UTI) of the item.
- [func itemThumbnailData(for: UICloudSharingController) -> Data?](uicloudsharingcontrollerdelegate/itemthumbnaildata(for:).md)
  Asks the delegate for the thumbnail image data to display on the invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/itemtitle(for:))*