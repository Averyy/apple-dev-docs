# modifyRecordZonesResultBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute after CloudKit modifies all of the record zones.

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
var modifyRecordZonesResultBlock: ((Result<Void, any Error>) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameter:

- A [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either: - A successful `Result`, or
- An error that contains information about a problem encountered modifying the record zones.

The closure executes only once, and represents your final opportunity to process the operation’s results. The closure executes serially with respect to the other closures of the operation.

Update the value of this property before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation/modifyrecordzonesresultblock)*