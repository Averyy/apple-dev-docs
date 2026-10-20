# discoverAllUserIdentitiesResultBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute when the operation finishes.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- visionOS - Deprecated
- watchOS 8.0+ - Deprecated in 10.0

> **Deprecated**: No longer supported. Please see Sharing CloudKit Data with Other iCloud Users.

## Declaration

```swift
var discoverAllUserIdentitiesResultBlock: ((Result<Void, any Error>) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameter:

- A [`Result`](../../Swift/result.md) that contains either:

  - A successful `Result`, or
  - An error that contains information about a problem encountered fetching the user identities.

The closure executes only once, and represents your final opportunity to process the operation’s results. The closure executes serially with respect to the other closures of the operation.

Update the value of this property before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdiscoveralluseridentitiesoperation/discoveralluseridentitiesresultblock)*