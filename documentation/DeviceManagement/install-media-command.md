# Install Media

**Framework**: Device Management  
**Kind**: httpRequest

Install a book on a device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.9+

#### Discussion

The request must contain either the `iTunesStoreID` or `MediaURL`. The `MediaURL` must lead to a PDF file, an EPUB file in `gzip` format, or an iBooks Author document in `gzip` format. Books that MDM has installed become managed books.

Use Volume Purchase Program (VPP) Licensing to obtain books from the Book Store. Books from the Book Store require that the device has enabled App Store. These books undergo backup, sync with iTunes, and remain on the device after removal of the MDM profile.

Books that aren’t from the Book Store don’t require that the device has enabled App Store. These books don’t undergo backup, don’t sync with iTunes, and don’t remain on the device after removal of the MDM profile.

If the book already exists, this command updates the book and makes it visible to the MDM server. The user doesn’t receive a prompt for a book installation or update unless they need to log in to complete a Book Store transaction.

If you install a book from the Book Store with the same `iTunesStoreID` as an existing managed book, the new book replaces the existing one.

If you install a book that isn’t from the Book Store with the same `PersistentID` as an existing book that also isn’t from the Book Store, the new book replaces the existing one.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad |
| User channel | macOS |
| Requires supervision | macOS |
| Allowed in user enrollment | iOS |
| Required access right | AllowAppInstallation |

##### Example Request and Response

## Topics

### Commands and responses
- [object InstallMediaCommand](installmediacommand.md)
  The command to install a book on a device.
- [object InstallMediaResponse](installmediaresponse.md)
  A response from the device after it processes the command to install a book on a device.

## Request Body

The request object the server returns for the Install Media Command.

## See Also

- [Managed Media List](managed-media-list-command.md)
  Get a list of the managed books on a device.
- [Remove Media](remove-media-command.md)
  Remove a previously installed book from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/install-media-command)*