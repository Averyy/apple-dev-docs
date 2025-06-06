# NSFileProviderTypeAndCreator

**Framework**: File Provider  
**Kind**: struct

A structure that contains the file type and file creator codes for an item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct NSFileProviderTypeAndCreator
```

## Topics

### Creating Type and Creator Structures
- [init()](nsfileprovidertypeandcreator/init.md)
  Returns a new type and creator structure with both codes set to `0`.
- [init(type: OSType, creator: OSType)](nsfileprovidertypeandcreator/init(type:creator:).md)
  Creates a structure that contains the provided type and creator codes.
### Accessing Type and Creator Codes
- [var creator: OSType](nsfileprovidertypeandcreator/creator.md)
  The item’s creator code.
- [var type: OSType](nsfileprovidertypeandcreator/type.md)
  The item’s type code.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias NSFileProviderItem](nsfileprovideritem-swift.typealias.md)
  An item the File Provider extension manages.
- [protocol NSFileProviderItemProtocol](nsfileprovideritemprotocol.md)
  A protocol that defines the properties of an item managed by the File Provider extension.
- [struct NSFileProviderItemIdentifier](nsfileprovideritemidentifier.md)
  A unique identifier for an item managed by the File Provider extension.
- [struct NSFileProviderItemCapabilities](nsfileprovideritemcapabilities.md)
  An item’s capabilities, which define the actions that the user can perform in the document browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertypeandcreator)*