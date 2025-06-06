# init(existingItemIdentifier:)

**Framework**: File Provider  
**Kind**: init

Initialize a location with the item identifier of a folder that already exists on the server.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(existingItemIdentifier: NSFileProviderItemIdentifier)
```

#### Discussion

If the known folder already exists on the server, the provider can specify the exact identifier of the item that needs to be used to back the known folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderknownfolderlocations/location/init(existingitemidentifier:))*