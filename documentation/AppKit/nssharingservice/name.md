# NSSharingService.Name

**Framework**: AppKit  
**Kind**: struct

Constants that describe the sharing services that macOS supports.

**Availability**:
- macOS ?+

## Declaration

```swift
struct Name
```

## Topics

### Creating a Sharing Service Name
- [init(String)](nssharingservice/name/init(_:).md)
  Creates a sharing service name using the provided string.
- [init(rawValue: String)](nssharingservice/name/init(rawvalue:).md)
  Creates a sharing service name using the specified raw value.
### Sharing Service Names
- [static let addToAperture: NSSharingService.Name](nssharingservice/name/addtoaperture.md)
  A service that shares an item provider’s contents with Aperture.
- [static let addToIPhoto: NSSharingService.Name](nssharingservice/name/addtoiphoto.md)
  A service that shares an item provider’s contents with iPhoto.
- [static let addToSafariReadingList: NSSharingService.Name](nssharingservice/name/addtosafarireadinglist.md)
  A service that shares an item provider’s contents with Safari’s Reading List.
- [static let cloudSharing: NSSharingService.Name](nssharingservice/name/cloudsharing.md)
  A service that shares an item provider’s contents with other iCloud users.
- [static let composeEmail: NSSharingService.Name](nssharingservice/name/composeemail.md)
  A service that uses an item provider’s contents to compose an email.
- [static let composeMessage: NSSharingService.Name](nssharingservice/name/composemessage.md)
  A service that uses an item provider’s contents to compose a message.
- [static let sendViaAirDrop: NSSharingService.Name](nssharingservice/name/sendviaairdrop.md)
  A service that sends an item provider’s contents to another device using AirDrop.
- [static let useAsDesktopPicture: NSSharingService.Name](nssharingservice/name/useasdesktoppicture.md)
  A service that sets the item provider’s contents as the current user’s desktop picture.
### Deprecated
- [Deprecated Symbols](name-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init?(named: NSSharingService.Name)](nssharingservice/init(named:).md)
  Returns a sharing service instance representing the specified service name.
- [init(title: String, image: NSImage, alternateImage: NSImage?, handler: () -> Void)](nssharingservice/init(title:image:alternateimage:handler:).md)
  Creates a custom sharing service object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/name)*