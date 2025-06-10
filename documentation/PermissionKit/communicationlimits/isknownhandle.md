# isKnownHandle(_:)

**Framework**: PermissionKit  
**Kind**: method

A Boolean that checks if the system knows the given handle.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final func isKnownHandle(_ handle: CommunicationHandle) async -> Bool
```

#### Return Value

Whether or not the given handle is known by the system.

## Parameters

- `handle`: A communication handle. This could be an email, phone number, username, or any other person identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimits/isknownhandle(_:))*