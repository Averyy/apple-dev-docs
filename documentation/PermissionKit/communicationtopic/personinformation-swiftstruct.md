# CommunicationTopic.PersonInformation

**Framework**: PermissionKit  
**Kind**: struct

Metadata corresponding to a specific person.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct PersonInformation
```

## Topics

### Initializing an instance
- [init(handle: CommunicationHandle, nameComponents: PersonNameComponents?, avatarImage: CGImage?)](communicationtopic/personinformation-swift.struct/init(handle:namecomponents:avatarimage:).md)
  Creates an object with the specified display name and contact information.
### Identifying metadata
- [var avatarImage: CGImage?](communicationtopic/personinformation-swift.struct/avatarimage.md)
  An image associated with the person.
- [var handle: CommunicationHandle](communicationtopic/personinformation-swift.struct/handle.md)
  A handle that can be used to communicate with the person.
- [var nameComponents: PersonNameComponents?](communicationtopic/personinformation-swift.struct/namecomponents.md)
  The components that make up the name of the person.
### Encoding and decoding
- [func encode(to: any Encoder) throws](communicationtopic/personinformation-swift.struct/encode(to:).md)
  Performs the inverse of the decoding process.
- [init(from: any Decoder) throws](communicationtopic/personinformation-swift.struct/init(from:).md)
  Creates an instance from the given decoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)

## See Also

- [var personInformation: [CommunicationTopic.PersonInformation]](communicationtopic/personinformation-swift.property.md)
  The metadata of the people with whom to communicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationtopic/personinformation-swift.struct)*