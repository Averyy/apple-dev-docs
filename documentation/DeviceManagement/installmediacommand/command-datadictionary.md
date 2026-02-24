# InstallMediaCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to install a book on a device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.9+

## Declaration

```swift
object InstallMediaCommand.Command
```

## Properties

- `Author` (string): The name of the book’s author. This value is available in iOS 8 and later.
- `iTunesStoreID` (integer): The book’s iTunes Store identifier.
- `Kind` (string): The kind of the media, which can be one of the following values: - `pdf`: A PDF file
- `epub`: An EPUB file in `gzip` format.
- `ibooks`: An iBooks Author file in `gzip` format. If you omit this value, its value is the file extension in the URL. This value is available in iOS 8 and later.
- `MediaType` (string) *(required)*: The media type, which can only be `Book`.
- `MediaURL` (string): The URL to retrieve the book. This value is available in iOS 8 and later.
- `PersistentID` (string): The book’s persistent identifier in reverse-DNS form; for example, `com.acme.manuals.training`. This value is available in iOS 8 and later.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.
- `Title` (string): The book’s title. This value is available in iOS 8 and later.
- `Version` (string): The book’s version number. This value is available in iOS 8 and later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installmediacommand/command-data.dictionary)*