# init(parentItemIdentifier:filename:)

**Framework**: File Provider  
**Kind**: init

Initialize a location with the filename of the folder in a specified parent.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init(parentItemIdentifier: NSFileProviderItemIdentifier, filename: String)
```

#### Discussion

When replicating a known folder the system will reuse a folder located at the specified filename within the parent if one exists, or create a new item at this location if none exists yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderknownfolderlocations/location/init(parentitemidentifier:filename:))*