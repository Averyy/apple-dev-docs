# CommunicationHandle.Kind

**Framework**: PermissionKit  
**Kind**: enum

An enumeration that identifies different types of communication handles.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum Kind
```

#### Overview

Use these cases to specify whether a handle represents an email address, phone number, username, or custom identifier when requesting communication permission.

## Topics

### Identifying a handle type
- [CommunicationHandle.Kind.phoneNumber](communicationhandle/kind-swift.enum/phonenumber.md)
  A person’s phone number.
- [CommunicationHandle.Kind.emailAddress](communicationhandle/kind-swift.enum/emailaddress.md)
  A person’s email address.
- [CommunicationHandle.Kind.custom](communicationhandle/kind-swift.enum/custom.md)
  A unique identifier that distinguishes one person from another.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationhandle/kind-swift.enum)*