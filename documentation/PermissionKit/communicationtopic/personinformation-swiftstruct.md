# CommunicationTopic.PersonInformation

**Framework**: PermissionKit  
**Kind**: struct

Information about a person the child wants to communicate with.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct PersonInformation
```

## Topics

### Creating contact details
- [init(handle: CommunicationHandle, nameComponents: PersonNameComponents?, avatarImage: CGImage?)](communicationtopic/personinformation-swift.struct/init(handle:namecomponents:avatarimage:).md)
  Creates person information with contact details and optional display information.
- [init(from: any Decoder) throws](communicationtopic/personinformation-swift.struct/init(from:).md)
  Creates an instance from the given decoder.
### Accessing properties
- [var avatarImage: CGImage?](communicationtopic/personinformation-swift.struct/avatarimage.md)
  An image that represents the person.
- [var handle: CommunicationHandle](communicationtopic/personinformation-swift.struct/handle.md)
  The handle to identify and communicate with the person.
- [var nameComponents: PersonNameComponents?](communicationtopic/personinformation-swift.struct/namecomponents.md)
  The components that make up the person’s name.
### Encoding
- [func encode(to: any Encoder) throws](communicationtopic/personinformation-swift.struct/encode(to:).md)
  Performs the inverse of the decoding process.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)

## See Also

- [CommunicationTopic.Action](communicationtopic/action.md)
  A communication action you can request permission for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationtopic/personinformation-swift.struct)*