# knownHandles(in:)

**Framework**: PermissionKit  
**Kind**: method

Checks which handles in a given set are known to the system.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func knownHandles(in handles: Set<CommunicationHandle>) async -> Set<CommunicationHandle>
```

#### Return Value

A subset of the given handles known to the system.

#### Discussion

> **Note**: This method requires that the calling app have a non-nil, nonempty bundle identifier.

## Parameters

- `handles`: A set of communication handles, such as email addresses,   phone numbers, user names, or any other set of personal identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimits/knownhandles(in:))*