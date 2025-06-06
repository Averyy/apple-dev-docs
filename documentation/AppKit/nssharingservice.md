# NSSharingService

**Framework**: AppKit  
**Kind**: class

An object that facilitates the sharing of content with social media services, or with apps like Mail or Safari.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class NSSharingService
```

#### Overview

An [`NSSharingService`](nssharingservice.md) object provides a consistent user experience for sharing items—[`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects, [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects, [`NSImage`](nsimage.md) objects, video (through file URLs), of any object that implements the [`NSPasteboardWriting`](nspasteboardwriting.md) protocol—in macOS.

For any item or group of items, the [`NSSharingService`](nssharingservice.md) displays a sheet with the content to share. A sharing service can create a post on a social network like Twitter or Facebook, send a message by email or iMessage, upload videos to viewing services, or send a file using AirDrop.

You can use [`NSSharingService`](nssharingservice.md) objects directly in your app. The following example shows how to create a button that shares content directly to a social media service.

```objc
- (void)awakeFromNib
{
    NSSharingService * service = [NSSharingService sharingServiceNamed:NSSharingServiceNamePostOnTwitter];
    [myShareOnTwitterButton setTitle:service.title];
    [myShareOnTwitterButton setEnabled:[service canPerformWithItems:nil]];
}
 
 
- (IBAction)shareOnTwitter:(id)sender
{
    // Items to share
    NSAttributedString *text = [self.textView attributedString];
    NSImage *image = [self.imageView image];
    NSArray * shareItems = [NSArray arrayWithObjects:text, image, nil];
 
    NSSharingService *service = [NSSharingService sharingServiceNamed:NSSharingServiceNamePostOnTwitter];
    service.delegate = self;
    [service performWithItems:shareItems];
}
```

## Topics

### Creating a Sharing Service
- [init?(named: NSSharingService.Name)](nssharingservice/init(named:).md)
  Returns a sharing service instance representing the specified service name.
- [init(title: String, image: NSImage, alternateImage: NSImage?, handler: () -> Void)](nssharingservice/init(title:image:alternateimage:handler:).md)
  Creates a custom sharing service object.
- [NSSharingService.Name](nssharingservice/name.md)
  Constants that describe the sharing services that macOS supports.
### Managing the Delegate
- [var delegate: (any NSSharingServiceDelegate)?](nssharingservice/delegate.md)
  Specifies the delegate of the sharing service.
- [protocol NSSharingServiceDelegate](nssharingservicedelegate.md)
  A set of methods that you use to customize the position and animation of a share sheet, and to be notified whether the item is successfully shared.
### Querying Service Availability
- [class func sharingServices(forItems: [Any]) -> [NSSharingService]](nssharingservice/sharingservices(foritems:).md)
  Returns a list of sharing services which could share all the provided items together.
- [func canPerform(withItems: [Any]?) -> Bool](nssharingservice/canperform(withitems:).md)
  Returns whether the service can share all the specified items.
### Getting the Service’s Details
- [var accountName: String?](nssharingservice/accountname.md)
  The account name used for posting on Twitter or Sina Weibo.
- [var alternateImage: NSImage?](nssharingservice/alternateimage.md)
  The alternate image representing the sharing service.
- [var image: NSImage](nssharingservice/image.md)
  The primary image representing the sharing service.
- [var title: String](nssharingservice/title.md)
  The title of the sharing service.
### Configuring the Service
- [var menuItemTitle: String](nssharingservice/menuitemtitle.md)
  The title of the service in the Share menu.
- [var recipients: [String]?](nssharingservice/recipients.md)
  An array containing the user handles of the desired recipients.
- [var subject: String?](nssharingservice/subject.md)
  The subject of the post.
### Sharing Items
- [func perform(withItems: [Any])](nssharingservice/perform(withitems:).md)
  Manually performs the service on the provided items.
### Providing CloudKit Share Options
- [NSSharingService.CloudKitOptions](nssharingservice/cloudkitoptions.md)
  Constants that describe how a participant can configure a CloudKit share.
### Getting the Shared Items
- [var attachmentFileURLs: [URL]?](nssharingservice/attachmentfileurls.md)
  An array of NSURL objects representing the files that were shared.
- [var messageBody: String?](nssharingservice/messagebody.md)
  The message body as a string.
- [var permanentLink: URL?](nssharingservice/permanentlink.md)
  A permanent URL (permalink) that your app can use to access the post.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSSharingServicePicker](nssharingservicepicker.md)
  A list of sharing services that the user can choose from.
- [protocol NSPreviewRepresentableActivityItem](nspreviewrepresentableactivityitem.md)
  An interface you adopt in custom objects that you want to share using the macOS share sheet.
- [class NSSharingServicePickerToolbarItem](nssharingservicepickertoolbaritem.md)
  A toolbar item that displays the macOS share sheet.
- [protocol NSServicesMenuRequestor](nsservicesmenurequestor.md)
  A set of methods that support interaction with items users can share through a sharing service.
- [protocol NSCloudSharingServiceDelegate](nscloudsharingservicedelegate.md)
  A set of methods for responding to the life cycle events of the cloud-sharing service.
- [Services Functions](services-functions.md)
  Configure the contents of your app’s Services menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice)*