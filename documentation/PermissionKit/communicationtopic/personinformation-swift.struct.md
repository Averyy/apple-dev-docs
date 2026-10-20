# CommunicationTopic.PersonInformation

**Framework**: PermissionKit  
**Kind**: struct  
**Role**: Structure

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
- [init(handle: CommunicationHandle, nameComponents: PersonNameComponents?, avatarImage: CGImage?)](./personinformation-swift.struct/init%28handle,namecomponents,avatarimage%29.md)
  Creates person information with contact details and optional display information.
- [init(from: any Decoder) throws](./personinformation-swift.struct/init%28from%29.md)
  Creates an instance from the given decoder.
### Accessing properties
- [var avatarImage: CGImage?](./personinformation-swift.struct/avatarimage.md)
  An image that represents the person.
- [var handle: CommunicationHandle](./personinformation-swift.struct/handle.md)
  The handle to identify and communicate with the person.
- [var nameComponents: PersonNameComponents?](./personinformation-swift.struct/namecomponents.md)
  The components that make up the person’s name.
### Encoding
- [func encode(to: any Encoder) throws](./personinformation-swift.struct/encode%28to%29.md)
  Performs the inverse of the decoding process.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)

## See Also

### Working with supporting types
- [CommunicationTopic.Action](./action.md)
  A communication action you can request permission for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationtopic/personinformation-swift.struct)*