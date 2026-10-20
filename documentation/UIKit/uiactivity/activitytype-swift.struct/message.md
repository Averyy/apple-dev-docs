# message

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A type of activity that posts the provided content to the Messages app.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static let message: UIActivity.ActivityType
```

```c
extern UIActivityType const UIActivityTypeMessage;
```

#### Discussion

When using this service, you can provide [`NSString`](../../../Foundation/nsstring.md) and [`NSAttributedString`](../../../Foundation/nsattributedstring.md) objects as data for the activity items. You may also specify [`NSURL`](../../../Foundation/nsurl.md) objects whose contents use the `sms` scheme.

If the device has MMS or FaceTime enabled, you can provide [`UIImage`](../../uiimage.md), and [`NSURL`](../../../Foundation/nsurl.md) objects as data for the activity items.

To specify an [`NSData`](../../../Foundation/nsdata.md) object, you must implement the [`UIActivityItemSource`](../../uiactivityitemsource.md) protocol, return the data object in [`activityViewController(_:itemForActivityType:)`](../../uiactivityitemsource/activityviewcontroller%28_,itemforactivitytype%29.md), and return the data object’s UTI in [`activityViewController(_:dataTypeIdentifierForActivityType:)`](../../uiactivityitemsource/activityviewcontroller%28_,datatypeidentifierforactivitytype%29.md).

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
- [static let openInIBooks: UIActivity.ActivityType](./openinibooks.md)
  A type of activity that opens the content in iBooks.
- [static let postToFacebook: UIActivity.ActivityType](./posttofacebook.md)
  A type of activity that posts the provided content to the user’s wall on Facebook.
- [static let postToFlickr: UIActivity.ActivityType](./posttoflickr.md)
  A type of activity that posts the provided image to the user’s Flickr account.
- [static let postToTencentWeibo: UIActivity.ActivityType](./posttotencentweibo.md)
  A type of activity that posts the provided content to the user’s Tencent Weibo feed.
- [static let postToTwitter: UIActivity.ActivityType](./posttotwitter.md)
  A type of activity that posts the provided content to the user’s Twitter feed.
- [static let postToVimeo: UIActivity.ActivityType](./posttovimeo.md)
  A type of activity that posts the provided video to the user’s Vimeo account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/activitytype-swift.struct/message)*