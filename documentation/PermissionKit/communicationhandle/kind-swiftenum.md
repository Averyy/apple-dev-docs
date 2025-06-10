# CommunicationHandle.Kind

**Framework**: PermissionKit  
**Kind**: enum

An enumeration of the different types of communication handles.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum Kind
```

## Topics

### Identifying a handle type
- [CommunicationHandle.Kind.phoneNumber](communicationhandle/kind-swift.enum/phonenumber.md)
  A person’s phone number.
- [CommunicationHandle.Kind.emailAddress](communicationhandle/kind-swift.enum/emailaddress.md)
  A person’s email address.
- [CommunicationHandle.Kind.custom](communicationhandle/kind-swift.enum/custom.md)
  A unique identifier, such as a custom communication handle or user ID, that distinguishes one person from another.
### Decoding
- [init(from: any Decoder) throws](communicationhandle/kind-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (CommunicationHandle.Kind, CommunicationHandle.Kind) -> Bool](communicationhandle/kind-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](communicationhandle/kind-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](communicationhandle/kind-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](communicationhandle/kind-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](communicationhandle/kind-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationhandle/kind-swift.enum)*