# fetchWebAuthTokenResultBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when the operation finishes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
var fetchWebAuthTokenResultBlock: ((Result<String, any Error>) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameter:

- A [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either: - The web authentication token
- An error that contains information about a problem encountered fetching the token.

The closure executes only once. The closure executes serially with respect to the other closures of the operation.

Update the value of this property before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchwebauthtokenoperation/fetchwebauthtokenresultblock)*