# discoverAllUserIdentitiesCompletionBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute when the operation finishes.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.12+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 8.0

> **Deprecated**: Use discoverAllUserIdentitiesResultBlock instead

## Declaration

```swift
var discoverAllUserIdentitiesCompletionBlock: (((any Error)?) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^discoverAllUserIdentitiesCompletionBlock)(NSError *operationError);
```

#### Discussion

The closure doesn’t return a value and takes the following parameter:

- An error if a problem occurs, or `nil` if CloudKit successfully fetches the user identities.

This closure executes only once, after all of the individual discovery closures finish. The closure executes serially with respect to the operation’s other closures. If you intend to use this closure to process results, update the property’s value before you execute the operation or submit it to a queue.

## See Also

### Processing the Operation Results
- [var userIdentityDiscoveredBlock: ((CKUserIdentity) -> Void)?](./useridentitydiscoveredblock.md)
  The closure to execute for each user identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdiscoveralluseridentitiesoperation/discoveralluseridentitiescompletionblock)*