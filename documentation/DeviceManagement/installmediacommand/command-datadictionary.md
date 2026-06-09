# InstallMediaCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to install a book on a device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.9+

## Declaration

```swift
object InstallMediaCommand.Command
```

## Properties

- `Author` (string): The name of the book’s author. Available: iOS 8+ | iPadOS 8+
Deprecated: macOS 11+
Removed: macOS 11+
- `iTunesStoreID` (integer): The book’s iTunes Store identifier. Deprecated: macOS 11+
Removed: macOS 11+
- `Kind` (string): The kind of the media, which can be one of the following values: - `pdf`: A PDF file
- `epub`: An EPUB file in `gzip` format.
- `ibooks`: An iBooks Author file in `gzip` format. If you omit this value, its value is the file extension in the URL. Available: iOS 8+ | iPadOS 8+
Deprecated: macOS 11+
Removed: macOS 11+
- `MediaType` (string) *(required)*: The media type, which can only be `Book`. Deprecated: macOS 11+
Removed: macOS 11+
- `MediaURL` (string): The URL to retrieve the book. Available: iOS 8+ | iPadOS 8+
Deprecated: macOS 11+
Removed: macOS 11+
- `PersistentID` (string): The book’s persistent identifier in reverse-DNS form; for example, `com.acme.manuals.training`. Available: iOS 8+ | iPadOS 8+
Deprecated: macOS 11+
Removed: macOS 11+
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command. Deprecated: macOS 11+
Removed: macOS 11+
- `RequestType` (string) *(required)*: The request type for this command. Deprecated: macOS 11+
Removed: macOS 11+
- `Title` (string): The book’s title. Available: iOS 8+ | iPadOS 8+
Deprecated: macOS 11+
Removed: macOS 11+
- `Version` (string): The book’s version number. Available: iOS 8+ | iPadOS 8+
Deprecated: macOS 11+
Removed: macOS 11+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installmediacommand/command-data.dictionary)*