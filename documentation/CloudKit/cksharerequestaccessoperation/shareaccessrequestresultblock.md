# shareAccessRequestResultBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute after CloudKit processes each share access request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var shareAccessRequestResultBlock: ((Result<Void, any Error>) -> Void)? { get set }
```

#### Discussion

Use this closure to handle the overall success or failure of the operation.

The closure returns no value and takes the following parameter:

- A [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either: - A successful `Result`, or
- An error that contains information about a problem encountered processing the share access requests.

The closure executes only once, and represents your final opportunity to process the operation’s results. It executes after all share access request completion closures finish. The closure executes serially with respect to the other closures of the operation.

Update the value of this property before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharerequestaccessoperation/shareaccessrequestresultblock)*