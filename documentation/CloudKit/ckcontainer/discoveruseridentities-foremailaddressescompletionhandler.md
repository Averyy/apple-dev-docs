# discoverUserIdentities(forEmailAddresses:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches the user identities for the specified email addresses.

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
@preconcurrency
func discoverUserIdentities(forEmailAddresses emails: [String], completionHandler: @escaping @Sendable (Result<[String : CKUserIdentity], any Error>) -> Void)
```

#### Discussion

This closure doesn’t return a value and takes the following parameters:

- A [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either a dictionary of user identities, or an error that describes why CloudKit can’t discover the email addresses. In the successful case, the dictionary uses the email addresses you specify in `emails` as its keys. Only successfully discovered user identities are present in this dictionary.

Use this method to retrieve the identities of users who the current user knows. The users you’re searching for must meet the following criteria:

- The user has run the app.
- The user grants the [`userDiscoverability`](ckcontainer/applicationpermissions/userdiscoverability.md) permission for the container.

This method searches for users asynchronously and with a low priority. If you want the task to execute the request with a higher priority, create an instance of [`CKDiscoverUserIdentitiesOperation`](ckdiscoveruseridentitiesoperation.md) and configure it to use the necessary priority.

## Parameters

- `emails`: The users’ email addresses.
- `completionHandler`: The handler to execute with the fetch results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckcontainer/discoveruseridentities(foremailaddresses:completionhandler:))*