# itemType(for:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the Uniform Type Identifier (UTI) of the item.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func itemType(for csc: UICloudSharingController) -> String?
```

#### Discussion

[`UICloudSharingController`](uicloudsharingcontroller.md) uses the UTI to determine if the shared item is a special type. This allows text presented by the controller to refer to the item using descriptive wording. For example, if the shared item is a presentation and `kUTTypePresentation` is returned, the screens refer to the shared item as a . Likewise, if the shared item is a document and `kUTTypeContent` is returned, the screens refer to the item as a . And when `kUTTypeSpreadsheet` is returned, the screens refer to the item as a .

For types unique to your app, return `nil` or do not implement this method.

## See Also

- [func itemTitle(for: UICloudSharingController) -> String?](uicloudsharingcontrollerdelegate/itemtitle(for:).md)
  Asks the delegate for the title to display on the invitation screen.
- [func itemThumbnailData(for: UICloudSharingController) -> Data?](uicloudsharingcontrollerdelegate/itemthumbnaildata(for:).md)
  Asks the delegate for the thumbnail image data to display on the invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/itemtype(for:))*