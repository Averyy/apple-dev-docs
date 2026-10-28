# allUserIdentitiesFromContacts()

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Fetches all user identities that match entries in the user’s Contacts.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- visionOS - Deprecated
- watchOS 8.0+ - Deprecated in 10.0

> **Deprecated**: No longer supported. Please see Sharing CloudKit Data with Other iCloud Users.

## Declaration

```swift
func allUserIdentitiesFromContacts() async throws -> [CKUserIdentity]
```

## Return Value

The user identities that match entries in the user’s Contacts.

## Discussion

This method searches for the users asynchronously and with a low priority. If you want the task to execute with a higher priority, create an instance of [`CKDiscoverAllUserIdentitiesOperation`](../ckdiscoveralluseridentitiesoperation.md) and configure it to use the necessary priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/alluseridentitiesfromcontacts())*