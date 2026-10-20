# userIdentities(forEmailAddresses:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Fetches the user identities for the specified email addresses and returns them to an awaiting caller.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- tvOS 15.0+ - Deprecated in 17.0
- visionOS - Deprecated
- watchOS 8.0+ - Deprecated in 10.0

> **Deprecated**: No longer supported. Please see Sharing CloudKit Data with Other iCloud Users.

## Declaration

```swift
func userIdentities(forEmailAddresses emails: [String]) async throws -> [String : CKUserIdentity]
```

#### Return Value

A [`Result`](../../Swift/result.md) that contains either a dictionary of user identities, or an error that describes why CloudKit can’t discover the email addresses.

In the successful case, the dictionary uses the email addresses you specify in `emails` as its keys. Only successfully discovered user identities are present in this dictionary.

#### Discussion

Use this method to retrieve the identities of users who the current user knows. The users you’re searching for must meet the following criteria:

- The user has run the app.
- The user grants the [`userDiscoverability`](./applicationpermissions/userdiscoverability.md) permission for the container.

This method searches for users asynchronously and with a low priority. If you want the task to execute the request with a higher priority, create an instance of [`CKDiscoverUserIdentitiesOperation`](../ckdiscoveruseridentitiesoperation.md) and configure it to use the necessary priority.

## Parameters

- `emails`: The users’ email addresses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/useridentities(foremailaddresses:))*