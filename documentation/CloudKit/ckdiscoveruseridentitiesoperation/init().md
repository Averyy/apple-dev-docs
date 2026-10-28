# init()

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates an operation for discovering user identities.

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
init()
```

```objc
- (instancetype) init;
```

## Discussion

You can use the operation only once. Create a new operation for each subsequent search.

## See Also

### Creating an Operation
- [convenience init(userIdentityLookupInfos: [CKUserIdentity.LookupInfo])](./init%28useridentitylookupinfos%29.md)
  Creates an operation for discovering the user identities of the specified lookup infos.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/init())*