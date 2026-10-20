# init(handle:nameComponents:avatarImage:)

**Framework**: PermissionKit  
**Kind**: init  
**Role**: Initializer

Creates person information with contact details and optional display information.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(handle: CommunicationHandle, nameComponents: PersonNameComponents? = nil, avatarImage: CGImage? = nil)
```

## Parameters

- `handle`: The handle you use to identify the person.
- `nameComponents`: The person’s name components.
- `avatarImage`: An image that represents the person.

## See Also

### Creating contact details
- [init(from: any Decoder) throws](./init%28from%29.md)
  Creates an instance from the given decoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationtopic/personinformation-swift.struct/init(handle:namecomponents:avatarimage:))*