# NSSharingService.Name

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that describe the sharing services that macOS supports.

**Availability**:
- macOS

## Declaration

```swift
struct Name
```

```c
typedef NSString * NSSharingServiceName;
```

## Topics

### Creating a Sharing Service Name
- [init(String)](./name/init%28_%29.md)
  Creates a sharing service name using the provided string.
- [init(rawValue: String)](./name/init%28rawvalue%29.md)
  Creates a sharing service name using the specified raw value.
### Sharing Service Names
- [static let addToAperture: NSSharingService.Name](./name/addtoaperture.md)
  A service that shares an item provider’s contents with Aperture.
- [static let addToIPhoto: NSSharingService.Name](./name/addtoiphoto.md)
  A service that shares an item provider’s contents with iPhoto.
- [static let addToSafariReadingList: NSSharingService.Name](./name/addtosafarireadinglist.md)
  A service that shares an item provider’s contents with Safari’s Reading List.
- [static let cloudSharing: NSSharingService.Name](./name/cloudsharing.md)
  A service that shares an item provider’s contents with other iCloud users.
- [static let composeEmail: NSSharingService.Name](./name/composeemail.md)
  A service that uses an item provider’s contents to compose an email.
- [static let composeMessage: NSSharingService.Name](./name/composemessage.md)
  A service that uses an item provider’s contents to compose a message.
- [static let sendViaAirDrop: NSSharingService.Name](./name/sendviaairdrop.md)
  A service that sends an item provider’s contents to another device using AirDrop.
- [static let useAsDesktopPicture: NSSharingService.Name](./name/useasdesktoppicture.md)
  A service that sets the item provider’s contents as the current user’s desktop picture.
### Deprecated
- [Deprecated symbols](../name-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a Sharing Service
- [init?(named: NSSharingService.Name)](./init%28named%29.md)
  Returns a sharing service instance representing the specified service name.
- [init(title: String, image: NSImage, alternateImage: NSImage?, handler: () -> Void)](./init%28title,image,alternateimage,handler%29.md)
  Creates a custom sharing service object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/name)*