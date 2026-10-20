# NSFileProviderKnownFolderLocations.Location

**Framework**: File Provider  
**Kind**: class  
**Role**: Class

**Availability**:
- macOS 15.0+

## Declaration

```swift
class Location
```

```objc
@interface NSFileProviderKnownFolderLocation : NSObject
```

## Topics

### Initializers
- [init(existingItemIdentifier: NSFileProviderItemIdentifier)](./location/init%28existingitemidentifier%29.md)
  Initialize a location with the item identifier of a folder that already exists on the server.
- [init(parentItemIdentifier: NSFileProviderItemIdentifier, filename: String)](./location/init%28parentitemidentifier,filename%29.md)
  Initialize a location with the filename of the folder in a specified parent.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Identifying known-folder locations
- [var desktopLocation: NSFileProviderKnownFolderLocations.Location?](./desktoplocation.md)
- [var documentsLocation: NSFileProviderKnownFolderLocations.Location?](./documentslocation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderknownfolderlocations/location)*