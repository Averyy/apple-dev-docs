# CommunicationHandle

**Framework**: PermissionKit  
**Kind**: struct  
**Role**: Structure

Contact information for identifying and communicating with a person.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct CommunicationHandle
```

## Overview

Use this structure to specify contact information like phone numbers, email addresses, or custom identifiers, along with the type of handle it represents.

## Topics

### Specifying handle types
- [CommunicationHandle.Kind](./communicationhandle/kind-swift.enum.md)
  An enumeration that identifies different types of communication handles.
### Creating handles
- [init(value: String, kind: CommunicationHandle.Kind)](./communicationhandle/init%28value,kind%29.md)
  Creates a communication handle.
### Accessing properties
- [var value: String](./communicationhandle/value.md)
  The value of the communication handle.
- [var kind: CommunicationHandle.Kind](./communicationhandle/kind-swift.property.md)
  The type of communication handle.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Response management
- [func responses<Topic>(for: Topic.Type) -> some AsyncSequence<PermissionResponse<Topic>, Never>
](./askcenter/responses%28for%29.md)
  Registers the topic type with the system and returns an asynchronous sequence of responses.
- [struct PermissionResponse](./permissionresponse.md)
  A full permission response that includes the original question and chosen answer.
- [struct PermissionChoice](./permissionchoice.md)
  A class that uniquely identifies a specific, statically defined permission choice.
- [class CommunicationLimits](./communicationlimits.md)
  A type that encapsulates the communication limits for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationhandle)*