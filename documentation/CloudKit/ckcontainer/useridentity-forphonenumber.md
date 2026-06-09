# userIdentity(forPhoneNumber:)

**Framework**: CloudKit  
**Kind**: method

Fetches the user identity for the specified phone number.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+ - Deprecated
- watchOS 8.0+

## Declaration

```swift
func userIdentity(forPhoneNumber phoneNumber: String) async throws -> CKUserIdentity?
```

#### Return Value

The user identity for the phone number.

#### Discussion

Use this method to retrieve the identity of a user who the current user knows. The user you’re searching for must meet the following criteria:

- The user has run the app.
- The user grants the [`userDiscoverability`](ckcontainer/applicationpermissions/userdiscoverability.md) permission for the container.

This method searches for the user asynchronously and with a low priority. If you want the task to execute the request with a higher priority, create an instance of [`CKDiscoverUserIdentitiesOperation`](ckdiscoveruseridentitiesoperation.md) and configure it to use the necessary priority.

## Parameters

- `phoneNumber`: The user’s phone number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/useridentity(forphonenumber:))*