# isKnownHandle(_:)

**Framework**: PermissionKit  
**Kind**: method

A Boolean that checks if the system knows the given handle.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func isKnownHandle(_ handle: CommunicationHandle) async -> Bool
```

#### Return Value

Whether or not the given handle is known by the system.

## Parameters

- `handle`: A communication handle. This could be an email, phone number, username, or any other person identifier.

## See Also

- [func knownHandles(in: Set<CommunicationHandle>) async -> Set<CommunicationHandle>](communicationlimits/knownhandles(in:).md)
  Checks which handles in a given set are known to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimits/isknownhandle(_:))*