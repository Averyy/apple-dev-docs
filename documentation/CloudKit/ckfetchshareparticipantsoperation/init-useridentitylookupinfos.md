# init(userIdentityLookupInfos:)

**Framework**: CloudKit  
**Kind**: init

Creates an operation for generating share participants from the specified user data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(userIdentityLookupInfos: [CKUserIdentity.LookupInfo])
```

#### Discussion

After you create the operation, assign a handler to the [`fetchShareParticipantsCompletionBlock`](ckfetchshareparticipantsoperation/fetchshareparticipantscompletionblock.md) property to process the results.

## Parameters

- `userIdentityLookupInfos`: The user data for the participants. If you specify  , you must assign a value to the   property before you execute this operation.

## See Also

- [init()](ckfetchshareparticipantsoperation/init.md)
  Creates an empty operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/init(useridentitylookupinfos:))*