# RemoveMediaCommand.Command

**Framework**: Device Management  
**Kind**: dictionary

The command to remove a previously installed book from a device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+

## Declaration

```swift
object RemoveMediaCommand.Command
```

## Properties

- `iTunesStoreID` (string): The book’s iTunes Store identifier.
- `MediaType` (string) *(required)*: The media type, which can only be `Book`.
- `PersistentID` (string): The book’s persistent identifier in reverse-DNS form; for example, `com.acme.manuals.training`.
- `RequestRequiresNetworkTether` (boolean): If `true`, the device needs to be network-tethered to run the command.
- `RequestType` (string) *(required)*: The request type for this command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/removemediacommand/command-data.dictionary)*