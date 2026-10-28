# postToFacebook

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A type of activity that posts the provided content to the user’s wall on Facebook.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static let postToFacebook: UIActivity.ActivityType
```

```c
extern UIActivityType const UIActivityTypePostToFacebook;
```

## Discussion

When using this service, you can provide [`NSString`](../../../Foundation/nsstring.md), [`NSAttributedString`](../../../Foundation/nsattributedstring.md), [`UIImage`](../../uiimage.md), and [`NSURL`](../../../Foundation/nsurl.md) objects as data for the activity items.

## See Also

### Constants
- [static let addToHomeScreen: UIActivity.ActivityType](./addtohomescreen.md)
- [static let addToReadingList: UIActivity.ActivityType](./addtoreadinglist.md)
  A type of activity that adds the URL to Safari’s reading list.
- [static let airDrop: UIActivity.ActivityType](./airdrop.md)
  A type of activity that makes the provided content available through AirDrop.
- [static let assignToContact: UIActivity.ActivityType](./assigntocontact.md)
  A type of activity that assigns the image to a contact.
- [static let collaborationCopyLink: UIActivity.ActivityType](./collaborationcopylink.md)
- [static let collaborationInviteWithLink: UIActivity.ActivityType](./collaborationinvitewithlink.md)
- [static let copyToPasteboard: UIActivity.ActivityType](./copytopasteboard.md)
  A type of activity that posts the provided content to the pasteboard.
- [static let mail: UIActivity.ActivityType](./mail.md)
  A type of activity that posts the provided content to a new email message.
- [static let markupAsPDF: UIActivity.ActivityType](./markupaspdf.md)
  A type of activity that marks up the provided content as a PDF file.
- [static let message: UIActivity.ActivityType](./message.md)
  A type of activity that posts the provided content to the Messages app.
- [static let openInIBooks: UIActivity.ActivityType](./openinibooks.md)
  A type of activity that opens the content in iBooks.
- [static let postToFlickr: UIActivity.ActivityType](./posttoflickr.md)
  A type of activity that posts the provided image to the user’s Flickr account.
- [static let postToTencentWeibo: UIActivity.ActivityType](./posttotencentweibo.md)
  A type of activity that posts the provided content to the user’s Tencent Weibo feed.
- [static let postToTwitter: UIActivity.ActivityType](./posttotwitter.md)
  A type of activity that posts the provided content to the user’s Twitter feed.
- [static let postToVimeo: UIActivity.ActivityType](./posttovimeo.md)
  A type of activity that posts the provided video to the user’s Vimeo account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/activitytype-swift.struct/posttofacebook)*