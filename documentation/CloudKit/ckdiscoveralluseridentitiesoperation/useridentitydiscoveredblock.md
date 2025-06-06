# userIdentityDiscoveredBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute for each user identity.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var userIdentityDiscoveredBlock: ((CKUserIdentity) -> Void)? { get set }
```

#### Discussion

The closure doesn’t return a value and takes the following parameter:

- The user identity that matches an entry in the device’s Contacts.

The operation executes this closure one or more times for each user identity it discovers. Each time the closure executes, it executes serially with respect to the other closures of the operation.

If you intend to use this closure to process results, set it before you execute the operation or add the operation to a queue.

## See Also

- [var discoverAllUserIdentitiesCompletionBlock: (((any Error)?) -> Void)?](ckdiscoveralluseridentitiesoperation/discoveralluseridentitiescompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdiscoveralluseridentitiesoperation/useridentitydiscoveredblock)*