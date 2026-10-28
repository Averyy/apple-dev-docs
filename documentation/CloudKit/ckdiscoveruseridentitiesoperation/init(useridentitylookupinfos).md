# init(userIdentityLookupInfos:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates an operation for discovering the user identities of the specified lookup infos.

**Availability**:
- iOS 10.0+ - Deprecated in 17.0
- iPadOS 10.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.12+ - Deprecated in 14.0
- tvOS 10.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 10.0

> **Deprecated**: No longer supported. Please see Sharing CloudKit Data with Other iCloud Users.

## Declaration

```swift
convenience init(userIdentityLookupInfos: [CKUserIdentity.LookupInfo])
```

```objc
- (instancetype) initWithUserIdentityLookupInfos:(NSArray<CKUserIdentityLookupInfo *> *) userIdentityLookupInfos;
```

## Discussion

After you create the operation, assign a handler to [`discoverUserIdentitiesCompletionBlock`](./discoveruseridentitiescompletionblock.md) so that you can process the search results.

## Parameters

- `userIdentityLookupInfos`: An array that contains instances of [`CKUserIdentity.LookupInfo`](../ckuseridentity/lookupinfo-swift.class.md). CloudKit uses this parameter as the default value for the [`userIdentityLookupInfos`](./useridentitylookupinfos.md) property. If you specify `nil`, you must assign a value to that property before you execute the operation.

## See Also

### Creating an Operation
- [init()](./init%28%29.md)
  Creates an operation for discovering user identities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/init(useridentitylookupinfos:))*