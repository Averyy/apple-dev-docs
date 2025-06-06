# UIActivity.ActivityType

**Framework**: UIKit  
**Kind**: struct

A structure that describes the types of activities for which the system has built-in support.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct ActivityType
```

#### Overview

These constants represent the values that can be stored in the [`activityType`](uiactivity/activitytype-swift.property.md) property of system-defined activity objects.

## Topics

### Constants
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
- [static let postToVimeo: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/posttovimeo.md)
  A type of activity that posts the provided video to the user’s Vimeo account.
- [static let postToWeibo: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/posttoweibo.md)
  A type of activity that posts the provided content to the user’s Weibo feed.
- [static let print: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/print.md)
  A type of activity that prints the provided content.
- [static let saveToCameraRoll: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/savetocameraroll.md)
  A type of activity that assigns the image or video to the user’s camera roll.
- [static let sharePlay: UIActivity.ActivityType](uiactivity/activitytype-swift.struct/shareplay.md)
  A type of activity that makes the provided content available through SharePlay.
### Initializers
- [init(String)](uiactivity/activitytype-swift.struct/init(_:).md)
  Creates an activity type.
- [init(rawValue: String)](uiactivity/activitytype-swift.struct/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class var activityCategory: UIActivity.Category](uiactivity/activitycategory.md)
  The category of the activity, which may be used to group activities in the UI.
- [UIActivity.Category](uiactivity/category.md)
  An enumeration that defines categories of activities.
- [var activityType: UIActivity.ActivityType?](uiactivity/activitytype-swift.property.md)
  The type of service being provided.
- [var activityTitle: String?](uiactivity/activitytitle.md)
  A user-readable string that describes the service.
- [var activityImage: UIImage?](uiactivity/activityimage.md)
  An image that identifies the service to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivity/activitytype-swift.struct)*