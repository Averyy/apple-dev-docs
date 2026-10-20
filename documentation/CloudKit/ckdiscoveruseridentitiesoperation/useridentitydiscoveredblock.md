# userIdentityDiscoveredBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute for each user identity.

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
var userIdentityDiscoveredBlock: ((CKUserIdentity, CKUserIdentity.LookupInfo) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^userIdentityDiscoveredBlock)(CKUserIdentity *identity, CKUserIdentityLookupInfo *lookupInfo);
```

#### Discussion

The closure doesn’t return a value and takes the following parameters:

- The user identity.
- The lookup info that corresponds to the user identity.

The operation executes this closure one or more times for each user identity it discovers. Each time the closure executes, it executes serially with respect to the other closures of the operation.

If you intend to use this closure to process results, set it before you execute the operation or add the operation to a queue.

## See Also

### Processing the Results
- [var discoverUserIdentitiesCompletionBlock: (((any Error)?) -> Void)?](./discoveruseridentitiescompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/useridentitydiscoveredblock)*