# init(userIdentityLookupInfos:)

**Framework**: CloudKit  
**Kind**: init

Creates an operation for discovering the user identities of the specified lookup infos.

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

After you create the operation, assign a handler to [`discoverUserIdentitiesCompletionBlock`](ckdiscoveruseridentitiesoperation/discoveruseridentitiescompletionblock.md) so that you can process the search results.

## Parameters

- `userIdentityLookupInfos`: An array that contains instances of  . CloudKit uses this parameter as the default value for the   property. If you specify  , you must assign a value to that property before you execute the operation.

## See Also

- [init()](ckdiscoveruseridentitiesoperation/init.md)
  Creates an operation for discovering user identities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/init(useridentitylookupinfos:))*