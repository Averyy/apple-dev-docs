# knownHandles(in:)

**Framework**: PermissionKit  
**Kind**: method

Checks which handles in a given set are known to the system.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func knownHandles(in handles: Set<CommunicationHandle>) async -> Set<CommunicationHandle>
```

## Mentions

- [Creating a communication experience](creating-a-communication-experience.md)

#### Return Value

A subset of the given handles known to the system.

#### Discussion

> **Note**: This method requires that the calling app have a non-nil, nonempty bundle identifier.

## Parameters

- `handles`: A set of communication handles, such as email addresses,   phone numbers, user names, or any other set of personal identifiers.

## See Also

- [func isKnownHandle(CommunicationHandle) async -> Bool](communicationlimits/isknownhandle(_:).md)
  A Boolean that checks if the system knows the given handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimits/knownhandles(in:))*