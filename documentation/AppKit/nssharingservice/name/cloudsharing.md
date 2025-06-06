# cloudSharing

**Framework**: AppKit  
**Kind**: property

A service that shares an item provider’s contents with other iCloud users.

**Availability**:
- macOS 10.12+

## Declaration

```swift
static let cloudSharing: NSSharingService.Name
```

#### Discussion

The behavior of the cloud-sharing service is different from other services. It creates a persistent sharing session between two or more iCloud users, and provides access to the original items, rather than sending copies. For more information about CloudKit Sharing, see [`Shared Records`](https://developer.apple.com/documentation/CloudKit/shared-records).

## See Also

- [static let addToAperture: NSSharingService.Name](nssharingservice/name/addtoaperture.md)
  A service that shares an item provider’s contents with Aperture.
- [static let addToIPhoto: NSSharingService.Name](nssharingservice/name/addtoiphoto.md)
  A service that shares an item provider’s contents with iPhoto.
- [static let addToSafariReadingList: NSSharingService.Name](nssharingservice/name/addtosafarireadinglist.md)
  A service that shares an item provider’s contents with Safari’s Reading List.
- [static let composeEmail: NSSharingService.Name](nssharingservice/name/composeemail.md)
  A service that uses an item provider’s contents to compose an email.
- [static let composeMessage: NSSharingService.Name](nssharingservice/name/composemessage.md)
  A service that uses an item provider’s contents to compose a message.
- [static let sendViaAirDrop: NSSharingService.Name](nssharingservice/name/sendviaairdrop.md)
  A service that sends an item provider’s contents to another device using AirDrop.
- [static let useAsDesktopPicture: NSSharingService.Name](nssharingservice/name/useasdesktoppicture.md)
  A service that sets the item provider’s contents as the current user’s desktop picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssharingservice/name/cloudsharing)*