# sharePlay

**Framework**: UIKit  
**Kind**: property

A type of activity that makes the provided content available through SharePlay.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- visionOS 1.0+

## Declaration

```swift
static let sharePlay: UIActivity.ActivityType
```

#### Discussion

When using this service, you can use [`registerGroupActivity(_:)`](https://developer.apple.com/documentation/foundation/nsitemprovider/3920459-registergroupactivity) to provide an [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) with a [`GroupActivity`](https://developer.apple.com/documentation/GroupActivities/GroupActivity) object as an activity item. If no `GroupActivity` object is provided, the service will start a FaceTime call without an accompanying SharePlay session.

## See Also

- [static let addToHomeScreen: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/addtohomescreen.md)
- [static let addToReadingList: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/addtoreadinglist.md)
  A type of activity that adds the URL to Safari’s reading list.
- [static let airDrop: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/airdrop.md)
  A type of activity that makes the provided content available through AirDrop.
- [static let assignToContact: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/assigntocontact.md)
  A type of activity that assigns the image to a contact.
- [static let collaborationCopyLink: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/collaborationcopylink.md)
- [static let collaborationInviteWithLink: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/collaborationinvitewithlink.md)
- [static let copyToPasteboard: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/copytopasteboard.md)
  A type of activity that posts the provided content to the pasteboard.
- [static let mail: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/mail.md)
  A type of activity that posts the provided content to a new email message.
- [static let markupAsPDF: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/markupaspdf.md)
  A type of activity that marks up the provided content as a PDF file.
- [static let message: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/message.md)
  A type of activity that posts the provided content to the Messages app.
- [static let openInIBooks: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/openinibooks.md)
  A type of activity that opens the content in iBooks.
- [static let postToFacebook: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/posttofacebook.md)
  A type of activity that posts the provided content to the user’s wall on Facebook.
- [static let postToFlickr: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/posttoflickr.md)
  A type of activity that posts the provided image to the user’s Flickr account.
- [static let postToTencentWeibo: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/posttotencentweibo.md)
  A type of activity that posts the provided content to the user’s Tencent Weibo feed.
- [static let postToTwitter: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/posttotwitter.md)
  A type of activity that posts the provided content to the user’s Twitter feed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/activitytype-swift.struct/shareplay)*