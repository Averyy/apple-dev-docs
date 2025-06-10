# CommunicationHandle

**Framework**: PermissionKit  
**Kind**: struct

A piece of identifying information that can be used to communicate with someone.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct CommunicationHandle
```

#### Overview

This structure wraps a string value to allow clients to specify additional [`CommunicationHandle.Kind`](communicationhandle/kind-swift.enum.md) information about the type of handle it represents, such as a phone number, email address, or custom handle.

## Topics

### Initializing a communication handle
- [init(value: String, kind: CommunicationHandle.Kind)](communicationhandle/init(value:kind:).md)
  Creates a communication handle.
### Getting the handle information
- [var value: String](communicationhandle/value.md)
  The value of the communication handle.
- [var kind: CommunicationHandle.Kind](communicationhandle/kind-swift.property.md)
  The type of communication handle.
### Selecting a constant
- [CommunicationHandle.Kind](communicationhandle/kind-swift.enum.md)
  An enumeration of the different types of communication handles.
### Decoding
- [init(from: any Decoder) throws](communicationhandle/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (CommunicationHandle, CommunicationHandle) -> Bool](communicationhandle/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](communicationhandle/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](communicationhandle/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](communicationhandle/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](communicationhandle/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CommunicationLimits](communicationlimits.md)
  A type that encapsulates the communication limits for your app.
- [struct PermissionResponse](permissionresponse.md)
  A full permission response that includes the original question and chosen answer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationhandle)*