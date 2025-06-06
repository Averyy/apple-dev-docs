# discoverAllUserIdentitiesCompletionBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when the operation finishes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var discoverAllUserIdentitiesCompletionBlock: (((any Error)?) -> Void)? { get set }
```

#### Discussion

The closure doesn’t return a value and takes the following parameter:

- An error if a problem occurs, or `nil` if CloudKit successfully fetches the user identities.

This closure executes only once, after all of the individual discovery closures finish. The closure executes serially with respect to the operation’s other closures. If you intend to use this closure to process results, update the property’s value before you execute the operation or submit it to a queue.

## See Also

- [var userIdentityDiscoveredBlock: ((CKUserIdentity) -> Void)?](ckdiscoveralluseridentitiesoperation/useridentitydiscoveredblock.md)
  The closure to execute for each user identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdiscoveralluseridentitiesoperation/discoveralluseridentitiescompletionblock)*