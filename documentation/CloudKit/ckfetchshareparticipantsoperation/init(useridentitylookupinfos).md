# init(userIdentityLookupInfos:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithUserIdentityLookupInfos:(NSArray<CKUserIdentityLookupInfo *> *) userIdentityLookupInfos;
```

#### Discussion

After you create the operation, assign a handler to the [`fetchShareParticipantsCompletionBlock`](./fetchshareparticipantscompletionblock.md) property to process the results.

## Parameters

- `userIdentityLookupInfos`: The user data for the participants. If you specify `nil`, you must assign a value to the [`userIdentityLookupInfos`](./useridentitylookupinfos.md) property before you execute this operation.

## See Also

### Creating an Operation
- [init()](./init%28%29.md)
  Creates an empty operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/init(useridentitylookupinfos:))*