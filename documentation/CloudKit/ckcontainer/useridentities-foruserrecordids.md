# userIdentities(forUserRecordIDs:)

**Framework**: CloudKit  
**Kind**: method

Fetches the user identities for the specified user record IDs and returns them to an awaiting caller.

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
func userIdentities(forUserRecordIDs userRecordIDs: [CKRecord.ID]) async throws -> [CKRecord.ID : CKUserIdentity]
```

#### Return Value

A [`Result`](https://developer.apple.com/documentation/swift/result) that contains either a dictionary of user identities, or an error that describes why CloudKit can’t discover the user record IDs.

In the successful case, the dictionary uses the user record IDs you specify in `userRecordIDs` as its keys. Only successfully discovered user identities are present in this dictionary.

#### Discussion

Use this method to retrieve the identities of users who the current user knows. The users you’re searching for must meet the following criteria:

- The user has run the app.
- The user grants the [`userDiscoverability`](ckcontainer/applicationpermissions/userdiscoverability.md) permission for the container.

This method searches for users asynchronously and with a low priority. If you want the task to execute the request with a higher priority, create an instance of [`CKDiscoverUserIdentitiesOperation`](ckdiscoveruseridentitiesoperation.md) and configure it to use the necessary priority.

## Parameters

- `userRecordIDs`: The users’ user record IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/useridentities(foruserrecordids:))*