# discoverUserIdentitiesResultBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when the operation finishes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+ - Deprecated
- watchOS 8.0+

## Declaration

```swift
var discoverUserIdentitiesResultBlock: ((Result<Void, any Error>) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameter:

- A [`Result`](https://developer.apple.com/documentation/swift/result) that contains either: - A successful `Result`, or
- An error that contains information about a problem encountered fetching the user identities.

This closure executes only once, after all of the individual discovery closures finish. The closure executes serially with respect to the operation’s other closures. If you intend to use this closure to process results, update the property’s value before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdiscoveruseridentitiesoperation/discoveruseridentitiesresultblock)*